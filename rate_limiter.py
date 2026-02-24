from time import time

request_log = {}
RATE_LIMIT = 5
TIME_WINDOW = 10

def is_rate_limited(ip):
    current_time = time()
    if ip not in request_log:
        request_log[ip] = []
    
    request_log[ip] = [t for t in request_log[ip] if current_time - t < TIME_WINDOW]
    request_log[ip].append(current_time)
    
    return len(request_log[ip]) > RATE_LIMIT