A, B, C, D = map(int, input().split())

A -= 1

A_C = A // C
A_D = A // D
A_Z = A // (C * D)

A_num = A -( A_C + A_D - A_Z )

B_C = B // C
B_D = B // D
B_Z = B // (C * D)


B_num = B - ( B_C + B_D - B_Z )


print(B_num - A_num)

