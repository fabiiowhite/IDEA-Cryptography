def string_to_binary(string):
    return ' '.join(format(ord(c), '08b') for c in string)

def simple_encrypt(message, key):
    # Transform the message and key into a list of character codes
    message_codes = [ord(c) for c in message]
    key_codes = [ord(c) for c in key]

    # Simple "encryption" by adding key character codes to message character codes
    encrypted_codes = [(m + k % 256) for m, k in zip(message_codes, key_codes * (len(message_codes) // len(key_codes) + 1))]

    # Convert codes back to characters
    encrypted_message = ''.join(chr(c % 256) for c in encrypted_codes)

    return encrypted_message

def simple_decrypt(encrypted_message, key):
    # Transform the encrypted message and key into a list of character codes
    encrypted_codes = [ord(c) for c in encrypted_message]
    key_codes = [ord(c) for c in key]

    # Simple "decryption" by subtracting key character codes from encrypted character codes
    decrypted_codes = [(e - k % 256) for e, k in zip(encrypted_codes, key_codes * (len(encrypted_codes) // len(key_codes) + 1))]

    # Convert codes back to characters
    decrypted_message = ''.join(chr(c % 256) for c in decrypted_codes)

    return decrypted_message
