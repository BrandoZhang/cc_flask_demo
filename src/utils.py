import socket
from collections import defaultdict

hit = 0
visitors_record = defaultdict(int)

def get_hostname():
    return socket.gethostname()

def get_local_address():
    return socket.gethostbyname(socket.gethostname())

def record_visitors(addr):
    global visitors_record
    visitors_record[addr] += 1
    return visitors_record


def hit_count():
    """
    Count server hits.
    """
    global hit
    hit += 1
    return hit