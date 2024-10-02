FROM python:3.9.20-slim 
WORKDIR /app
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY Pipfile Pipfile.lock /app/
RUN pip install pipenv && pipenv install --ignore-pipfile --python /usr/local/bin/python3.9
COPY main.py app.py /app/
EXPOSE 8000
CMD ["pipenv", "run", "uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]