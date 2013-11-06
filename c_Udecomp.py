#c-U decompostion to single qubit gates
""" Created by : Infinity """

import cmath
import math as m
import numpy as np
import sys

tolerance = 10**(-5)
class matrix:
	def __init__(self,qbits,elements,cbits):
		self.qbits = qbits
		self.elements = np.asarray(elements)
		self.cbits = cbits
	def qsize(self):
		return len(self.qbits)
	def csize(self):
		return len(self.csize)
		

def do_error(msg):
	sys.stderr.write('ERROR:' +msg+ "\n")
	sys.exit(-1)
def c_Udecomp(Umatrix):
	if (Umatrix[0] == 0.0):
		if(Umatrix[3] != 0.0):
			do_error("Error0: Detected Unitary error")
		gamma = m.pi
		beta = 0.0
		U_1 = cmath.polar(Umatrix[1])
		U_2 = cmath.polar(Umatrix[2])
		if (U_1[0] != 1 or U_2[0] != 1):
			do_error("Error01: Detected unitary error")
		alpha = (U_1[1] + U_2[1] - m.pi)/2.0
		delta = 2.0*(alpha - U_2[1])
	elif (Umatrix[1] == 0.0):
		if (Umatrix[2] != 0.0):
			do_error("Error0: Detected Unitary error")
		gamma = 0.0
		beta = 0.0
		U_0 = cmath.polar(Umatrix[0])
		U_3 = cmath.polar(Umatrix[3])
		if (U_0[0] != 1 or U_3[0] != 1):
			do_error("Error02: Detected unitary error")
		alpha = (U_0[1] + U_3[1])/2.0
		delta = (U_3[1] - U_0[1])
		
	else:
		U0_2 = Umatrix[2]/Umatrix[0]
		U0_2pol = cmath.polar(U0_2)
		gamma = 2*m.atan(U0_2pol[0])
		beta = U0_2pol[1]
		U1_3 = Umatrix[1]/Umatrix[3]
		#print "tol1 ",((m.sin(beta)*U0_2pol[1]) - U1_3.imag)
		#print U0_2pol[1]
		#print U1_3.imag
		if ((((-m.cos(beta)*U0_2pol[0]) - U1_3.real) > tolerance) or (((m.sin(beta)*U0_2pol[0]) - U1_3.imag) > tolerance)):
			#print Umatrix
			#print matrixmult(Umatrix.reshape(2,2),Umatrix.reshape(2,2))
			do_error("Error1: Detected unitary error")
		U_0 = cmath.polar(Umatrix[0]/m.cos(gamma/2.0))
		if (U_0[0] - 1.0 > tolerance):
			do_error("Error2: Detected unitary error")
		U_0p = U_0[1]
		U_3 = cmath.polar(Umatrix[3]/m.cos(gamma/2.0))
		if (U_3[0] - 1.0 > tolerance):
			do_error("Error5: Detected unitary error")
		U_3p = U_3[1]
		U_1 = cmath.polar(Umatrix[1]/m.sin(gamma/2.0))
		if (U_1[0] - 1.0 > tolerance):
			do_error("Error3: Detected unitary error")
		U_1p = U_1[1]
		U_2 = cmath.polar(Umatrix[2]/m.sin(gamma/2.0))
		if (U_1[0] - 1.0 > tolerance):
			do_error("Error4: Detected unitary error")
		U_2p = U_2[1]
		#print U_0p, U_1p,m.pi,beta
		alpha = (U_0p + U_1p - m.pi + beta)/2.0
		delta = (2.0*alpha - beta - 2.0*U_0p)
	RzA = Rz(beta)
	RzB = Rz(-(delta+beta)/2.0)
	C = Rz((delta-beta)/2.0)
	A = [RzA[0]*(m.cos(gamma/4.0)),-RzA[0]*(m.sin(gamma/4.0)),RzA[3]*m.sin(gamma/4.0),RzA[3]*m.cos(gamma/4.0)]
	B = [RzB[0]*m.cos(gamma/4.0), RzB[3]*m.sin(gamma/4.0), -RzB[0]*m.sin(gamma/4.0), RzB[3]*m.cos(gamma/4.0)]
	#print alpha,beta,gamma,delta
	#self_check1(Umatrix,alpha,beta,gamma,delta)
	alpha1 = complex(m.cos(alpha),m.sin(alpha))
	alpha1 = [1.0+0.0j,0.0+0.0j,0.0+0.0j,alpha]
	return (alpha1,A,B,C)

def Rz(beta):
	Rz1 = complex(m.cos(beta/2.0), -m.sin(beta/2.0))
	Rz2 = complex(m.cos(beta/2.0), m.sin(beta/2.0))
	return [Rz1,0.0+0.0j,0.0+0.0j,Rz2]

def Ry(beta):
	return (m.cos(beta/2.0),-m.sin(beta/2.0),m.sin(beta/2),m.cos(beta/2))

def self_check1(Umatrix,alpha,beta,gamma,delta):
	Rzbeta = Rz(beta)
	Rygamma = Ry(gamma)
	Rzdelta = Rz(delta)
	Rzbeta = np.array(Rzbeta).reshape(2,2)
	Rygamma = np.array(Rygamma).reshape(2,2)
	Rzdelta = np.array(Rzdelta).reshape(2,2)
	M1 = matrixmult(Rzbeta,Rygamma)
	M2 = matrixmult(M1,Rzdelta)
	M3 = complex(m.cos(alpha),m.sin(alpha))*M2
	print Umatrix
	print M3

def self_check(Umatrix,alpha,A,B,C):
	X = [0.0+0.0j,1.0+0.0j,1.0+0.0j,0.0+0.0j]
	A = np.array(A)
	B = np.array(B)
	C = np.array(C)
	X = np.array(X)
	A = A.reshape(2,2)
	B = B.reshape(2,2)
	C = C.reshape(2,2)
	print alpha
	print A
	print B
	print C
	X = X.reshape(2,2)
	print X
	
	M1 = matrixmult(X,C)
	M2 = matrixmult(B,M1)
	M3 = matrixmult(X,M2)
	M4 = matrixmult(A,M3)
	M5 = complex(m.cos(alpha),m.sin(alpha))*M4
	print Umatrix
	print M5

def matrixmult(m1,m2):
	M = [0.0+0.0j,0.0+0.0j,0.0+0.0j,0.0+0.0j]
	M = np.array(M)
	M = M.reshape(2,2)
	for i in range(2):   
		for j in range(2): 
			for k in range(2): 
				M[i][j] += m1[i][k]*m2[k][j]
	return M

