import logging

logger = logging.getLogger(__name__)


def run() -> None:
    """Start the future Kafka consumption loop."""
    logging.basicConfig(level=logging.INFO)
    logger.info("Order consumer scaffold is ready; Kafka processing is not implemented")


if __name__ == "__main__":
    run()
