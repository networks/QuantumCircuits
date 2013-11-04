#Quantum circuit decomposition
"""Created by : Infinity"""

from c_Udecomp import*
import scipy.linalg as ln
from toQASM import*
from read_inputs import*
import numpy as np

def QCircDecomp(gates,interim):

	Decomp = []
	X = [0.0+0.0j,1.0+0.0j,1.0+0.0j,0.0+0.0j]
	
	while(len(gates) != 0):
		if (gates[-1].qsize() == 1):
			if (gates[-1].csize() == 0):
				Decomp.append(gates[-1])
				gates.pop()
			elif (gates[-1].csize() == 1):
				if (gates[-1].elements == X):
					Decomp.append(gates[-1])
					gates.pop()
				else:
					alpha,A,B,C = c_Udecomp(gates[-1].elements)
					C1 = matrix(gates[-1].qbits,C,[])
					X1 = matrix(gates[-1].qbits,X,gates[-1].cbits)
					B1 = matrix(gates[-1].qbits,B,[])
					A1 = matrix(gates[-1].qbits,A,[])
					alpha1 = matrix(gates[-1].cbits,alpha,[])
					Decomp = Decomp + [alpha1,A1,X1,B1,X1,C1]
					gates.pop()
			else:
				V = sqrt(gates[-1].elements)
				Vdager = matrix(gates[-1].qbits,numpy.asarray(V.getH()),gates[-1].cbits[-1])
				V1 = matrix(gates[-1].qbits,np.asarray(V),gates[-1].cbits[-1])
				X1 = matrix(gates[-1].cbits[-1],X,gates[-1].cbits[:-1])
				V2 = matrix(gates[-1].qbits,np.asarray(V),gates[-1].cbits[:-1])
				gates[-1] = V1
				gates = gates + [X1,Vdager,X1,V2]
		else:
				do_error("Error: Unidentified gate")
		if (interim == 1):
			print_cir(gates,Decomp)
	
	print_cir(gates,Decomp)

def print_cir(gates,Decomp):
	global j
	for i in gates:
		print_matrix(i,j)
		j = j+1
	for j in range(len(Decomp)):
		print_matrix(Decomp[-1-j],j)
		j = j+1		
				
def sqrt(Umatrix):
	return ln.sqrtm(np.array(Umatrix).reshape(2,2))

if __name__ == '__main__':
	global j
	j = 0
	gates = read_inputs()
	print gates
	for i in range(2):
		print '\tqubit    q' + str(i)
	QCircDecomp(gates,0)
