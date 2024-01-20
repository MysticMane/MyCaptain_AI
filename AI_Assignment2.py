s1={1,3,4,5,6,7,8}
s2={2,6}
s3=s1.union(s2)
s4=s1.intersection(s2)
s5=s1.difference(s2)
s6=s1.symmetric_difference(s2)
print("The two sets are ",s1,"and ",s2)
print("The Union of two sets is: ",s3)
print("THe Intersection of two sets is: ",s4)
print("The Difference of two sets is: ",s5)
print("The Symmetric Difference of two sets is: ",s6)


""" Output
The two sets are  {1, 3, 4, 5, 6, 7, 8} and  {2, 6}
The Union of two sets is:  {1, 2, 3, 4, 5, 6, 7, 8}
THe Intersection of two sets is:  {6}
The Difference of two sets is:  {1, 3, 4, 5, 7, 8}
The Symmetric Difference of two sets is:  {1, 2, 3, 4, 5, 7, 8} """
