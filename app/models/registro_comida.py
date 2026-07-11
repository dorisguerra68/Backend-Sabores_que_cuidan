from datetime import datetime
from decimal import Decimal
from typing import Optional, TYPE_CHECKING
from sqlalchemy import String, Integer, Numeric, Text, ForeignKey, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database.base_class import Base

# Importamos el modelo para que Python conozca el tipo
from app.models.usuario import Usuario

# Esto solo lo lee tu editor/IDE para el autocompletado, Python lo ignora al ejecutar
if TYPE_CHECKING:
    from app.models.usuario import Usuario
    from app.models.alimento import Alimento
    from app.models.tipo_usuario import TipoUsuario
    from app.models.momento_comida import MomentoComida


class RegistroComida(Base):
    __tablename__ = "registro_comida"

    id_rgtcomida: Mapped[int] = mapped_column(primary_key=True, index=True)

    # id_usuario: Mapped[int] = mapped_column(ForeignKey('usuario.id_usuario'), nullable=False)
    id_alimento: Mapped[int] = mapped_column(ForeignKey('alimento.id_alimento'), nullable=False)
    # id_tpu: Mapped[int] = mapped_column(ForeignKey('tipo_usuario.id_tpu'), nullable=False)
    # id_momentoc: Mapped[int] = mapped_column(ForeignKey('momento_comida.id_momentoc'), nullable=False)

    fecha: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    racion: Mapped[Decimal] = mapped_column(Numeric(6, 2), nullable=False)
    observacion: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    # CORREGIDO: Todas las relaciones comentadas de forma segura y alineadas con 4 espacios
    # momento_comida: Mapped["MomentoComida"] = relationship(back_populates="registro_comida")
    # usuario: Mapped["Usuario"] = relationship(back_populates="registro_comida")
    # alimento: Mapped["Alimento"] = relationship(back_populates="registro_comida")
