import enum
from datetime import datetime
from decimal import Decimal
from typing import Optional, TYPE_CHECKING
from sqlalchemy import Integer, Numeric, Text, ForeignKey, DateTime, Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database.base_class import Base



# Esto solo lo lee tu editor/IDE para el autocompletado, Python lo ignora al ejecutar
if TYPE_CHECKING:
    from app.models.alimento import Alimento

    from app.models.usuario import Usuario
    from app.models.tipo_usuario import TipoUsuario

# creamos las lista desplegable de la hora de comida
class horaComidaEnum(str, enum.Enum):
    DESAYUNO = "Desayuno"
    MEDIA_MANANA = "Media Manana"
    COMIDA = "Comida"
    MERIENDA = "Merienda"
    CENA = "Cena"


class RegistroComida(Base):
    __tablename__ = "registro_comida"

    id_rgtcomida: Mapped[int] = mapped_column(primary_key=True, index=True)

    id_alimento: Mapped[int] = mapped_column(ForeignKey('alimento.id_alimento'), nullable=False)
    # id_usuario: Mapped[int] = mapped_column(ForeignKey('usuario.id_usuario'), nullable=False)
    # id_tpu: Mapped[int] = mapped_column(ForeignKey('tipo_usuario.id_tpu'), nullable=False)

    fecha: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    racion: Mapped[Decimal] = mapped_column(Numeric(6, 2), nullable=False)
    observacion: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    #la opción del menú desplegable de hora de comida
    hora_comida: Mapped[horaComidaEnum] = mapped_column(
        Enum(horaComidaEnum),
        nullable=False
    )



    # usuario: Mapped["Usuario"] = relationship(back_populates="registro_comida")
    # alimento: Mapped["Alimento"] = relationship(back_populates="registro_comida")
