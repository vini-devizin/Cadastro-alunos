import jwt
import datetime
import os
from dotenv import load_dotenv

load_dotenv('../../../.env')
secret_key = os.getenv('SECRET_KEY')

def generate_token(user_id, user_type):
    """
    -> Generate tokens to auth
    :param user_id: User's id
    :param user_type: User's type
    :return: The token
    """
    times = { # Different times for each user type
        'student': 60,
        'teacher': 30,
        'admin': 15
    }
    exp = datetime.now(datetime.timezone.utc) + datetime.timedelta(minutes=times[user_type])
    payload = {
        'userId': user_id,
        'userType': user_type,
        'exp': exp
    }
    token = jwt.encode(payload, secret_key, algorithm='HS256')
    return token

def verify_token(token):
    """
    -> Verify tokens
    :param token: Token that will be verified
    :return: The payload or if the token has expired or is invalid
    """
    try:
        payload = jwt.decode(token, secret_key, algorithm='HS256')
        return payload
    except jwt.ExpiredSignatureError:
        print('\033[0;33mToken expirado!\033[0m')
    except jwt.InvalidTokenError:
        print('\033[0;31mToken Inválido!\033[0m')
