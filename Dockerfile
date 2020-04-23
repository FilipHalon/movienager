FROM python:3.7

RUN mkdir /movienager_image
WORKDIR /movienager_image

ADD . /movienager_image/

ENV PYTHONUNBUFFERED 1
ENV LANG C.UTF-8

COPY requirements.txt /code/
RUN pip install -r requirements.txt
