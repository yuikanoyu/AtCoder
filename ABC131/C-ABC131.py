# only Python 3.4
import fractions

A, B, C, D = map(int, input().split())

A -= 1

Z = ((C * D) // fractions.gcd(C, D))

A_C = A // C
A_D = A // D
A_Z = A // Z

A_num = A - (A_C + A_D - A_Z)

B_C = B // C
B_D = B // D
B_Z = B // Z


B_num = B - (B_C + B_D - B_Z)


print(B_num - A_num)

