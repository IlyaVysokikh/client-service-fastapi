from dataclasses import dataclass

from src.application.common.handling.Handler import Handler
from src.application.user.register_command import RegisterCommand
from src.domain.aggregates.user.register_result import RegisterResult
from src.domain.aggregates.user.user_errors import UserErrors
from src.domain.aggregates.user.user_repository import UserRepository
from src.domain.aggregates.user.user_validation_rules import UserValidationRules
from src.domain.result.abstract_result import AbstractResult
from src.domain.result.abstract_result_with_value import AbstractResultWithValue
from src.domain.result.result import Result
from src.domain.services.security_service import SecurityService


@dataclass(frozen=True, eq=False)
class RegisterCommandHandler(Handler[RegisterCommand, RegisterResult]):
    user_repository: UserRepository

    async def execute(self, parameters: RegisterCommand) -> AbstractResultWithValue[RegisterResult]:

        validation_result: AbstractResult = await self.validate(parameters)
        if not validation_result.success:
            return Result.failure_value_errors(validation_result.errors)

        hashed_password: str = SecurityService.hash_password(parameters.password)

        return await self.user_repository.create(
            parameters.name,
            parameters.last_name,
            parameters.email,
            hashed_password
        )

    async def validate(self, command: RegisterCommand) -> AbstractResult:
        if (UserValidationRules.MIN_PASSWORD_LENGTH.value > len(command.password)
                or UserValidationRules.MAX_PASSWORD_LENGTH.value < len(command.password)):
            return Result.failure_value(UserErrors.invalid_password_length)

