from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict
# Root folder (order-system/)
ROOT_DIR = Path(__file__).resolve().parent.parent.parent

class Settings(BaseSettings):
    DATABASE_URL: str 
    KAFKA_BOOTSTRAP_SERVERS: str = "localhost:9092"
    KAFKA_NEW_ORDERS_TOPIC: str = "new-orders"
    KAFKA_CONSUMER_GROUP: str = "order-processor"
    API_HOST: str = "127.0.0.1"
    API_PORT: int = 8000

    model_config = SettingsConfigDict(env_file= ROOT_DIR / ".env", extra="ignore")

settings = Settings()