#tablecatter is a script to read in an arbitrary number of two-column LaTeX-formatted tables (a left-hand column holding parameter names and a right-hand column holding parameter values), and output a new table with one column of parameter values per input file.
#written by Marshall C. Johnson (github.com/captain-exoplanet)
#call as: python tablecatter.py input1.tex input2.tex input3.tex output.tex
#where input1.tex ... inputn.tex is an arbitrarily long list of input LaTeX tables, and output.tex is the name of the output table that will be created.
#dependencies: numpy, readcol.py

import numpy as np
from readcol import readcol
import argparse
import sys

parser=argparse.ArgumentParser()
parser.add_argument("infiles", type=str, help="names of the input files, the last one is the output file name", nargs='+')
args=parser.parse_args()

inlist=args.infiles



    
nfiles=len(inlist)-1

parsin = [dict() for x in range(nfiles)]

def inreader(infile):
    names, values = readcol(infile, twod=False, fsep='&')
    outstruc = dict(zip(names, values))
    outstruc['index']=names
    outstruc['invals']=values
    return outstruc

for i in range (0,nfiles):
    parsin[i]=inreader(inlist[i])
    if i == 0:
        allkeys=parsin[i]['index']
    else:
        allkeys=np.append(allkeys,parsin[i]['index'])

keys=np.unique(allkeys)
nkeys=len(keys)

f=open(inlist[nfiles],'w')

for i in range (0,nkeys):
    outstr=keys[i]+' & '
    for j in range (0,nfiles):
        if any(keys[i] in s for s in parsin[j]['index']):
            outstr+=parsin[j][keys[i]][:len(parsin[j][keys[i]])-3]
        if j != nfiles-1:
            outstr+=' & '
        
    f.write(outstr+' \\\ \n')


f.close()
