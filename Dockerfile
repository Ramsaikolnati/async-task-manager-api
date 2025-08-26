FROM python:3.10
WORKDIR /code
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
# Default command can be overridden (docker-compose sets it)
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
