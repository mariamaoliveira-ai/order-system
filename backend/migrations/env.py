"""Alembic environment placeholder; application metadata will be wired during TDD."""

from alembic import context


def run_migrations_online() -> None:
    raise NotImplementedError("Wire SQLAlchemy metadata when the first model is implemented")


def run_migrations_offline() -> None:
    raise NotImplementedError("Wire migration metadata when the first model is implemented")


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
