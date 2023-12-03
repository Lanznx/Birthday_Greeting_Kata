FROM python:3.9-slim

RUN apt-get update && apt-get install -y \
  pkg-config \
  libssl-dev \
  python3-dev \
  default-libmysqlclient-dev \
  build-essential \
  iputils-ping

COPY requirements.txt /Birthday_Greeting_Kata/

RUN pip install -r /Birthday_Greeting_Kata/requirements.txt

COPY . /Birthday_Greeting_Kata

WORKDIR /Birthday_Greeting_Kata

EXPOSE 7070

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "7070"]
