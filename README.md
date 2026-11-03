# group25082026fastapi

test rewritten ha-ha 2


# alembic
- uv run alembic init -t async migrations
- uv run alembic revision --autogenerate -m "create user table"
- uv run alembic upgrade head
- uv run alembic current
- uv run alembic history
- uv run alembic downgrade -1
