# gunicorn.conf.py
bind = "0.0.0.0:8000"
workers = 3
loglevel = "info"
wsgi_app = "portfolio.wsgi:application"
