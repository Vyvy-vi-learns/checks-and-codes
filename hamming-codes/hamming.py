import numpy as np
from functools import reduce


def generate_bit_block(num: int = 256):
    np.set_printoptions(linewidth=2 * (num ** 0.5 + 1))
    return np.random.randint(0, 2, num)

def print_bit_block(arr):
    arr = list(map(str, arr))
    char = int(len(arr) ** 0.5)
    print(f'\n'.join([''.join(arr[i: i+char]) for i in range(0, len(arr), char)]))


if len(bits) <= 10 ** 6:
    bits = generate_bit_block(eval(input('Enter no. of bits: ')))
    print_bit_block(bits)
else:
    print('num too large')
