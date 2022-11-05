#!/Library/Frameworks/Python.framework/Versions/3.10/bin/python3
import gmpy2 as gmpy

e =  

n1 =
n2 = 
n3 = 

c1 = 
c2 = 
c3 = 

N = n1*n2*n3
N1 = n2*n3
N2 = n1*n3
N3 = n1*n2

u1 = gmpy.invert(N1, n1)
u2 = gmpy.invert(N2, n2)
u3 = gmpy.invert(N3, n3)

M = (c1*u1*N1 + c2*u2*N2 + c3*u3*N3) % N

m = gmpy.iroot(M,e)[0]


print (bytes.fromhex(hex(m)[2:].rstrip("L")).decode("ascii"))
