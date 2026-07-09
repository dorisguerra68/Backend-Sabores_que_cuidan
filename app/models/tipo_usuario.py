from typing import List, TYPE_CHECKING
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base_class import Base

if TYPE_CHECKING:
    from app.models.usuario import Usuario

class TipoUsuario(Base):
    __tablename__ = 'tipo_usuario'
    id_tpu: Mapped[int] = mapped_column(primary_key=True, index=True)
    nombre: Mapped[str] = mapped_column(String(20), nullable=False)


    #  La otra mitad de la relación para que se avisen mutuamente
    usuarios: Mapped[List["Usuario"]] = relationship(back_populates="tipo_usuario")

