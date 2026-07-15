# Sabores que Cuidan - Backend

Este repositorio contiene la API REST para el proyecto **Sabores que Cuidan**, desarrollada en Python utilizando FastAPI. La aplicación gestiona alimentos, registros de comidas y usuarios, manteniendo un enfoque modular y escalable.

## 🚀 Tecnologías Utilizadas

* **Python 3.x**: Lenguaje de programación principal.
* **FastAPI**: Framework web moderno para construir APIs de alto rendimiento.
* **PostgreSQL**: Sistema de gestión de bases de datos relacional potente y robusto.
* **SQLAlchemy**: ORM para la gestión y consulta de la base de datos.
* **Alembic**: Herramienta de migración ligera para el esquema de la base de datos.
* **Uvicorn**: Servidor ASGI de producción para ejecutar la aplicación.

---

## 📁 Estructura del Proyecto

El backend sigue un diseño arquitectónico limpio dividido por capas:

```text
sabores_que_cuidan/
├── alembic/              # Configuraciones y scripts de migraciones de la base de datos
├── app/                  # Código principal de la aplicación
│   ├── api/              # Capa de enrutamiento (Endpoints)
│   │   ├── alimento_router.py
│   │   ├── home_router.py
│   │   ├── registro_comida_router.py
│   │   └── registro_usuario_router.py
│   ├── controllers/      # Lógica de negocio de la aplicación
│   │   ├── controller_alimento.py
│   │   ├── controller_registro_comida.py
│   │   └── controller_registro_usuario.py
│   ├── core/             # Configuraciones globales y variables de entorno
│   │   └── config.py
│   ├── database/         # Conexión, bases y sesiones de la base de datos
│   │   ├── base.py
│   │   ├── base_class.py
│   │   └── db_connection.py
│   ├── models/           # Modelos de datos de SQLAlchemy (Entidades)
│   └── schemas/          # Esquemas de Pydantic (Validación y serialización de datos)
├── test/                 # Pruebas unitarias y de integración
├── venv/                 # Entorno virtual de Python
├── .env                  # Variables de entorno locales (Privado)
├── .env.example          # Plantilla de ejemplo para las variables de entorno
├── .gitignore            # Archivos excluidos del control de versiones
├── alembic.ini           # Configuración del entorno de Alembic
├── main.py               # Punto de entrada principal de la aplicación FastAPI
├── README.md             # Documentación general del proyecto
└── requirements.txt      # Dependencias y librerías del proyecto
```

---

## 🛠️ Instalación y Configuración Local

Sigue estos pasos para levantar el entorno de desarrollo en tu máquina local:

### 1. Clonar el repositorio
```bash
git clone <URL_DE_TU_REPOSITORIO>
cd sabores_que_cuidan
```

### 2. Configurar el entorno virtual
```bash
# Crear entorno virtual
python -m venv venv

# Activar entorno virtual
# En Windows:
venv\Scripts\activate
# En Linux/macOS:
source venv/bin/activate
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4. Configurar variables de entorno
Copia el archivo de ejemplo:
```bash
cp .env.example .env
```

Abre el archivo `.env` recién creado y configura tus credenciales de PostgreSQL y de la aplicación siguiendo este formato:

```ini
APP_TITLE="Sabores que Cuidan"
APP_VERSION="1.0.0"
APP_DESCRIPTION="Backend API para la gestión de alimentos y usuarios"

DB_HOST=localhost
DB_PORT=5432
DB_NAME=tu_base_de_datos
DB_USER=tu_usuario
DB_PASSWORD=tu_contraseña

DATABASE_URL=postgresql://tu_usuario:tu_contraseña@localhost:5432/tu_base_de_datos
```

### 5. Ejecutar migraciones de base de datos
Para crear todas las tablas en tu base de datos de PostgreSQL mediante Alembic, ejecuta:
```bash
alembic upgrade head
```

---

## ⚡ Ejecución de la Aplicación

Para iniciar el servidor de desarrollo local, ejecuta el siguiente comando:

```bash
uvicorn main:app --reload
```

El servidor estará disponible en: [http://127.0.0.1:8000](http://127.0.0.1:8000)

### 📖 Documentación Interactiva de la API
FastAPI genera documentación automática basada en tus routers y esquemas de validación. Puedes interactuar con ella en:
* **Swagger UI:** [http://127.0.0](http://127.0.0)
* **ReDoc:** [http://127.0.0](http://127.0.0)

---


## 🍏 Gestión del Índice Glucémico (IG)

La entidad de **alimentos** (`app/api/alimento_router.py`) clasifica y valida los ingredientes registrados bajo los estándares clínicos del Índice Glucémico. Los alimentos se categorizan en la base de datos según su impacto en la glucemia postprandial:

| Clasificación del IG | Rango de Valores | Descripción / Ejemplos |
| :--- | :--- | :--- |
| 🟢 **IG Bajo** | `≤ 55` | Legumbres, verduras sin almidón, la mayoría de las frutas enteras. |
| 🟡 **IG Medio** | `56 - 69` | Maíz dulce, plátano maduro, arroz integral, avena tradicional. |
| 🔴 **IG Alto** | `≥ 70` | Pan blanco, arroz blanco, patatas cocidas, azúcares refinados. |
---
## 🚀 Futuras Mejoras (Próxima Fase)

Tras la validación de este MVP, el proyecto evolucionará para ofrecer un cálculo nutricional y glucémico ultra-realista adaptado a las porciones exactas que consume el usuario. Las modificaciones planificadas para la API incluyen:

### 1. Cálculo Proporcional de Macronutrientes
* **Control de Raciones:** Permitir al usuario introducir los gramos exactos consumidos para recalcular dinámicamente los Carbohidratos Totales, Glúcidos (azúcares simples) y Lípidos, superando la base estática de 100g.
* **Fórmula de Conversión:** 
  $$\text{Macronutriente en la Ración (g)} = \frac{\text{Valor Base por 100g} \times \text{Gramos Consumidos}}{100}$$
---
### 2. Implementación de la Carga Glucémica (CG)
Para reflejar el impacto glucémico real en el organismo (y no solo la calidad teórica del carbohidrato), la API calculará la **Carga Glucémica** de la porción introducida mediante la fórmula:
$$\text{Carga Glucémica (CG)} = \frac{\text{IG del Alimento} \times \text{Carbohidratos de la Ración (g)}}{100}$$
---

### 📚 Fuentes Oficiales de Información
Los valores numéricos cargados en la base de datos y los umbrales de validación aplicados por la API se han fundamentado en los criterios y guías oficiales de las siguientes instituciones:

1. **Agencia Española de Seguridad Alimentaria y Nutrición (AESAN)**: Directrices oficiales de nutrición, ingestas de referencia y herramientas de evaluación nutricional en España.
2. **Sistema Nacional de Salud (SNS) - Ministerio de Sanidad de España**: Directrices de nutrición clínica y guías de salud para el control metabólico.
3. **Consejería de Sanidad - Comunidad de Madrid**: Manuales de alimentación saludable, recomendaciones dietéticas oficiales y planes de prevención.
4. **BEDCA** (Base de Datos Española de Composición de Alimentos) para los macronutrientes adaptados al mercado español.

## ✒️ Autores y Créditos

* **Doris Guerra Loreto** - *Desarrollador Full Stack* - [dorisguerra68](https://github.com)

---

