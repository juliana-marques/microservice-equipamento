FROM python:3.9
WORKDIR /app
RUN adduser --disabled-password --gecos '' appuser
RUN pip install Flask gunicorn requests mock flask_wtf flask_testing
COPY ./controller/*.py /app/controller/
COPY ./service/*.py /app/service/
COPY ./tests/*.py /app/tests/
COPY ./repository/*.py /app/repository/
COPY ./model/*.py /app/model/
RUN chown -R appuser:appuser /app
USER appuser
CMD exec gunicorn --bind :"$PORT" --workers 1 --threads 8 --timeout 0 controller.main:app