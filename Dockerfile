FROM python:3.7-alpine
RUN apk add --no-cache bash
WORKDIR /code
RUN apk add --no-cache openssl-dev libffi-dev gcc linux-headers libc-dev git
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
