'''write a program to reverse  a string'''
def reverse_string(a):
    str = ""
    for i in a:
        str = i + str
    return str
string = "Tushar yadavendu"
y = reverse_string(string)
print(y)
