def identify_hash(hash_string):
    hash_len = len(hash_string)
    if hash_len == 32:
        return "MD5"
    elif hash_len == 40:
        return "SHA1"
    elif hash_len == 64:
        return "SHA256"
    elif hash_len == 128:
        return "SHA512"
    else:
        return "Unknown"

hash_input = input("Enter hash: ")
print(f"Possible hash type: {identify_hash(hash_input)}")

