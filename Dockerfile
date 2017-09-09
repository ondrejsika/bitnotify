FROM python:2.7-alpine
MAINTAINER Ondrej Sika <ondrej@ondrejsika.com>

WORKDIR /app

COPY setup.py /app/setup.py
RUN pip install -e .

COPY . /app

CMD ["gunicorn", "wsgi", "-b", "0.0.0.0:80"]

EXPOSE 80
VOLUME /app/db

