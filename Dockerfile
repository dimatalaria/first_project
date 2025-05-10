FROM python:3.12-slim

RUN useradd -s /bin/sh -u 1234 nonroot

WORKDIR /usr/src/myapp

RUN apt-get update && apt-get install -y \
    netcat-openbsd \
    curl \
    libpq-dev \
    gcc

RUN curl -sSL https://install.python-poetry.org | python3 -

ENV POETRY_VIRTUALENVS_CREATE=false
ENV PYTHONUNBUFFERED=1

ENV PATH="/root/.local/bin:$PATH"

COPY pyproject.toml poetry.lock ./

RUN poetry install --no-interaction --no-ansi --no-root

COPY entrypoint.sh /usr/src/myapp
COPY src .

RUN sed -i 's/\r$//g' /usr/src/myapp/entrypoint.sh
RUN chmod +x /usr/src/myapp/entrypoint.sh

ENTRYPOINT ["/usr/src/myapp/entrypoint.sh"]

RUN chown -R nonroot:nonroot /usr/src/myapp
USER nonroot

