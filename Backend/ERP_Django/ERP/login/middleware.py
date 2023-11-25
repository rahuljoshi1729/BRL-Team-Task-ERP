
from django.contrib.auth import authenticate
import jwt
from django.conf import settings

class JWTMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        jwt_token = request.COOKIES.get('jwt_token')

        if jwt_token:
            try:
                SECRET_KEY ='P6ZdKYzdqQqFB3n0uHSWcZ2mbHl_L5BPOVPfmJEzRnQ='
                decoded_token = jwt.decode(jwt_token, SECRET_KEY, algorithms=['HS256'])
                user_id = decoded_token.get('user_id')
                role = decoded_token.get('role')

                user = authenticate(request, user_id=user_id, role=role)

                if user:
                    request.user = user
            except jwt.ExpiredSignatureError:
                # Handle token expiration if needed
                pass
            except jwt.InvalidTokenError:
                # Handle invalid token
                pass

        response = self.get_response(request)
        return response
