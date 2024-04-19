# Test Task for UTF


### Описание:

- Добавил представление, которое возвращает JSON требуемого формата.
- Изменил сериализатор FoodListSerializer для корректного отображения данных.
- Добавил фабрики для создания минимального количества данных:
  - 3 категории блюд(к одной из них не принадлежит ни одно блюдо)
  - 3 блюда с полем is_publish=True
  - 3 блюда с полем is_publish равным True/False 50/50.


### Используемые технологии:

[![pre-commit](https://img.shields.io/badge/Python-3.11-3776AB?logo=python&logoColor=white)](https://www.python.org/downloads/release/python-3111/)
[![pre-commit](https://img.shields.io/badge/Django-3.2-092E20?logo=django&logoColor=white)](https://docs.djangoproject.com/en/4.2/releases/3.2/)
[![pre-commit](https://img.shields.io/badge/Django_REST_framework-3.12-800000?logo=djangorestramework&logoColor=white)](https://www.django-rest-framework.org/community/3.12-announcement/)
[![sqlite](https://img.shields.io/badge/-sqlite-464646?style=flat-square&logo=sqlite)](https://www.sqlite.org/docs.html)
[![Nginx](https://img.shields.io/badge/-NGINX-464646?style=flat-square&logo=NGINX)](https://nginx.org/ru/)
[![gunicorn](https://img.shields.io/badge/-gunicorn-464646?style=flat-square&logo=gunicorn)](https://gunicorn.org/)
[![docker](https://img.shields.io/badge/-Docker-464646?style=flat-square&logo=docker)](https://www.docker.com/)

### Для запуска:

1. **Установка:** Клонируйте репозиторий на свой компьютер.
2. **Docker Compose:** Перейдите в директорию проекта и выполните следующие команды для запуска приложения с использованием Docker Compose.

```bash
docker compose build
docker compose up
```
3. **Доступ к ендпоинту:** После завершения настройки среды Docker Compose, вы можете запросить данные:

    ```GET http://127.0.0.1/api/v1/foods/```
