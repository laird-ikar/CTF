import gmpy

e = 

n1 = 
n2 = 
n3 = 

c1 = 
c2 = 
c3 = 

N = n1*n2*n3
N1 = N/n1
N2 = N/n2
N3 = N/n3

u1 = gmpy.invert(N1, n1)
u2 = gmpy.invert(N2, n2)
u3 = gmpy.invert(N3, n3)

M = (c1*u1*N1 + c2*u2*N2 + c3*u3*N3) % N

m = gmpy.root(M,e)[0]

print hex(m)[2:].rstrip("L").decode("hex")
