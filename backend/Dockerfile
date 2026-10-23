FROM python:3.13-slim

WORKDIR /app

ENV UV_PROJECT_ENVIRONMENT=/usr/local

RUN apt-get update \
    && apt-get install -y --no-install-recommends curl \
    && rm -rf /var/lib/apt/lists/*

RUN curl -LsSf https://astral.sh/uv/install.sh | sh \
    && mv /root/.local/bin/uv /usr/local/bin/uv \
    && mv /root/.local/bin/uvx /usr/local/bin/uvx

COPY pyproject.toml uv.lock /app/
RUN uv sync --frozen --no-editable

COPY /app /app

EXPOSE 8000

CMD ["uv", "run", "uvicorn", "main:app", "--host=0.0.0.0", "--port=8000"]
