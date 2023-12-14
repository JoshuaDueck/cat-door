from sqlalchemy.types import TypeDecorator
from sqlalchemy import Integer


class UnixTimestamp(TypeDecorator):
    impl = Integer

    def process_bind_param(self, value, dialect):
        if value is not None:
            return int(value.timestamp())
        else:
            return None
