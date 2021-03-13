import numpy as np
import math
from functools import reduce


def generate_bit_block(num: int = 256):
    np.set_printoptions(linewidth=2 * (num ** 0.5 + 1))
    return np.random.randint(0, 2, num)

def print_bit_block(arr):
    arr = list(map(str, arr))
    char = int(len(arr) ** 0.5)
    print(f'\n'.join([''.join(arr[i: i+char]) for i in range(0, len(arr), char)]))

def parity_bits(block_size):
    bits = int(math.log(block_size, 2))
    print(f'No. of parity bits: {bits}\nNo of data bits: {block_size - bits}')

def hamming_check(bits):
    ls = reduce(lambda x, y: x ^ y, [i for i, bit in enumerate(bits) if bit])
    return ls


bits = eval(input('Enter no. of bits: '))
if bits <= 2 ** 14:
    parity_bits(bits)
    bits = generate_bit_block(bits)
    print_bit_block(bits)
    print('This block of bits may or may not have any errors')
    print(hamming_check(bits))
else:
    print('num too large')
