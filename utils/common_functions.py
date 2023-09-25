import random
import string


def generate_valid_email(chars=string.ascii_letters + string.digits, length=10) -> str:
    return f'{generate_string(chars, length)}@mail.com'


def generate_valid_name(chars=string.ascii_letters, length=5) -> str:
    return f'{generate_string(chars, length)} {generate_string(chars, length)}'


def generate_string(chars, length):
    return "".join(random.choice(chars) for _ in range(length))
