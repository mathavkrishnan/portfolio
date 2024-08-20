# gunicorn.conf.py
bind = "0.0.0.0:$PORT"
workers = 3
loglevel = "info"
wsgi_app = "portfolio.wsgi:app"
