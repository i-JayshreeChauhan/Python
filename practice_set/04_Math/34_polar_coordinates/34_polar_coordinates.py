import cmath

z = complex(input())

#converting it to polar coordinates (real + i (imag)) --> (modulas , phase) <<-------this is called polar coodinates
r = abs(z)      #modulus
p = cmath.phase(z)   #phase angle in radians

print(r)
print(p)