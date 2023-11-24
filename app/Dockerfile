FROM python:3.10

WORKDIR /opt/app

ENV DJANGO_SETTINGS_MODULE 'drfproject.settings'

COPY run_uwsgi.sh run_uwsgi.sh
COPY requirements.txt requirements.txt
COPY uwsgi/uwsgi.ini uwsgi.ini

RUN apt-get update && apt-get install -y wait-for-it

RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

COPY . .
RUN mkdir -p /opt/app/static
RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD wait-for-it db:5432 -- python manage.py migrate && uwsgi --ini uwsgi.ini
