'''
Created on Oct 19, 2013

@author: Sireesh
'''

import cmath    
from numpy import matrix
import numpy
import scipy.linalg
import sys
from c_Udecomp import *
#sys.stdout = open('test.qasm', 'w')

class matrix:
    def __init__(self, qbits,elements,cbits):
        self.qbits = qbits 
        self.elements = elements
        self.cbits = cbits
    def qsize(self):
        return len(self.qbits)
    def csize(self):
        return len(self.cbits)        
    
def print_matrix(matrix,j):
    print '\tdef    A' + str(j) + ',' + str(matrix.csize()) + ',\'\m{' + str(matrix.elements[0]) + ' & ' + str(matrix.elements[1]) + ' \cr ' + str(matrix.elements[2]) + ' & ' + str(matrix.elements[3]) + '}\''
    string = ""
    for i in matrix.cbits:
        string = string + 'q' + str(i) + ','    
    print '\tA' + str(j) + '\t' + string + 'q' + str(matrix.qbits[0])


def sqrt(unitary):
    return scipy.linalg.sqrtm(numpy.array(unitary.elements).reshape(2,2))

def breakOneLevelDown(matrix):
    V = sqrt(matrix)
    Vd = numpy.asmatrix(V).getH()
    Vd = numpy.asarray(Vd)
    print '\tdef    c-V,1,\'\m{' + str(V[0][0]) + ' & ' + str(V[0][1]) + ' \cr ' + str(V[1][0]) + ' & ' + str(V[1][1]) + '}\''
    print '\tdef    c-X1,' + str(matrix.cbits-1) + ',\'X\''
    print '\tdef    c-Vd,1,\'\m{' + str(Vd[0][0]) + ' & ' + str(Vd[0][1]) + ' \cr ' + str(Vd[1][0]) + ' & ' + str(Vd[1][1]) + '}\''
    print '\tdef    c-X2,' + str(matrix.cbits-1) + ',\'X\''
    print '\tdef    c-V2,' + str(matrix.cbits-1) + ',\'\m{' + str(V[0][0]) + ' & ' + str(V[0][1]) + ' \cr ' + str(V[1][0]) + ' & ' + str(V[1][1]) + '}\''
#    for i in range(matrix.cbits+1):
#        print '\tqubit    q' + str(i)
    print '\tc-V    q' + str(matrix.cbits-1) + ',q' + str(matrix.cbits)
    string = ""
    for i in range(matrix.cbits-1):
        string = string + 'q' + str(i) + ','
    print '\tc-X1    ' + string + 'q' + str(matrix.cbits-1)
    print '\tc-Vd    q' + str(matrix.cbits-1) + ',q' + str(matrix.cbits)
    print '\tc-X2    ' + string + 'q' + str(matrix.cbits-1)
    print '\tc-V2    ' + string + 'q' + str(matrix.cbits)
