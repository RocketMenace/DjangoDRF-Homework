
# Домашняя работа 26.2

Модуль: Celery.


## Локальный запуск

Клонировать используя указаный URL.

```bash
  git clone https://github.com/RocketMenace/Homework-24.1.git
```

Установить зависимости из файла pyproject.toml

```bash
  poetry install
```

Запуск сервера

```bash
  python3 manage.py runserver
```
```bash
  python3 manage.py createmoderatorgroup
```
```bash
  python3 manage.py createmoderator
```
```bash
  python3 manage.py csu
```
Запуск периодических задач 

```bash
  celery -A config worker --loglevel=info --beat
```

Запуск из контейнера используя docker compose file. 

```bash
  docker-compose up
```
