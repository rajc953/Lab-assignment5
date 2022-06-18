""" 5. Write a python program to print a triangular pattern of the alphabet (user input the number of rows).
Example: Input the number of rows = 5, then the pattern should come out as given below.
If the count of the alphabet gets exhausted, repeat the alphabet from A.
A
BC
DEF
GHIJ
KLMNO"""
# Input:
n = int(input('Enter number of rows: '))

a=0
Alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for i in range(1,n+1):
    for j in range (1,i+1):
        print(Alphabet[a%26], end='')
        a+=1
    print()
