# TaskList
Простой бекенд сервис для управления списком задач

## Стек
- FastAPI
- Pydantic
- SQLAlchemy
- PostgreSQL
- Python-jose
- Python-decouple
- PyTest

## Запуск
### Рекомендуется запускать используя Docker
```shell
docker build -t task_list .
docker run task_list
```

### Пример .env файла для запуска
```
DATABASE_IP=127.0.0.1:5432
DATABASE_USER=user
DATABASE_PASSWORD=password
DATABASE_NAME=database_name
JWT_TOKEN_SECRET=my_secret
```

## Документация
**SwaggerUI доступен на endpoint'e `/docs`**

### Структура
- `src/base` - Базовые системы
- `src/controllers` - Логика
- `src/models` - Модели (SQLAlchemy / Pydantic)
- `src/routers` - Endpoint'ы
- `src/app.py` - Основное приложение FastAPI
- `tests` - Unit-тесты
