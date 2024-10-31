FROM python:3.11.10-slim

WORKDIR /app

RUN pip install pipenv
COPY ./Pipfile ./Pipfile.lock ./
RUN pipenv install --deploy --ignore-pipfile

COPY ./db_app/ ./

CMD ["python", "main.py"]