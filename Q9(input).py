""" 9. Write a program to count the number of occurrences of each word in the list(List entered by the user)"""
n = int(input("Number of words: "))
list = []
for i in range(n):
    word = input("Enter the word: ")
    list.append(word)
times = {}
for i in list:
    if i not in times:
        times[i]= 1
    else:
        times[i] +=1
print("The list of words entered by user are: ",list)
print("Number of occurences: ", times)
