from __future__ import division
import scipy.io.wavfile
import numpy as np
from numpy import abs, sign, array
from collections import Counter
import matplotlib.pyplot as plt
import argparse

__doc__ = "This file preprocess wav data to feed it into the RNN"

DEFAULT_FILENAME = 'data/gen/bad_taste.wav'
ENCODING_VALUES = [2, 4, 8, 16, 32]
NUM_POINTS = 500
START_POS = 0

class preprocess(object):
    def __init__(self, filename=DEFAULT_FILENAME, encoding=16):
    	# TODO : Find a better way to initialize values
    	assert encoding in ENCODING_VALUES, "".format(
    	    "encoding values should be in {}".format(ENCODING_VALUES))
        assert isinstance(filename, basestring), 'wrong filename type {}'.format(
            type(filename))
        self.filename = filename
        self.rate, self.signal = scipy.io.wavfile.read(filename)

    def slice(self, pos, dur):
        self.signal = self.signal[pos:pos+dur]

    def get_signal(self, stype='normalized'):
		if stype == 'normalized':
		    return self.nsignal
		else:
			return self.signal

    def normalize(self, encoding=16, verbose=False):
        # Normalization between -1.0 and 1.0
        self.nsignal = self.signal.astype(np.int64)
        M = max(self.nsignal)
        m = min(self.nsignal)

        self.nsignal = -1.0 + 2.0 * (self.nsignal - float(m)) / float(M - m)
    	if verbose:
    		print(self.nsignal)

    def show_signal(self, signal=None, stype='normalized'):
		if signal == None:
			if stype == 'normalized':
			    signal = self.nsignal
			else:
				signal = self.signal
		plt.figure()
		plt.plot(signal,"-x",alpha=0.5)
		plt.show()

def show_process():
	p = preprocess(DEFAULT_FILENAME)
	print("sample rate")
	print(p.rate)
	print("number of points")
	print(len(p.signal))
	# print('normalizing')
	p.normalize()
	print("normalized signal")
	print(p.nsignal)
	print("sliced signal")
	p.seek(10,520)
	print(len(p.seek(10,520)))

def process_file():
	pass

if __name__ == '__main__':
	args = {}
	parser = argparse.ArgumentParser(
		description = __doc__,
		formatter_class = argparse.RawTextHelpFormatter)
	parser.add_argument('-filename',default=DEFAULT_FILENAME,help="Filename to process",type=str)
	parser.add_argument('-num_points',default=NUM_POINTS,help="Number of points to consider in the signal",type=int)
	parser.add_argument('-start_pos',default=START_POS,help="starting position of the signal",type=int)
	args = parser.parse_args()
	#args = vars(args)
	print(args)

   	#show_process()
