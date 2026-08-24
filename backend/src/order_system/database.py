"""Database boundary reserved for SQLAlchemy engine and session setup."""

from collections.abc import Iterator


def get_db_session() -> Iterator[None]:
    """Placeholder dependency for the future request database session."""
    yield None
