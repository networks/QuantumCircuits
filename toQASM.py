'''
Created on Oct 19, 2013

@author: Sireesh
'''

import cmath    
from numpy import matrix
import numpy
import scipy.linalg
import sys
#sys.stdout = open('test.qasm', 'w')

class matrix:
    def __init__(self, size,elements,cbits):
        self.size = size
        self.elements = elements
        self.cbits = cbits
    
def toSingleQubit(A,B,C,D):
    print '\tdef    A,0,\'\m{' + str(A.elements[0]) + ' & ' + str(A.elements[1]) + ' \cr ' + str(A.elements[2]) + ' & ' + str(A.elements[3]) + '}\''
    print '\tdef    B,0,\'\m{' + str(B.elements[0]) + ' & ' + str(B.elements[1]) + ' \cr ' + str(B.elements[2]) + ' & ' + str(B.elements[3]) + '}\''
    print '\tdef    C,0,\'\m{' + str(C.elements[0]) + ' & ' + str(C.elements[1]) + ' \cr ' + str(C.elements[2]) + ' & ' + str(C.elements[3]) + '}\''
    print '\tdef    D,0,\'\m{' + str(D.elements[0]) + ' & ' + str(D.elements[1]) + ' \cr ' + str(D.elements[2]) + ' & ' + str(D.elements[3]) + '}\''
    print '\tqubit    q0'
    print '\tqubit    q1'
    print '\tC    q1'
    print '\tcnot    q0, q1'
    print '\tB    q1'
    print '\tcnot    q0, q1'
    print '\tA    q1'
    print '\tD    q0'

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
    for i in range(matrix.cbits+1):
        print '\tqubit    q' + str(i)
    print '\tc-V    q' + str(matrix.cbits-1) + ',q' + str(matrix.cbits)
    string = ""
    for i in range(matrix.cbits-1):
        string = string + 'q' + str(i) + ','
    print '\tc-X1    ' + string + 'q' + str(matrix.cbits-1)
    print '\tc-Vd    q' + str(matrix.cbits-1) + ',q' + str(matrix.cbits)
    print '\tc-X2    ' + string + 'q' + str(matrix.cbits-1)
    print '\tc-V2    ' + string + 'q' + str(matrix.cbits)


def decomposeRecursion(matrix):
    V = sqrt(matrix)
    Vd = numpy.asmatrix(V).getH()
    Vd = numpy.asarray(Vd)
    
if __name__ == '__main__':
    el_A = [1,2,3+8j,4]
    A = matrix(2,el_A,5)
    el_B = [1,2+4j,3,4]
    B = matrix(2,el_B,0)
    el_C = [1,2,3+3j,4+9j]
    C = matrix(2,el_C,0)
    el_D = [1,0,0,2+5j]
    D = matrix(2,el_D,0)
    breakOneLevelDown(A)

