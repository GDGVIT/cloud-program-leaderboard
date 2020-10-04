web: gunicorn backend.wsgi
worker: celery -A backend worker -l info
beat: celery -A backend beat -l INFO