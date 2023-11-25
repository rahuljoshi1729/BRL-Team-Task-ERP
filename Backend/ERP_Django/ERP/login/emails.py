from django.core.mail import send_mail
import random
from django.conf import settings
from .models import LoginUser


def send_otp_via_email(email,user_id,password):
    subject="you account verification email"
    otp=random.randint(1000,9999)
    message=f'your otp is {otp}'
    email_from=settings.EMAIL_HOST_USER
    send_mail(subject,message,email_from,[email])
    user_obj=LoginUser(user_id=user_id,password=password,otp=otp)
    user_obj.save()

def send_passwordreset_mail(email):
    subject="password reset"
    token=generate_jwt_token_reset(email)
    reset_url = f"http://127.0.0.1:8000/api/password/reset/{token}/" 
    message=f'your password reset link is {reset_url}'
    email_from=settings.EMAIL_HOST_USER
    send_mail(subject,message,email_from,[email])
    


import jwt
from datetime import datetime, timedelta
import os
import base64

#generate secret key
""" def generate_secret_key():
    return base64.urlsafe_b64encode(os.urandom(32)).decode('utf-8') """


SECRET_KEY ='P6ZdKYzdqQqFB3n0uHSWcZ2mbHl_L5BPOVPfmJEzRnQ='

def generate_jwt_token(user_id, role):
    payload = {
        'user_id': user_id,
        'role': role,
        'exp': datetime.utcnow() + timedelta(days=1)
    }
    return jwt.encode(payload, SECRET_KEY, algorithm='HS256') 

#for password reset
def generate_jwt_token_reset(email):
    payload = {
        'email': email,
        'exp': datetime.utcnow() + timedelta(days=1)
    }
    return jwt.encode(payload, SECRET_KEY, algorithm='HS256') 


def decode_jwt_token(token):
    try:
        payload = jwt.decode(token,SECRET_KEY, algorithms=['HS256'])
        user_id = payload['user_id']
        role = payload['role']
        return user_id, role
    except jwt.ExpiredSignatureError:
        # Token has expired
        return None, None
    except jwt.InvalidTokenError:
        # Invalid token
        return None, None
    
#for password reset
def decode_jwt_token_reset(token):
    try:
        payload = jwt.decode(token,SECRET_KEY, algorithms=['HS256'])
        email = payload['email']
        return email
    except jwt.ExpiredSignatureError:
        # Token has expired
        return None, None
    except jwt.InvalidTokenError:
        # Invalid token
        return None, None
    

from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
@csrf_exempt
def getdatafromjwt(request):
    jwt_token = request.COOKIES.get('jwt_token')
    if jwt_token:
        try:
            user_id, role = decode_jwt_token(jwt_token)
            data = {'user_id': user_id, 'role': role}
            return Response(data)
        except jwt.ExpiredSignatureError:
            return Response({'error': 'Token expired'}, status=401)
    else:
        return Response({'error': 'Invalid token'}, status=401)
