#7. Write a Python program that counts the number of elements within a list that are greater than 30.

elements=[10,20,14,66,100,23,78,1]
count=0
for i in elements:
    if i>30:
        count+=1
print("the no. of elements greater than 30 are= ",count)

