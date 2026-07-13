from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import config


from app.api.home_router import router as home_router
from app.api.alimento_router import router as alimento_router
from app.api.registro_comida_router import router as registro_comida_router



app = FastAPI(
    title="Sabores que Cuidan API",
    description="Backend para el control nutricional y glucémico",
    version="1.0.0"
)

# configurar el CORS, autoriza unir el Backend con el Frontend.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(home_router)
app.include_router(alimento_router)
app.include_router(registro_comida_router)
