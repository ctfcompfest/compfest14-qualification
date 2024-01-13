import multiprocessing

bind = "127.0.0.1:1337"
workers = 10
threads = 3
worker_class = 'sync'
worker_connections = 1000
max_requests = 100
timeout = 1
graceful_timeout = 1