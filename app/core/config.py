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

    # Configuración de Pydantic Settings
    # Línea 20: Permite mapear APP_TITLE a app_title, DB_HOST a db_host, etc.
    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding='utf-8',
        case_sensitive=False,
        extra='ignore'
    )

    # Propiedad dinámica para generar la URL de conexión
    @property
    def database_url(self) -> str:
        return (
            f"postgresql+psycopg://{self.db_user}:{self.db_password}"
            f"@{self.db_host}:{self.db_port}/{self.db_name}"
        )

# se crea la instancia de la clase, para exportarla como 'config'
config = Settings()
