import numpy as np
import sys

Z = 0.008 #metallicity
a_max = 1 #--semi-major-axis-max
a_min = 0.001 #--semi-major-axis-min


def new_grid(filename):
    with open('new_'+filename, 'w') as fwrite:
        with open(filename) as grid:
            while line := grid.readline():
                params = line.rstrip().split('--')
                fwrite.write('--{}--{}--metallicity {} --semi-major-axis-max {} --semi-major-axis-min {}\n'.format(params[1], params[2], Z, a_max, a_min))
    return

if __name__ == "__main__":
    new_grid(sys.argv[1:][0])