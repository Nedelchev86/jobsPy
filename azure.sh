
gunicorn --bind=0.0.0.0 --timeout 600 jobsPy.wsgi & celery -A jobsPy worker --loglevel=info -P eventlet -E