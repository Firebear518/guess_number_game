import random

def get_random(start, end):
    if start > end:
        start, end = end, start
    return random.randint(start, end)
