from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import config
from app.database.db_connection import engine # 🌟 ¡CORREGIDO! Ruta exacta a tu archivo real

# cargamos los modelos de las entidades
from app.database.base_class import Base
from app.models.registro_comida import RegistroComida
from app.models.registro_usuario import Usuario
from app.models.alimento import Alimento

# enlazar los routers
from app.api.home_router import router as home_router
from app.api.alimento_router import router as alimento_router
from app.api.registro_comida_router import router as registro_comida_router
from app.api.registro_usuario_router import router as registro_usuario_router

app = FastAPI(
    title="Sabores que Cuidan API",
    description="Backend para el control nutricional y glucémico",
    version="1.0.0"
)

# 🌟 AUTOMÁTICO: Creará la tabla 'registro_comida' limpia en tu pgAdmin4 con la columna nueva integrada
Base.metadata.create_all(bind=engine)

# configurar el CORS, autoriza unir el Backend con el Frontend.
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "http://localhost:5174",
        "http://127.0.0.1:5174",
        "https://frontend-sabores-que-cuidan-alpha.vercel.app"

    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(home_router)
app.include_router(alimento_router)
app.include_router(registro_comida_router)
app.include_router(registro_usuario_router)
