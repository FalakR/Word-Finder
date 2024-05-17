"""Personal Project"""
from helper_functions import *
import sys


if __name__ == '__main__':
    try:
        word_to_find = sys.argv[1]
        print(find_word(word_to_find))
    except IndexError:
        print('Please provide an argument in the execution, the word to find!\n'
              'Example: python main.py foo')

