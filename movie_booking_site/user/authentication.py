import logging
from base64 import b64decode

from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User

logger = logging.getLogger(__name__)


class CustomAuthentication(BaseBackend):
    """
    Custom BasicAuthentication- Authenticates user by username and password given in Authorization header
    """

    def authenticate(self, request):
        username = password = None
        logger.info(request.headers, request.META)

        credentials = request.META.get("HTTP_AUTHORIZATION")
        logger.info("credentials: %s" % credentials)
        if not credentials:
            logger.info("No credentials passed")
        # else:
        #     credentials = credentials.split("")
        #     b64decode(credentials).decode()
        #     username =

        username = request.headers.get("Username")
        password = request.headers.get("Password")

        try:
            user = User.objects.get(username=username)
            pwd_valid = check_password(password, user.password)

            if not pwd_valid:
                logger.critical(
                    "Incorrect password entered for username: %s" % username
                )
                user = None
            credentials = {
                get_user_model().USERNAME_FIELD: username,
                "password": password,
            }
            user = authenticate(**credentials)
            return (user, None)  # authentication successful

        except User.DoesNotExist:
            user = None
            logger.critical("User %s not found" % username)

        return (user, None)

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
