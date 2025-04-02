FROM python:3.9-alpine

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN apk add --no-cache gcc musl-dev linux-headers geos libc-dev postgresql-dev && \
    python3 -m pip install --upgrade pip setuptools wheel && \
    pip install -r requirements.txt

COPY . /app/

CMD ["python", "kafka_locations_consumer.py"]