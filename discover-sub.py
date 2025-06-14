import requests

domain = "google.com"
subdomains = ["www", "mail", "ftp", "test"]

for sub in subdomains:
    url = f"https://{sub}.{domain}"
    try:
        r = requests.get(url, timeout=1)
        print(f"[+] Found subdomain: {url}")
    except requests.ConnectionError:
        pass

