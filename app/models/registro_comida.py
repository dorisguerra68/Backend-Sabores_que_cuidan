import enum
from datetime import datetime
from decimal import Decimal
from typing import Optional, TYPE_CHECKING
from sqlalchemy import Integer, Numeric, Text, ForeignKey, DateTime, Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database.base_class import Base

# Bloque de seguridad contra importaciones circulares
if TYPE_CHECKING:
    from app.models.alimento import Alimento
    from app.models.registro_usuario import Usuario  # Mantiene la referencia al objeto Python


# Creamos la lista desplegable de la hora de comida
class horaComidaEnum(str, enum.Enum):
    DESAYUNO = "Desayuno"
    MEDIA_MANANA = "Media Manana"
    COMIDA = "Comida"
    MERIENDA = "Merienda"
    CENA = "Cena"


class RegistroComida(Base):
    __tablename__ = "registro_comida"

    id_rgtcomida: Mapped[int] = mapped_column(primary_key=True, index=True)

    # Claves foráneas (Físicas en PostgreSQL)
    id_alimento: Mapped[int] = mapped_column(ForeignKey('alimento.id_alimento'), nullable=False)
    id_usuario: Mapped[int] = mapped_column(ForeignKey('registro_usuario.id_usuario'),nullable=False)

    fecha: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    racion: Mapped[Decimal] = mapped_column(Numeric(6, 2), nullable=False)
    observacion: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    # Opción del menú desplegable de hora de comida
    hora_comida: Mapped[horaComidaEnum] = mapped_column(
        Enum(horaComidaEnum),
        nullable=False
    )

    # Relaciones virtuales (Lógica en SQLAlchemy)
    usuario: Mapped["Usuario"] = relationship(back_populates="registro_comida")
    alimento: Mapped["Alimento"] = relationship(back_populates="registro_comida")
