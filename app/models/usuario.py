from datetime import date
from decimal import Decimal
from typing import List,Optional, TYPE_CHECKING
from sqlalchemy import String, Date, Numeric, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database.base_class import Base

# Chequeamos el modelo para que Python conozca el tipo de  relacionar
if TYPE_CHECKING:
    from app.models.tipo_usuario import TipoUsuario
    from app.models.registro_comida import RegistroComida

class Usuario(Base):
    __tablename__ = 'usuario'

    id_usuario: Mapped[int] = mapped_column(primary_key=True, index=True)
    id_tpu: Mapped[int] = mapped_column(ForeignKey('tipo_usuario.id_tpu'), nullable=False)
    fecha_registro: Mapped[date] = mapped_column(Date)
    nombre_completo: Mapped[str] = mapped_column(String(140), nullable=False)
    # Campos que permiten nulos (Optional en Python / nullable=True en SQL)
    edad: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    sexo: Mapped[Optional[str]] = mapped_column(String(12), nullable=True)
    altura: Mapped[Optional[Decimal]] = mapped_column(Numeric(5, 2), nullable=True)

    # Campo con valor por defecto
    estado: Mapped[str] = mapped_column(String(20), default="activo")

    # Campos comentados por si decides usarlos en el futuro
    # email: Mapped[str] = mapped_column(String(130), unique=True, nullable=False)
    # password_hash: Mapped[str] = mapped_column(String, nullable=False)

    # Relación virtual bidireccional (Le avisa a TipoUsuario)
    tipo_usuario: Mapped["TipoUsuario"] = relationship(back_populates="usuarios")
    registro_comida: Mapped[List["RegistroComida"]] = relationship(back_populates="usuario")