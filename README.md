# restaurant-booking
REST API для бронирования столиков в ресторане.

## Запуск
1. Убедитесь, что Docker и docker-compose установлены.
2. Выполните: `docker-compose up --build`
3. Перейдите внутрь контейнера: `docker-compose exec app bash`
4. Выполните первичную миграцию: `alembic revision --autogenerate -m "Initial migration"`
5. Примените миграцию к базе данных: `alembic upgrade head`
6. API будет доступно на `http://localhost:8000`.

## Эндпоинты
- GET /tables/ - список столиков
- POST /tables/ - создать столик
- DELETE /tables/{id} - удалить столик
- GET /reservations/ - список броней
- POST /reservations/ - создать бронь
- DELETE /reservations/{id} - удалить бронь