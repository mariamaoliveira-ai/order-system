from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    database_url: str = "postgresql+psycopg://order_system:change-me@localhost:5432/order_system"
    kafka_bootstrap_servers: str = "localhost:9092"
    kafka_new_orders_topic: str = "new-orders"
    kafka_consumer_group: str = "order-processor"
    api_host: str = "127.0.0.1"
    api_port: int = 8000

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()
