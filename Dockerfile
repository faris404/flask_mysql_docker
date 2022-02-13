FROM python:3.8-slim

WORKDIR app

RUN apt-get -q update -y && apt-get install \
    python3-dev default-libmysqlclient-dev build-essential -y

COPY ./requirements.txt /app/requirements.txt

RUN pip install -r ./requirements.txt

COPY . /app

CMD [ "python", "app.py" ]