FROM python:3.11.10-slim

WORKDIR /app

RUN pip install pipenv
COPY ./Pipfile ./Pipfile.lock ./
RUN pipenv install --system --deploy

COPY ./app/ ./

CMD ["python", "main.py"]