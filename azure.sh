python manage.py collectstatic --noinput

gunicorn --bind=0.0.0.0 --timeout 600 jobsPy.wsgi --workers=4 & celery -A jobsPy worker --loglevel=info -P eventlet -E