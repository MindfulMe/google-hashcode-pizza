import numpy as np
import math
import sys


def read_file(filename):
    '''
    Read the file.
    Return the pizza as a binary matrix: tomatoes = 1, mushrooms = 0 + returns the minimum ingredients required for each slice,
    and the maximum cells allowed for each slice // 'tis not fully mine description
    '''
    
    with open(filename, 'r') as f:
        line = f.readline()
        rows, cols, min_ings, max_cells = [int(n) for n in line.split()] '''get first row '''

def main():
    '''
    Main function
    '''


if __name__ == '__main__':
    main()