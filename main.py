from fastapi import FastAPI
from app.core.config import config
from app.database.db_connection import engine, Base


# Importamos todos los modelos creados para que la Base.metadata la reconozca y las crean.
from app.models.tipo_usuario import TipoUsuario
from app.models.usuario import Usuario
from app.models.valor_glucemico import ValorGlucemico
from app.models.momento_comida import MomentoComida
from app.models.alimento import Alimento
from app.models.registro_comida import RegistroComida

#se crean las tablas mapeadas en postgres, y configuración FASTAPI
Base.metadata.create_all(engine)

app = FastAPI(
    title="Sabores que Cuidan API",
    description="Backend para el control nutricional y glucémico",
    version="1.0.0"
)

# aquí importamos los routers necesarios
from app.api.home_router import router as home_router
from app.api.tipo_usuario_router import router as tipo_usuario_router


# importar las rutas de cada models
app.include_router(home_router)
app.include_router(tipo_usuario_router)



