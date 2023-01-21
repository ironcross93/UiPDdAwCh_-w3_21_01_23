
def print_hi(name):

    print(f'Hi, {name}')



if __name__ == '__main__':
    print_hi('PyCharm')


import logging

def get_logs(level, format):
    logging.basicConfig(level=level, format=format)
    return logging

logger = get_logs(logging.DEBUG, "%(asctime)s %(levelname)s %(message)s")
logger.debug("This is a debug message.")


import base64

def encrypt_base64(text):
    encoded_text = base64.b64encode(text.encode())
    return encoded_text.decode()

def decrypt_base64(encoded_text):
    decoded_text = base64.b64decode(encoded_text.encode()).decode()
    return decoded_text
text = "Hello World"
encoded_text = encrypt_base64(text)
print(encoded_text)
decoded_text = decrypt_base64(encoded_text)
print(decoded_text)

import random
import string


def generate_password():

    characters = string.ascii_letters + string.digits + string.punctuation


    password = random.sample(characters, 8)


    while not (any(c.isupper() for c in password) and any(c.islower() for c in password) and any(
            c.isdigit() for c in password) and any(c in string.punctuation for c in password)):
        password = random.sample(characters, 8)

    return ''.join(password)


password = generate_password()
print(password)
