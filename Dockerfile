FROM python:3.7-alpine
LABEL maintainer="halon.filip@gmail.com"
RUN apk --update add build-base postgresql-dev python3-dev musl-dev zlib-dev jpeg-dev

ENV LIBRARY_PATH=/lib:/usr/lib
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/movienager

ADD ./Pipfile /usr/src/movienager/Pipfile
RUN pip install pipenv && pipenv install --skip-lock --system --dev

ADD ./movienager /usr/src/movienager/

RUN adduser -D user
USER user
