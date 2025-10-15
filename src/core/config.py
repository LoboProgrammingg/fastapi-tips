from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Mini CRM API"
    VERSION: str = "1.0.0"
    ENVIRONMENT: str = "development"

    API_KEY_SECRET: str = "super-secreta-chave-de-teste" 

    class Config:
        env_file = ".env" 

settings = Settings()