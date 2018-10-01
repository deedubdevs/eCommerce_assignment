from django.contrib.auth.models import AbstractUser
from django_enumfield import enum
from users.enums.usertypes import UserTypeEnum


class CustomUser(AbstractUser):
    user_type = enum.EnumField(UserTypeEnum, default=UserTypeEnum.REGULAR)

    def __str__(self):
        return self.first_name


def is_owner(self):
    return self.user_type == UserTypeEnum.STORE_OWNER
