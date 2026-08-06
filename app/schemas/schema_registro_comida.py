from datetime import datetime
from decimal import Decimal
from typing import Optional
from pydantic import BaseModel, ConfigDict
from app.models.registro_comida import horaComidaEnum


# 1. El esquema base con lo mínimo que guarda la tabla
class RegistroComidaBase(BaseModel):
    id_alimento: int
    fecha: datetime
    racion: Decimal
    hora_comida: horaComidaEnum
    observacion: Optional[str] = None
    #añado el nuevo campo necesario para el impacto_glucémico
    impacto_glucemico: str


# 2. El esquema que usará el frontend para ENVIAR una nueva comida (Petición POST)
# El frontend solo manda los IDs y los datos de la ingesta
class RegistroComidaCreate(RegistroComidaBase):
    id_usuario: Optional[int] = 1  #modificado para que no me pida obligatorio el usuario
    #id_rgtcomida: int



# 3. Respuesta simple (Solo IDs)
class RegistroComidaResponse(RegistroComidaBase):
    id_rgtcomida: int
    id_usuario: int

    model_config = ConfigDict(from_attributes=True)


# =====================================================================
# 4. LO QUE TE PEDIRÁ EL FRONTEND PARA LAS PANTALLAS (Petición GET)
# =====================================================================

# Primero creamos el molde de cómo se verá el alimento dentro de la comida
# se añade indíce glucémico para poder obtener la referencia visual
class AlimentoEnComida(BaseModel):
    id_alimento: int
    nombre: str
    categoria: str
    indice_glucemico: int

    model_config = ConfigDict(from_attributes=True)


# Este esquema es completo 'relationship(back_populates="registro_comida")'
class RegistroComidaDetalladoResponse(RegistroComidaResponse):
    alimento: AlimentoEnComida  # <-- Pydantic llena esto automáticamente usando SQLAlchemy
