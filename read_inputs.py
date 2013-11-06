'''
Created on 25-Oct-2013

@author: sireesh
'''
import sys
from toQASM import*

def read_inputs():
    list = []
    f = open(sys.argv[1], 'r')
    for line in f:
        ip = []
        line = line.strip()
        l = line.split(',')
        k = 0
        for i in l:
            m = []
            for j in i.split(' '):
                if(k==1):
                    m.append(complex(j))
                else:
                    m.append(int(j))    
            k = k+1
            ip.append(m)
        m = matrix(ip[0],ip[1],ip[2])              
        list.append(m)
    return list
