# gunicorn.conf.py
bind = "0.0.0.0"
workers = 3
#user = "myusername"
#group = "mygroup"
loglevel = "info"
#accesslog = "/path/to/access.log"
#errorlog = "/path/to/error.log"
#pidfile = "/path/to/gunicorn.pid"
daemon = True

wsgi_app = "portfolio.wsgi:app"
