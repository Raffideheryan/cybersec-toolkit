import requests

url = "https://google.com/"
wordlist = ["admin", "login", "test", "dashboard"]

for word in wordlist:
    full_url = url + word + "/"
    r = requests.get(full_url)
    if r.status_code == 200:
        print(f"[+] Found directory: {full_url}")

