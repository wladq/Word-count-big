#from bswen.com

import sys

def generate_big_random_letters(filename, size):
    """
    Generate big random letters/alphabets to a file
    :param filename: the filename
    :param size: the size in bytes
    :return: void
    """
    import random
    import string

    chars = ' ab'.join([random.choice(string.ascii_letters) for i in range(size//4)])  # 1

    with open(filename, 'w') as f:
        f.write(chars)
    pass

if __name__ == "__main__":
    generate_big_random_letters(sys.argv[1],int(sys.argv[2]))