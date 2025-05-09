FROM python:3.12-slim

RUN useradd -s /bin/sh -u 1234 nonroot

WORKDIR /usr/src/myapp

# Устанавливаем зависимости для Poetry и PostgreSQL
RUN apt-get update && apt-get install -y \
    netcat-openbsd \
    curl \
    libpq-dev \
    gcc

# Устанавливаем Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -

# Указываем, что Poetry должен работать без виртуального окружения
ENV POETRY_VIRTUALENVS_CREATE=false
ENV PYTHONUNBUFFERED=1

# Добавляем Poetry в PATH
ENV PATH="/root/.local/bin:$PATH"

# Копируем файлы зависимостей
COPY pyproject.toml poetry.lock ./

# Устанавливаем зависимости через Poetry
RUN poetry install --no-interaction --no-ansi --no-root

# Копируем код приложения
COPY entrypoint.sh /usr/src/myapp
COPY src .

# Настраиваем entrypoint
RUN sed -i 's/\r$//g' /usr/src/myapp/entrypoint.sh
RUN chmod +x /usr/src/myapp/entrypoint.sh

ENTRYPOINT ["/usr/src/myapp/entrypoint.sh"]

RUN chown -R nonroot:nonroot /usr/src/myapp
USER nonroot

