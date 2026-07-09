from typing import List, TYPE_CHECKING
from sqlalchemy import String
from sqlalchemy.orm import Mapped,mapped_column,relationship
from app.database.base_class import Base

if TYPE_CHECKING:
    from app.models.registro_comida import RegistroComida

class MomentoComida(Base):
     __tablename__ = 'momento_comida'

     id_momentoc: Mapped[int] = mapped_column(primary_key=True, index=True)
     nombre: Mapped[str] = mapped_column(String(15), nullable=False, unique=True)

     #se relaciona con registro de comida
     registro_comida: Mapped[List["RegistroComida"]] = relationship(back_populates="momento_comida")
