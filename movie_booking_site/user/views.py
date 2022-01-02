import json
import logging

from django.contrib.auth.models import User
from django.http import HttpResponse
from rest_framework.views import APIView

logger = logging.getLogger(__name__)


class RegisterUser(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        response = {"status": False, "message": ""}
        status_code = 200
        try:

            data = request.data
            username = data.get("username")
            email = data.get("email")
            password = data.get("password")

            if not (username and email and password):
                response.update(
                    {
                        "message": "Please provide mandatory fields- username, email and password"
                    }
                )
                status_code = 400
                return HttpResponse(json.dumps(response), status=status_code)

            if ":" in username or ":" in password:
                # do not allow ':' in credentials
                response.update({"message": "Credentials cannot contain character ':'"})
                status_code = 400
                return HttpResponse(json.dumps(response), status=status_code)

            user = User.objects.create_user(username, email, password)
            logger.info("User %s created" % username)

            if data.get("firstname"):
                user.first_name = data.get("firstname")
            if data.get("lastname"):
                user.last_name = data.get("lastname")
            user.save()

            response.update({"status": True, "message": "User Created"})
            status_code = 201

        except Exception as e:
            logger.critical("Exception in RegisterUser: %s", str(e))
            response.update({"error": str(e)})

        return HttpResponse(
            json.dumps(response), content_type="application/json", status=status_code
        )
