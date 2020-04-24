FROM alpine:3.11
LABEL maintainer="halon.filip@gmail.com"

FROM python:3.7-alpine
RUN apk --update add gcc build-base freetype-dev libpng-dev openblas-dev postgresql-dev python3-dev musl-dev zlib-dev jpeg-dev

ENV LIBRARY_PATH=/lib:/usr/lib
ENV PYTHONUNBUFFERED 1

RUN mkdir /movienager
WORKDIR /movienager

ADD ./Pipfile /movienager/Pipfile
RUN pip install pipenv && pipenv install --skip-lock --system --dev

ADD . /movienager/

RUN adduser -D user
USER user
