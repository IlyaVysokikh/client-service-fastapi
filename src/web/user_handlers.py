import logging

from fastapi import APIRouter, Depends, status
from punq import Container

from src.application.auth.register_result_dto import RegisterResultDTO
from src.application.common.handling.Handler import Handler
from src.application.auth.register_command import RegisterCommand
from src.web.container import get_container
from src.web.models.register_dto import RegisterDto


user_router = APIRouter(tags=["Users"])

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@user_router.post(
    "/register",
    summary="Register a new auth",
    description="Endpoint to register a new auth.",
    responses={
        status.HTTP_200_OK: {"model": RegisterResultDTO}
    }
)
async def register_user(
        register_dto: RegisterDto,
        container: Container = Depends(get_container)
) -> RegisterResultDTO:
    """
    Registers a new auth with the provided information.
    """
    handler = container.resolve(Handler[RegisterCommand, RegisterResultDTO])

    result = await handler.execute(register_dto.to_command())
    # if not result.success:
    #     logger.error(f"Error occurred while registering auth: {result.get_errors()}  ")
    # logger.info(f"Идентификатор пользователя: {result.get_value().oid}")

    return result

# @user_router.post(
#     "/authenticate",
#     summary="Authenticate a auth",
#     description="Endpoint to log in a auth."
# )
# async def authenticate_user():
#     """
#     Authenticates a auth with their credentials.
#     """
#     pass
#
# @user_router.post(
#     "/logout",
#     summary="Log out a auth",
#     description="Endpoint to log out an authenticated auth."
# )
# async def logout_user():
#     """
#     Logs out the currently authenticated auth by invalidating their session or token.
#     """
#     pass
#
# @user_router.post(
#     "/confirm-email",
#     summary="Confirm email",
#     description="Endpoint to confirm a auth's email."
# )
# async def confirm_email():
#     """
#     Confirms a auth's email address using a confirmation token.
#     """
    pass
