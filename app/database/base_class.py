from sqlalchemy.ext.declarative import declarative_base, as_declarative
from sqlalchemy.orm import declared_attr

#esta es la base que heredan en las tablas
@as_declarative()
class Base:
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()
