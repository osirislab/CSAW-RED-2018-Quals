FROM python:2.7

RUN apt-get update && apt-get install -y python-dev python-pip sqlite3 gunicorn

RUN pip install Flask

COPY cells.py /opt/

EXPOSE 4000
CMD python /opt/cells.py
