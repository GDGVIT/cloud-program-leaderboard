web: gunicorn backend.wsgi
worker: celery -A backend worker --loglevel=info --beat