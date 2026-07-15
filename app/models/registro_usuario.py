import enum
from datetime import date
from decimal import Decimal
from typing import List, Optional, TYPE_CHECKING
from sqlalchemy import Enum
from sqlalchemy import String, Date, Numeric, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database.base_class import Base

if TYPE_CHECKING:
    from app.models.registro_comida import RegistroComida


class tipoUsuario(str, enum.Enum):
    SANO = "Sano"
    RESISTENTE_INSULINA = "ResistenteInsulina"


class Usuario(Base):
    __tablename__ = 'registro_usuario'

    id_usuario: Mapped[int] = mapped_column(primary_key=True, index=True)
    fecha_registro: Mapped[date] = mapped_column(Date)
    nombre_completo: Mapped[str] = mapped_column(String(140), nullable=False)

    edad: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    sexo: Mapped[Optional[str]] = mapped_column(String(12), nullable=True)
    altura: Mapped[Optional[Decimal]] = mapped_column(Numeric(5, 2), nullable=True)

    tipo_persona: Mapped[tipoUsuario] = mapped_column(
        Enum(
            tipoUsuario,
            values_callable=lambda enum_cls: [e.value for e in enum_cls],
            name="tipousuario"
        ),
        nullable=False,
        default=tipoUsuario.SANO
    )

    estado: Mapped[str] = mapped_column(String(20), default="activo")

    # NUEVO: Email del usuario
    email: Mapped[str] = mapped_column(
        String(140),
        unique=True,
        nullable=False,
        index=True
    )

    # NUEVO: Contraseña hasheada
    password_hash: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    # Relación bidireccional
    registro_comida: Mapped[List["RegistroComida"]] = relationship(back_populates="usuario")
