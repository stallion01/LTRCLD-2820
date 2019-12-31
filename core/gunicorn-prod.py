
#IP Bind location
backlog = 2048

#Performance
workers = 4
worker_connections = 100
timeout = 30
keepalive = 2

#Reload on changes
reload = True


#Logging
errorlog = '/var/log/sites/ltraci-3225/error.log'
loglevel = 'info'
accesslog = '/var/log/sites/ltraci-3225/access.log'
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'