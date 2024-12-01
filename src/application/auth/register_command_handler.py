import logging
from dataclasses import dataclass

from src.application.auth.auth_mapper import AuthMapper
from src.application.auth.register_result_dto import RegisterResultDTO
from src.application.common.handling.Handler import Handler
from src.application.auth.register_command import RegisterCommand
from src.domain.aggregates.user.user_errors import UserErrors
from src.domain.aggregates.user.user_repository import UserRepository
from src.domain.aggregates.user.user_validation_rules import UserValidationRules
from src.domain.events.message_producer import MessageProducer
from src.domain.result.abstract_result import AbstractResult
from src.domain.result.result import Result
from src.domain.services.security_service import SecurityService


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@dataclass(frozen=True, eq=False)
class RegisterCommandHandler(Handler[RegisterCommand, RegisterResultDTO]):
    user_repository: UserRepository
    producer: MessageProducer

    topic = "EMAIL"

    async def execute(self, parameters: RegisterCommand) -> RegisterResultDTO:

        validation_result: AbstractResult = await self.validate(parameters)
        if not validation_result.is_success():
            return Result.failure_value_errors(validation_result.get_errors())

        hashed_password: str = SecurityService.hash_password(parameters.password)

        self.producer.produce(self.topic, message=parameters.to_dict())

        result = await self.user_repository.create(
            parameters.name,
            parameters.last_name,
            parameters.email,
            hashed_password
        )

        return AuthMapper.to_register_result_dto(result)

    async def validate(self, command: RegisterCommand) -> AbstractResult:
        if (UserValidationRules.MIN_PASSWORD_LENGTH.value > len(command.password)
                or UserValidationRules.MAX_PASSWORD_LENGTH.value < len(command.password)):
            return Result.failure_value(UserErrors.invalid_password_length)

        return Result.success()

