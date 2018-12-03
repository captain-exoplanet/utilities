# utilities
Various generally useful codes and scripts.

Contents:

  tablecatter.py: a script to read in an arbitrary number of two-column LaTeX-formatted tables (a left-hand column holding parameter names and a right-hand column holding parameter values), and output a new table with a left-hand column holding the parameter names and then one column of parameter values per input file.

  Call as: python tablecatter.py input1.tex input2.tex input3.tex output.tex
  Where input1.tex ... inputn.tex is an arbitrarily long list of input LaTeX tables, and output.tex is the name of the output table that will be created.

  Dependencies: numpy, argparse, sys, readcol.py (https://github.com/keflavich/agpy/blob/master/agpy/readcol.py)

  Known bugs and issues:
  -The parameters in the output file will be sorted in alphabetical order, rather than whatever order was in the input files.
