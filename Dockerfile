FROM python:3.12

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

ADD pyproject.toml /app

RUN pip install --upgrade pip
RUN pip install poetry

RUN poetry config virtualenvs.create false
RUN poetry install --no-root --no-interaction --no-ansi

COPY . /app

EXPOSE 8000
EXPOSE 5434

CMD ["sh", "-c", "python manage.py makemigrations users && python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]