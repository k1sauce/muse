
'''
python barachant300csv_to_numpy --muse_data_file=sample.csv --save_file=annotated_muse_sample_data.npy
'''

import ipdb
import numpy
from argparse import ArgumentParser




if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--muse_data_file', required=True)
    parser.add_argument('--save_file', required=True)
    args = parser.parse_args()



    muse_data = numpy.loadtxt(args.muse_data_file, skiprows=1, delimiter=",")
    muse_data = muse_data[:, 1:7]
    muse_data[:,5] = muse_data[:,5] - 1
    numpy.save(args.save_file, muse_data)
