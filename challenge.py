from schedule import every, repeat, run_pending # you need to install schedule with pip install schedule
import time

ip_group = {}

def request_handled(ip_address):
    if  ip_address in ip_group.keys():
        ip_group[ip_address] += 1
    else:
        ip_group[ip_address] = 0


def top100():
    return sorted(ip_group.items(), key=lambda x: x[1], reverse=True)[:100].keys


@repeat(every().day.at("23:59:59"))
def clear():
    ip_group = {}
    
    
while True:
    run_pending()
    time.sleep(1)