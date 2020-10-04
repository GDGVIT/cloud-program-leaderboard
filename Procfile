web: gunicorn backend.wsgi
worker: python manage.py celery -A backend worker --loglevel=info --beat