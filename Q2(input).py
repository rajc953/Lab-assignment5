''' 2. Python Program to Print all Numbers in a Range Divisible by a Given Number. (user inputs the range
and the number)'''
start = int(input("enter the starting point of the range: "))
end = int(input("enter the end point of the range: "))
div = int(input("enter the dividing no, : "))
for i in range(start,end+1):
    if i % div == 0:
        print(i,end = " ")
