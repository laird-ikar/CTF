#!python3

from itertools import combinations_with_replacement
import numpy as np
from numpy import matrix
from numpy import linalg

alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
cyphered=""
word=""
n=2

def modMatInv(A,p):       # Finds the inverse of matrix A mod p
  n=len(A)
  A=matrix(A)
  adj=np.zeros(shape=(n,n))
  for i in range(0,n):
    for j in range(0,n):
      adj[i][j]=((-1)**(i+j)*int(round(linalg.det(minor(A,j,i)))))%p
  return (modInv(int(round(linalg.det(A))),p)*adj)%p

def modInv(a,p):          # Finds the inverse of a mod p, if it exists
  for i in range(1,p):
    if (i*a)%p==1:
      return i
  raise ValueError(str(a)+" has no inverse mod "+str(p))

def minor(A,i,j):    # Return matrix A with the ith row and jth column deleted
  A=np.array(A)
  minor=np.zeros(shape=(len(A)-1,len(A)-1))
  p=0
  for s in range(0,len(minor)):
    if p==i:
      p=p+1
    q=0
    for t in range(0,len(minor)):
      if q==j:
        q=q+1
      minor[s][t]=A[p][q]
      q=q+1
    p=p+1
  return minor

def strToVec(str, n):
    if len(str) % n != 0:
        raise ValueError
    vec = []
    for i in range(len(str) // n):
        subvec = []
        for j in range(n):
            subvec.append(alphabet.index(str[i * n + j]))
        vec.append(subvec)
    return vec

vecArr = strToVec(cyphered, n)

x = np.empty((n,n), dtype=int)

for comb in combinations_with_replacement(range(len(alphabet)),n**2):
    x.flat[:] = comb
    try:
        x = modMatInv(x, len(alphabet))
        str = ""
        for vec in vecArr:
            s = np.matmul(x, vec)
            str += alphabet[int(s[0] % len(alphabet))]
            str += alphabet[int(s[1] % len(alphabet))]
        if (word in str):
            print(str)
    except(ValueError):
        continue
