#! /usr/bin/env python3

import ipaddress, socket, requests
from datetime import date
from optparse import OptionParser
from colorama import Fore, Back, Style
from time import strftime, localtime

status_color = {
    '+': Fore.GREEN,
    '-': Fore.RED,
    '*': Fore.YELLOW,
    ':': Fore.CYAN,
    ' ': Fore.WHITE
}

API_KEY = "YOUR_API_KEY"
viewdns_api = "https://api.viewdns.info/reverseip/?host=IP_ADDRESS&apikey=API_KEY&output=json"

def display(status, data, start='', end='\n'):
    print(f"{start}{status_color[status]}[{status}] {Fore.BLUE}[{date.today()} {strftime('%H:%M:%S', localtime())}] {status_color[status]}{Style.BRIGHT}{data}{Fore.RESET}{Style.RESET_ALL}", end=end)

def get_arguments(*args):
    parser = OptionParser()
    for arg in args:
        parser.add_option(arg[0], arg[1], dest=arg[2], help=arg[3])
    return parser.parse_args()[0]

def getInfo(ip):
    info = {}
    try:
        ipaddress.ip_address(ip)
    except:
        return False
    host = socket.gethostbyaddr(ip)[0]
    info["host"] = host
    response = requests.get(viewdns_api.replace("IP_ADDRESS", ip).replace("API_KEY", API_KEY))
    info["domains"] = [[domain["name"], domain["last_resolved"]] for domain in response.json()["response"]["domains"]] if response.status_code == 200 and int(response.json()["response"]["domain_count"]) > 0 else []
    return info

if __name__ == "__main__":
    pass