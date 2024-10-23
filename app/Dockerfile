FROM python:3.11.10-slim

WORKDIR /app

RUN pip install pipenv
COPY ./Pipfile ./Pipfile.lock ./
RUN pipenv install --system --deploy

COPY ./app/ ./

EXPOSE 8080

ENV FLASK_APP=app.py
ENV FLAS_RUN_HOST=0.0.0.0
ENV FLAS_RUN_PORT=8080

CMD ["flask", "run"]