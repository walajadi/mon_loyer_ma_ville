FROM python:3.9

COPY requirements.txt /tmp/
RUN pip install --requirement /tmp/requirements.txt
ADD backend /app
EXPOSE 8000
WORKDIR /app
CMD gunicorn backend.wsgi:application -b 127.0.0.1:8000 -w 9 -t 60 --access-logfile - --error-logfile -

