FROM python:3.8-alpine
MAINTAINER Sharon Kennedy <sharon@nomadiclabs.ca>

ENV PROJECT_ROOT /app
WORKDIR $PROJECT_ROOT

COPY requirements.txt requirements.txt

RUN apk update && \
   apk add postgresql-libs libpq libjpeg zlib && \
   apk add --virtual .build-deps gcc musl-dev postgresql-dev zlib-dev jpeg-dev && \
   python3 -m pip install --upgrade -r requirements.txt --no-cache-dir && \
   apk --purge del .build-deps

COPY . .
CMD python manage.py runserver 0.0.0.0:8000