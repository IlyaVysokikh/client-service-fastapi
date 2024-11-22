from fastapi import APIRouter, Depends, status
from punq import Container

from src.application.common.handling.Handler import Handler
from src.application.user.register_command import RegisterCommand
from src.domain.aggregates.user.register_result import RegisterResult
from src.domain.result.abstract_result_with_value import AbstractResultWithValue
from src.web.container import get_container
from src.web.models.register_dto import RegisterDto


user_router = APIRouter(tags=["Users"])


@user_router.post(
    "/register",
    summary="Register a new user",
    description="Endpoint to register a new user.",
    responses={
        status.HTTP_200_OK: {"model": AbstractResultWithValue[RegisterResult]}
    }
)
async def register_user(
        register_dto: RegisterDto,
        container: Container = Depends(get_container)
) -> AbstractResultWithValue[RegisterResult]:
    """
    Registers a new user with the provided information.
    """
    handler = container.resolve(Handler[RegisterCommand, RegisterResult])

    return await handler.execute(register_dto=register_dto.to_command())

# @user_router.post(
#     "/authenticate",
#     summary="Authenticate a user",
#     description="Endpoint to log in a user."
# )
# async def authenticate_user():
#     """
#     Authenticates a user with their credentials.
#     """
#     pass
#
# @user_router.post(
#     "/logout",
#     summary="Log out a user",
#     description="Endpoint to log out an authenticated user."
# )
# async def logout_user():
#     """
#     Logs out the currently authenticated user by invalidating their session or token.
#     """
#     pass
#
# @user_router.post(
#     "/confirm-email",
#     summary="Confirm email",
#     description="Endpoint to confirm a user's email."
# )
# async def confirm_email():
#     """
#     Confirms a user's email address using a confirmation token.
#     """
    pass
