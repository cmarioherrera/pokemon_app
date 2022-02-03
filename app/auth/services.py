
from dataclasses import dataclass

from werkzeug.security import safe_str_cmp
from app.models import User


users = [
    User(1, 'user1', 'password'),
    User(2, 'user2', 'password')
]


@dataclass
class AuthServices:

    @classmethod
    def get_usernames(cls):
        return {user.username: user for user in users}

    def get_user_ids(cls):
        return {user.id: user for user in users}

    @classmethod
    def authenticate(cls, username, password):
        users = cls.get_usernames()
        user = users[username]
        if user and safe_str_cmp(user.password.encode('utf-8'), password.encode('utf-8')):
            return user
