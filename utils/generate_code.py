import random
from django.utils.text import slugify


def generate_code(n=8):
    numbers = 'abcd1234'
    code = ''.join(random.choice(numbers) for x in range(n))
    return code 


print(f'{slugify("web design")}-category-{generate_code()[:4]}')