import enum


NAMING_CONVENTION = {
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_name)s",
        "ck": "ck_%(table_name)s_`%(constraint_name)s`",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s"
      }


class RolesEnum(int, enum.Enum):
    ADMIN = 0
    USER = 1


class FlashEnum(str, enum.Enum):
  ZETTELDUPLICATE = "A Zettel with that Title and/or Luhmann ID already exists! Please try again!"
  ADMIN_ERROR = 'You are not an admin!'