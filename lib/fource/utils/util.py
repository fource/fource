import string
import random


def random_string(size=10, chars=string.letters):
    return ''.join(random.choice(chars) for _ in range(size))


def random_number(size=10, chars=string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def random_identifier(size=10, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def get_random_dict():
    return {
        'fource_random_string': random_string(),
        'fource_random_number': random_number(),
        'fource_random_identifier': random_identifier(),
    }
