# print("how old are you?")
# age = input()
# print("how tall are you?")
# height = input()
import math
import random

#print(math.pi)
#print(math.sqrt(85))
#
# print(random.random())
# print(random.choice([1, 2, 3, 4]))
#
# #print(float(3.1415 * 2))
#
# print("spam" * 8)

S = 'spam'
#S[0] = 'z'
S = 'z' + S[1:]
print(S)

S = 'shrubbery'
L = list(S)
print(L)
L[1] = 'c'
print(''.join(L))

B = bytearray(b'spam')
B.extend(b'eggs')
print(B)
print(B.decode())
