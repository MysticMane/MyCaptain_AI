l=[0,1]
n=int(input("Enter the Number of Elements for Fibonacci Series: "))
for i in range(0,n-2):
    x=l[i]+l[i+1]
    l.append(x)

print(l)

""" output
Enter the Number of Elements for Fibonacci Series: 10
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]"""
