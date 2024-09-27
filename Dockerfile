FROM python:3.9.20-slim 
WORKDIR /app
COPY main.py .
CMD ["python", "main.py"]