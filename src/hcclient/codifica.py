import hashlib

def encrypt(sentence, key):
    # Hash the key
    key = hashlib.sha256(str(key).encode()).hexdigest()
    # Convert the hashed key to an integer
    key = int(key, 16) % 256  # We use modulo 256 to ensure the key is within the ASCII range

    encrypted_sentence = []
    for char in sentence:
        ascii_value = ord(char)
        encrypted_ascii_value = ascii_value + key
        encrypted_sentence.append(encrypted_ascii_value % 256)  # We use modulo 256 to ensure the value is within the ASCII range
    return encrypted_sentence
def decrypt(encrypted_sentence, key):
    # Hash the key
    key = hashlib.sha256(str(key).encode()).hexdigest()
    # Convert the hashed key to an integer
    key = int(key, 16) % 256  # We use modulo 256 to ensure the key is within the ASCII range

    decrypted_sentence = ""
    for encrypted_ascii_value in encrypted_sentence:
        ascii_value = (encrypted_ascii_value - key) % 256
        # Only add the character to the sentence if it's within the printable ASCII range
        if 32 <= ascii_value <= 126:
            decrypted_sentence += chr(ascii_value)
    return decrypted_sentence

# Usage
