FROM python:3.12-alpine


# Устанавливаем рабочую директорию  
WORKDIR /app

# Копируем файлы в контейнер  
COPY app.py /app/
COPY requirements.txt /app/

# Устанавливаем зависимости  
RUN pip install Flask
RUN pip install --no-cache-dir -r requirements.txt

# Указываем команду для запуска приложения  
CMD ["python", "app.py"]

EXPOSE 5000