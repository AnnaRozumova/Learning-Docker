FROM python:3.11.10-slim

WORKDIR /app

RUN pip install pipenv
COPY ./Pipfile ./Pipfile.lock ./
RUN pipenv install --system --deploy

COPY ./db_app/ ./

EXPOSE 5000

ENV FLASK_APP=main.py
ENV FLAS_RUN_HOST=0.0.0.0
ENV FLAS_RUN_PORT=5000

CMD ["flask", "run"]