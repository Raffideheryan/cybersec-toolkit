import re

def detect_phishing(email_text):
    suspicious_keywords = ["verify", "click", "urgent", "login", "account"]
    email_lower = email_text.lower()
    
    keywords_found = [word for word in suspicious_keywords if word in email_lower]
    url_pattern = r"http[s]?://"
    urls_found = re.search(url_pattern, email_text)
    
    if keywords_found and urls_found:
        print("\n[!] Possible phishing email: suspicious keywords AND link detected.")
    elif keywords_found:
        print("\n[*] Suspicious words found BUT no link detected.")
    else:
        print("\n[+] Email seems safe.")

def main():
    print("Enter/paste the email text (type 'END' on a new line to finish):")
    lines = []
    while True:
        line = input()
        if line.strip().upper() == 'END':
            break
        lines.append(line)
    
    email_text = "\n".join(lines)
    detect_phishing(email_text)

if __name__ == "__main__":
    main()
