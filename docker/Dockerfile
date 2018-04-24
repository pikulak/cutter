FROM python:3.6.2

# Django doesn't run without this flag in some cases
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY docker/bin/wait-for-it.sh /wait-for-it.sh
RUN chmod +x /wait-for-it.sh

COPY docker/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
