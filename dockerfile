FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN apt update && apt install -y libpq-dev gcc
RUN pip install --upgrade pip setuptools wheel
RUN pip install --no-cache-dir -r requirements.txt && pip list

CMD ["python", "-m", "main"]
