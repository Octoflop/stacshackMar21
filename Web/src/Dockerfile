FROM ubuntu:latest

RUN apt-get update -y && apt-get install -y python3 python3-dev python3-pip \
    python3-opencv

COPY requirements.txt /requirements.txt

RUN pip3 install -r requirements.txt

ADD . /app

WORKDIR /app

EXPOSE 80

ENTRYPOINT [ "python3" ]

CMD [ "app.py" ]
