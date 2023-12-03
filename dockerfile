FROM python:3.9-slim

RUN apt-get update && apt-get install -y \
  pkg-config \
  libssl-dev \
  python3-dev \
  default-libmysqlclient-dev \
  build-essential \
  iputils-ping

COPY requirements.txt /app/

RUN pip install -r /app/requirements.txt

COPY . /app

WORKDIR /app

EXPOSE 7070

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "7070"]
