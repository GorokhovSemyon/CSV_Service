# Используем базовый образ Python
FROM python:3.9

# Устанавливаем переменные окружения для Django
ENV DJANGO_SETTINGS_MODULE=csv_serv.settings
ENV PYTHONUNBUFFERED 1

# Создаем и переключаемся в рабочую директорию /app
RUN mkdir /app
WORKDIR /app

# Копируем requirements.txt в рабочую директорию
COPY requirements.txt /app/

# Устанавливаем зависимости Python
RUN pip install -r requirements.txt

# Копируем остальные файлы проекта в рабочую директорию
COPY . /app/

# Собираем статические файлы Django
RUN python manage.py collectstatic --noinput

# Запускаем Gunicorn для обслуживания приложения Django
CMD ["gunicorn", "csv_serv.wsgi:application", "--bind", "0.0.0.0:8000"]