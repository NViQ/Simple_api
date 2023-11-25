if [ ! -f "/opt/app/.initialized" ]; then
    python manage.py createsuperuser --no-input
    touch /opt/app/.initialized
fi

exec uwsgi --ini uwsgi.ini