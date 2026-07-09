from fastapi import FastAPI
from app.core.config import config


from app.api.home_router import router as home_router
from app.api.tipo_usuario_router import router as tipo_usuario_router



app = FastAPI(
    title="Sabores que Cuidan API",
    description="Backend para el control nutricional y glucémico",
    version="1.0.0"
)

app.include_router(home_router)
app.include_router(tipo_usuario_router)
