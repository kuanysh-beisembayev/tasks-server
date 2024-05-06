FROM python:3.12-slim-bullseye

RUN useradd --create-home --home-dir /app --shell /bin/bash app
WORKDIR /app

COPY requirements ./requirements
RUN pip install --disable-pip-version-check --no-cache-dir -r requirements/base.txt

COPY . .
USER app
