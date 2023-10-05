import numpy as np

def norma (v,p):
    a = v[p]
    num = np.linalg.norm(a)
    return num **2

def sum_prov (v,p):
    suma = 0
    for p in range (len(v)):
        sum1 = suma + norma (v,p)
        suma = sum1
    return suma

def prov (v,p):
    num = norma (v,p)
    den = sum_prov (v,p)
    return num/den

def amplitud (v1,v2):
    v1n = v1 / norma **(1/2)    
    v2n = v2 / norma **(1/2)
    r = np.transpose(np.conjugate(v2n))
    o = np.dot(r*v1n)
    return o
def probabilidad (v1,v2):
    v1n = v1 / norma **(1/2)
    v2n = v2 / norma **(1/2)
    r = np.transpose(np.conjugate(v2n))
    o = np.dot(r*v1n)
    p =np.real(o)
    i = np.imag (o)
    tra2 = norma(p,i)
    return tra2
