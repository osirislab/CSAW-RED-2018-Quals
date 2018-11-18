FROM python:2.7

RUN apt-get update && apt-get install -y python-dev python-pip sqlite3 gunicorn

RUN pip install Flask

COPY app /opt/

EXPOSE 4000
CMD python /opt/magic.py
