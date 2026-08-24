from order_consumer.main import run


def test_consumer_entrypoint_is_importable() -> None:
    assert callable(run)
