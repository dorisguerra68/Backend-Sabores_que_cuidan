from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_title: str
    app_version: str
    app_description: str

    # DataBase
    db_host: str
    db_port: int
    db_name: str
    db_user: str
    db_password: str

    # Propiedad dinámica para generar la URL de conexión
    @property
    def database_url(self) -> str:
        return (
            f"postgresql+psycopg://{self.db_user}:{self.db_password}"
            f"@{self.db_host}:{self.db_port}/{self.db_name}"
        )

    # Configuración moderna de Pydantic Settings v2
    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding='utf-8',
        case_sensitive=False  # Permite mapear APP_TITLE a app_title, DB_HOST a db_host, etc.
    )

# Instanciamos la clase para exportarla como 'config'
config = Settings()
