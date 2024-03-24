import requests
import time
from colorama import Fore, Style
from urllib.parse import urlparse
import socket
import os

# Inisialisasi warna
fr = Fore.RED
fg = Fore.GREEN
fy = Fore.YELLOW
fm = Fore.MAGENTA
fc = Fore.CYAN
fres = Style.RESET_ALL

def banner():
  os.system("clear")
  print(f"""{fr}     _  _   _  _ ___   _     _____  _____ _    ___ ___ _____ 
  _ | |/_\ | \| |   \ /_\   | __\ \/ / _ \ |  / _ \_ _|_   _|  :: BY TPNET SERVICE{fres}
 | || / _ \| .` | |) / _ \  | _| >  <|  _/ |_| (_) | |  | |    :: CODER BY ./lyx
  \__/_/ \_\_|\_|___/_/ \_\ |___/_/\_\_| |____\___/___| |_|    :: TOOLS SCAN VULN SQLI
                                                             """)
                                                             
def get_ip_address(url):
    parsed_url = urlparse(url)
    domain = parsed_url.netloc
    try:
        ip_address = socket.gethostbyname(domain)
        return ip_address
    except socket.gaierror as e:
        print(f"[{fc}{time.strftime(f'%H:%M:%S')}{fres}] [{fr}CRITICAL{fres}] Failed to resolve IP for {domain}: {e}")
        return None

def get_server_info(url):
    parsed_url = urlparse(url)
    domain = parsed_url.netloc
    try:
        ip_address = get_ip_address(url)
        if ip_address:
            server_info = socket.gethostbyaddr(ip_address)
            return server_info
        else:
            return None
    except socket.herror as e:
        print(f"\n{fc}[{time.strftime('%H:%M:%S')}{fres}] [{fr}CRITICAL{fres}] Failed to get server info for {domain}: {e}\n")
        return None

