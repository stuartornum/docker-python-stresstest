FROM python:2-slim

ADD . /srv
RUN /usr/local/bin/pip install -r /srv/requirements.txt

EXPOSE 8000
WORKDIR /srv
ENTRYPOINT ["gunicorn", "-w", "4", "-b", "0.0.0.0:8000", "hello:app"]

