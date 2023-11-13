FROM python:3.9
WORKDIR /app
RUN pip install Flask gunicorn requests
COPY . .
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 main:app
