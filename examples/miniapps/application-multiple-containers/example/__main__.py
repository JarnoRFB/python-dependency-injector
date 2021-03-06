"""Main module."""

import sys

from dependency_injector.wiring import Provide

from .services import UserService, AuthService, PhotoService
from .containers import Application


def main(
        email: str,
        password: str,
        photo: str,
        user_service: UserService = Provide[Application.services.user],
        auth_service: AuthService = Provide[Application.services.auth],
        photo_service: PhotoService = Provide[Application.services.photo],
) -> None:
    user = user_service.get_user(email)
    auth_service.authenticate(user, password)
    photo_service.upload_photo(user, photo)


if __name__ == '__main__':
    application = Application()
    application.config.from_yaml('config.yml')
    application.core.configure_logging()
    application.wire(modules=[sys.modules[__name__]])

    main(*sys.argv[1:])
