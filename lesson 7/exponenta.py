import math

def exponenta(*args):
    return math.exp(args[0])

def wrapper(*args):
    return args[0](args[1])
