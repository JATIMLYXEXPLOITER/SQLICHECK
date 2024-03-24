import os
import requests
from bs4 import BeautifulSoup
import json
from urllib.parse import urlparse

def find_linked_paths(url):
    linked_paths = set()  # Gunakan set untuk menyimpan path unik

    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        for link in soup.find_all('a', href=True):
            href = link['href']
            parsed_href = urlparse(href)
            linked_paths.add(parsed_href.path)

    return linked_paths

def main():
    main_url = input("Masukkan URL utama: ")
    parsed_url = urlparse(main_url)
    domain = urlparse(main_url).netloc.split('.')[1] if len(parsed_url.netloc.split('.')) > 1 else parsed_url.netloc
    linked_paths = find_linked_paths(main_url)

    if linked_paths:
        domain_directory = os.path.join("log", domain)
        os.makedirs(domain_directory, exist_ok=True)  # Membuat direktori domain jika belum ada
        filename = os.path.join(domain_directory, f"{domain}.json")  # Menggunakan nama domain untuk nama file
        with open(filename, 'w') as f:
            json.dump({"path": list(linked_paths)}, f, indent=4)
        print(f"Found path: {len(linked_paths)}")
        print(f"Path telah disimpan dalam file '{filename}'")
    else:
        print("Tidak ada path yang ditautkan.")

if __name__ == "__main__":
    main()