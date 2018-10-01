from django_enumfield import enum


class UserTypeEnum(enum.Enum):
    STORE_OWNER = 1
    REGULAR = 2
