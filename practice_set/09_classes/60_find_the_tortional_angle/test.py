
import math

A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))
D = list(map(int,input().split()))

# for plane ABC
BA = [a - b for a, b in zip(A, B)]
BC = [a - b for a, b in zip(C, B)]

# for plane BCD
CB = [a - b for a, b in zip(B, C)]
CD = [a - b for a, b in zip(D, C)]

#Find normal vectors to each plane using cross product
# A[a1,a2,a3]   B[b1,b2,b3] 
# AxB = [a2b3-a3b2 , a3b1-a1b3 , a1b2-a2b1]

# n1 = BA x BC
# n2 = CB x CD
n1 = [ BA[1]*BC[2] - BA[2]*BC[1] , BA[2]*BC[0] - BA[0]*BC[2] , BA[0]*BC[1] - BA[1]*BC[0] ]
n2 = [ CB[1]*BC[2] - CB[2]*CD[1] , CB[2]*CD[0] - CB[0]*CD[2] , CB[0]*CD[1] - CB[1]*CD[0] ]

mag_n1 = (n1[0]**2 + n1[1]**2 + n1[2]**2)**0.5
mag_n2 = (n2[0]**2 + n2[1]**2 + n2[2]**2)**0.5

numerator = sum(a*b for a, b in zip(n1, n2))
denominator = mag_n1 * mag_n2

rad_angle = math.acos(numerator/denominator)
deg_angle = math.degrees(rad_angle)

print(f"{deg_angle:.2f}")