# gunicorn.conf.py
bind = "127.0.0.1"
workers = 3
loglevel = "info"
wsgi_app = "portfolio.wsgi:application"
