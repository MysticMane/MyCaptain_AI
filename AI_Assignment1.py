l1=[]
n=int(input("Enter the size of the list: "))
for i in range(0,n):
    x=int(input("Enter the Number: "))
    l1.append(x)
for i in l1:
    if i>0:
        continue
    else:
        l1.remove(i)
        
print("The positive numbers are: ",l1)


""" Output
Enter the size of the list: 3
Enter the Number: 96
Enter the Number: -8
Enter the Number: 86
The positive numbers are:  [96, 86]"""
