FROM python:3.9
WORKDIR /app
RUN pip install Flask gunicorn requests mock
COPY controller.main .
COPY service/ .
COPY tests/ .
CMD exec gunicorn --bind :"$PORT" --workers 1 --threads 8 --timeout 0 controller.main:app