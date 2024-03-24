import socket
import requests
import whois

def get_ip(domain):
    try:
        ip = socket.gethostbyname(domain)
        return ip
    except socket.gaierror:
        return None

def get_location(ip):
    try:
        response = requests.get(f"http://ip-api.com/json/{ip}")
        data = response.json()
        return {
            "country": data.get("country", "Unknown"),
            "city": data.get("city", "Unknown"),
            "zip": data.get("zip", "Unknown"),
            "region": data.get("regionName", "Unknown"),
            "timezone": data.get("timezone", "Unknown"),
            "isp": data.get("isp", "Unknown"),
            "org": data.get("org", "Unknown"),
            "ip_range": f"{data.get('query', 'Unknown')} - {data.get('query', 'Unknown')}"
        }
    except requests.RequestException:
        return {
            "country": "Unknown",
            "city": "Unknown",
            "zip": "Unknown",
            "region": "Unknown",
            "timezone": "Unknown",
            "isp": "Unknown",
            "org": "Unknown",
            "ip_range": "Unknown"
        }

def get_hosting_provider(domain):
    try:
        domain_info = whois.whois(domain)
        registrar = domain_info.registrar
        if registrar:
            return registrar
        name_servers = domain_info.name_servers
        if name_servers:
            return name_servers[0]
        return None
    except whois.parser.PywhoisError:
        return None

def check_mysql_database(domain):
    # Implementasi ini akan bergantung pada cara pengecekan yang spesifik untuk database MySQL.
    # Ini bisa menjadi cek koneksi langsung ke database atau melalui API jika disediakan oleh penyedia hosting.
    # Di sini saya akan memberikan contoh sederhana.
    # Gantilah dengan implementasi yang sesuai dengan kebutuhan Anda.
    return "Yes"  # Misalnya, kembalikan "Yes" jika database MySQL ditemukan.

def main():
    while True:
        domain_url = input("Masukkan URL: ")
        
        # Mendapatkan alamat IP
        ip = get_ip(domain_url)
        
        if ip:
            # Mendapatkan lokasi dari alamat IP
            location_info = get_location(ip)
        else:
            location_info = {}
        
        # Mendapatkan waktu lokal berdasarkan Time Zone
        timezone = location_info.get("timezone", "Unknown")
        local_time = "Unknown"
        if timezone != "Unknown":
            local_time = datetime.now(pytz.timezone(timezone)).strftime("%Y-%m-%d %H:%M:%S %Z%z")
        
        # Mendapatkan penyedia hosting
        provider = get_hosting_provider(domain_url)
        
        # Menampilkan hasil
        print(f"Domain: {domain_url}")
        print(f"Real IP Found: {ip}")
        print(f"IP Range: {location_info.get('ip_range', 'Unknown')}")
        print(f"Location: {location_info.get('country', 'Unknown')}, {location_info.get('city', 'Unknown')}, {location_info.get('region', 'Unknown')}, {location_info.get('zip', 'Unknown')}")
        print(f"Time Zone: {timezone}")
        print(f"Local Time: {local_time}")
        print(f"ISP: {location_info.get('isp', 'Unknown')}")
        print(f"Organization: {location_info.get('org', 'Unknown')}")
        print(f"Hosting: {provider}")
        print(f"Database MySQL: {check_mysql_database(domain_url)}")
        print("\n")

if __name__ == "__main__":
    main()