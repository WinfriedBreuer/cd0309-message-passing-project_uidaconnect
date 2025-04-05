FROM python:3.7-slim-bullseye

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN python3 -m pip install --upgrade pip setuptools wheel && \
    pip install -r requirements.txt


EXPOSE 5000

COPY . /app

CMD ["python", "main.py"]

