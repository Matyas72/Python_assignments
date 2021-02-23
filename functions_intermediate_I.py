import random


def randInt(min=0, max=100):
    dif = max - min
    return round(random.random() * dif + min)
