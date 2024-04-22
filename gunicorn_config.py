# bind ="0.0.0.0:8080"
# workers = 2

# gunicorn_config.py

# Bind address and port
bind = '0.0.0.0:8000'

# Number of worker processes
workers = 3

# Worker class for handling requests
worker_class = 'sync'

# Timeout for worker processes
timeout = 30