def check_sql_injection(url):
    try:
        response = requests.get(url)
    except requests.exceptions.RequestException as e:
        print(f"\n[{fc}{time.strftime('%H:%M:%S')}{fres}] [{fr}CRITICAL{fres}] Error accessing {url}: {e}{fres}\n")
        return

    # Inisialisasi variabel untuk menyimpan detail
    detail = {
        'url': url,
        'domain': '',
        'status': response.status_code,
        'vulnerability': False,
        'waf_protection': [],
        'real_ip': None,
        'server_info': None
    }

    # Periksa apakah terdapat indikasi error database seperti MySQL, PostgreSQL, dll.
    if "error" in response.text.lower():
        detail['vulnerability'] = True
        print(f"[{fc}{time.strftime('%H:%M:%S')}{fres}] [{fg}INFO{fres}] Vulnerable to SQL Injection: {fm}{url}{fres}")

        # Periksa tanda-tanda pelindung WAF dalam header respons HTTP
        waf_headers = [
    'WAF', 'X-Frame-Options', 'WAF-Version', 'Web-Application-Firewall',
    'Server', 'X-Mod-Security', 'X-WebKnight', 'X-AspNet-Version',
    'X-Runtime', 'X-Powered-By', 'X-Cdn',
    'X-Content-Security-Policy', 'X-Permitted-Cross-Domain-Policies',
    'X-XSS-Protection', 'Content-Security-Policy', 'X-Content-Type-Options',
    'X-Content-Security-Policy-Report-Only', 'X-Content-Security-Policy-Report-Only',
    'X-Robots-Tag', 'X-Download-Options', 'X-DNS-Prefetch-Control',
    'X-Frame-Options', 'X-Powered-By', 'X-UA-Compatible', 'X-Content-Type-Options',
    'Strict-Transport-Security', 'Barracuda', 'SonicWall', 'Cloudflare',
    'Barracuda WAF-as-a-Service', 'Barracuda Web Application Firewall',
    'F5 Distributed Cloud WAF (Web Application Firewall)', 'ModSecurity',
    'Sucuri', 'Imperva Incapsula', 'F5 BIG-IP Application Security Manager',
    'FortiWeb', 'Akamai Kona Site Defender', 'Citrix NetScaler AppFirewall',
    'Wallarm', 'Armor Defense', 'Radware AppWall', 'AppTrana', 'SiteLock',
    'PerimeterX', 'Distil Networks', 'StackPath WAF', 'Comodo cWatch',
    'Sucuri CloudProxy', 'Wordfence', 'SiteGuard WP Plugin', 'NinjaFirewall',
    'BulletProof Security', 'WP Cerber Security', 'Acunetix', 'Netsparker',
    'Qualys Web Application Scanning (WAS)', 'Rapid7 AppSpider', 'Tenable.io Web Application Scanning',
    'Nmap NSE Scripts', 'OWASP ZAP (Zed Attack Proxy)', 'Burp Suite', 'SQLMap',
    'AppSpider', 'Qualys WAS', 'Netsparker', 'IBM Security AppScan', 'Veracode',
    'Trustwave App Scanner', 'Arachni', 'w3af', 'Skipfish', 'Grabber'
]

        for header in waf_headers:
            if header in response.headers:
                detail['waf_protection'].append(header)

        if detail['waf_protection']:
            print(f"[{fc}{time.strftime('%H:%M:%S')}{fres}] [{fr}CRITICAL{fres}] WAF Protection Detected: {fm}{', '.join(detail['waf_protection'])}{fres}")

        detail['real_ip'] = get_ip_address(url)
        if detail['real_ip']:
            print(f"[{fc}{time.strftime('%H:%M:%S')}{fres}] [{fg}INFO{fres}] Retrive Real IP: {fm}{detail['real_ip']}{fres}")
            detail['server_info'] = get_server_info(url)
            if detail['server_info']:
                print(f"{fc}[{time.strftime('%H:%M:%S')}{fres}] [{fg}INFO{fres}] Retrive Server Info: {fm}{detail['server_info'][0]} - {detail['server_info'][2][0]}{fres}")
            else:
                print(f"[{fc}{time.strftime('%H:%M:%S')}{fres}] [{fr}CRITICAL{fres}] Failed to get server info{fres}")
        else:
            print(f"[{fc}{time.strftime('%H:%M:%S')}{fres}] [{fr}CRITICAL{fres}] Failed to resolve IP for: {fm}{url}{fres}")

        print(f"[{fc}{time.strftime('%H:%M:%S')}{fres}] [{fg}INFO{fres}] Status Code: {fm}{detail['status']}\n{fres}")
    else:
        print(f"\n[{fc}{time.strftime('%H:%M:%S')}{fres}] [{fr}CRITICAL{fres}] Not Vulnerable to SQL Injection: {fm}{url}{fres}")
        detail['real_ip'] = get_ip_address(url)
        if detail['real_ip']:
            print(f"[{fc}{time.strftime('%H:%M:%S')}{fres}] [{fg}INFO{fres}] IP Address: {fm}{detail['real_ip']}{fres}")
            detail['server_info'] = get_server_info(url)
            if detail['server_info']:
                print(f"[{fc}{time.strftime('%H:%M:%S')}{fres}] [{fg}INFO{fres}] Server Info: {fm}{detail['server_info'][0]} - {detail['server_info'][2][0]}{fres}")
            else:
                print(f"[{fc}{time.strftime('%H:%M:%S')}{fres}] [{fr}CRITICAL{fres}] Failed to get server info{fres}")
        else:
            print(f"[{fc}{time.strftime('%H:%M:%S')}{fres}] [{fr}CRITICAL{fres}] Failed to resolve IP for: {fm}{url}{fres}")

def login():
  print(f"[{fc}{time.strftime('%H:%M:%S')}{fres}] [{fg}INFO{fres}] MAAF JIKA SCAN TERLALU LAMA ANDA BISA MENGECEK TERLEBIH DAHULU KONEKSI ANDA ATAU ANDA DAPAT MENUNGGU SCANNYA BERJALAN TERIMAKASIH:)")

# Membaca daftar URL dari file target.txt
with open("target.txt", "r") as file:
    urls = file.readlines()
    urls = [url.strip() for url in urls]  # Menghapus karakter newline (\n) dari setiap URL
banner()
login()
# Periksa setiap URL dalam daftar
for url in urls:
    check_sql_injection(url)
    
    
