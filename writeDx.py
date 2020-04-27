#! /usr/bin/python

import re, os, sys
import os.path as path
import time
import fnmatch
import glob
import numpy as np
from numpy import inf
from scipy.ndimage import measurements

def filter_blobs(wat_grid):
    lw, num = measurements.label(wat_grid)
    n=wat_grid
    for i in range(num):
        if len(n[np.where(lw==i)]) <= 100:
            n[np.where(lw==i)] = 0.0
	return n
def normalize(x):
    
    return x

def np2dx(np_file):
	m = np.load(np_file)
	#print(m.shape)
	try:
		if m.shape!=(48,48,48):
			m = np.reshape(m,m.shape[1:-1])
	except:
		print(np_file)
	#m = np.reshape(m,[16,16,16])
	m = normalize(m)
	m = m.clip(min=0)
	m = np.nan_to_num(m)
	#m = np.clip(m,a_min=None,a_max=20)
	#m[np.abs(m) <= 5] = 0
	#print(m[np.where(m>5)])
	#m[np.abs(m) == 0] = 2
	#m[m== -inf] = 14 * 5
	#m= m/50.0
	

	grid = m
	origin = [0,0,0]
	delta = [0.5,0.5,0.5]

	_dxtemplate="""object 1 class gridpositions counts %i %i %i
origin %.3f %.3f %.3f
delta %.5f   0   0
delta 0   %.5f   0
delta 0   0   %.5f
object 2 class gridconnections counts %i %i %i
object 3 class array type double rank 0 items %i data follows
"""

	out_dx = open(np_file.replace('.npy','.dx'), 'w')
	out_dx.write(_dxtemplate%( grid.shape[0],grid.shape[1],grid.shape[2],
							origin[0],origin[1],origin[2],
							delta[0],delta[1],delta[2],
							grid.shape[0],grid.shape[1],grid.shape[2],
							grid.size))

	count=0
	for data in grid.flat:
		if count==3: out_dx.write('\n'); count=0
		out_dx.write('%8.5f\t'%(float(data)))
		count+=1
	out_dx.write('\n')
	out_dx.close()



npys = glob.glob('*.npy')

for arr in npys:
	np2dx(arr)