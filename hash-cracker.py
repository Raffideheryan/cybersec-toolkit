import hashlib

def get_hash_function(algorithm):
    """Return the corresponding hash function from hashlib."""
    try:
        return getattr(hashlib, algorithm.lower())
    except AttributeError:
        print(f"[!] Error: Unsupported hash type '{algorithm}'")
        return None

def crack_hash(target_hash, hash_func, wordlist):
    """Try to crack the hash using the given hash function and wordlist."""
    for word in wordlist:
        word = word.strip()
        hashed_word = hash_func(word.encode()).hexdigest()
        if hashed_word == target_hash:
            return word
    return None

def main():
    print("=== Hash Cracker ===")
    
    # Get user inputs
    target_hash = input("[*] Enter the hash to crack: ").strip()
    algorithm = input("[*] Enter the hash type (md5, sha1, sha256, sha512, etc.): ").strip()
    wordlist_path = input("[*] Enter path to wordlist file: ").strip()

    hash_func = get_hash_function(algorithm)
    if not hash_func:
        return

    try:
        with open(wordlist_path, 'r', encoding='utf-8', errors='ignore') as f:
            wordlist = f.readlines()
    except FileNotFoundError:
        print(f"[!] Error: File '{wordlist_path}' not found.")
        return

    print("[*] Cracking hash...")
    result = crack_hash(target_hash, hash_func, wordlist)

    if result:
        print(f"[+] Hash cracked! Plaintext: {result}")
    else:
        print("[-] Hash not found in wordlist.")

if __name__ == "__main__":
    main()
