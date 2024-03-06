import random
import string

def random_string(length=5, additional_string=''):
    random_part = ''.join(random.choices(string.ascii_letters, k=length))
    combined_string = random_part + additional_string
    combined_list = list(combined_string)
    random.shuffle(combined_list)
    return ''.join(combined_list)
