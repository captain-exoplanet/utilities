# utilities
Various generally useful codes and scripts.

## Contents:


  ### parsetextable.py
  
  A function to read in a LaTeX-formatted table and return a numpy array containing the values and uncertainties for specified parameter columns.
  
  Inputs:
  - tablein: a two-dimensional string array containing the table to be parsed.
  - ecolumns: an array containing the indices of the N columns which are to be returned. Each of these columns should contain a value and associated uncertainty, which may be asymmetric.
  
  Returns:
  - temparray: an array with 3N columns, where each set of three columns contain the value, positive uncertainty, and negative uncertainty, respectively, from each of the N specified columns in the input table.
  
  I would typically call this code as:
  ```
  from parsetextable import parsetextable
  from readcol import readcol
  tablein = readcol('example.tex',twod=True,fsep='&')
  ecolumns = [1, 2, 3, 5]
  tableout = parsetextable(tablein, ecolumns)
  ```
  
  The code assumes a LaTeX-formatted table with values and their uncertainties in the same column, for example:
  ```
  Parameter name & $1.0 \pm 0.5$ & $1.0_{-0.3}^{+0.4}$ \\
  ```
  Would be returned as:
  ```
  np.array([1.0, 0.5, 0.5, 1.0, 0.4, 0.3])
  ```
  Uncertainties must be specified as in this example in order for the code to properly parse the table.
  
  Dependencies: numpy. I typically use readcol.py (https://github.com/keflavich/agpy/blob/master/agpy/readcol.py) to read in table data, but any method to read an ascii LaTeX table into a string array will work.
 

  ### tablecatter.py 
  
  A script to read in an arbitrary number of two-column LaTeX-formatted tables (a left-hand column holding parameter names and a right-hand column holding parameter values), and output a new table with a left-hand column holding the parameter names and then one column of parameter values per input file.

  Call as: 
  ```
  python tablecatter.py input1.tex input2.tex input3.tex output.tex
  ```
  Where input1.tex ... inputn.tex is an arbitrarily long list of input LaTeX tables, and output.tex is the name of the output table that will be created.

  Dependencies: numpy, argparse, sys, readcol.py (https://github.com/keflavich/agpy/blob/master/agpy/readcol.py)

  Known bugs and issues:
  -The parameters in the output file will be sorted in alphabetical order, rather than whatever order was in the input files.
