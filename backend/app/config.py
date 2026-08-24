from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql+psycopg://order_system:change-me@localhost:5432/order_system"
    KAFKA_BOOTSTRAP_SERVERS: str = "localhost:9092"
    KAFKA_NEW_ORDERS_TOPIC: str = "new-orders"
    KAFKA_CONSUMER_GROUP: str = "order-processor"
    API_HOST: str = "127.0.0.1"
    API_PORT: int = 8000

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

settings = Settings()