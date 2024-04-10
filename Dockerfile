FROM python:3.11-alpine

WORKDIR /app

COPY pyproject.toml /app/pyproject.toml
RUN pip install poetry
RUN poetry install

COPY . .


ENV CELERY_BROKER_URL=pyamqp://guest@localhost//

CMD [ "poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"] & \
    celery -A tasks worker --loglevel=INFO
