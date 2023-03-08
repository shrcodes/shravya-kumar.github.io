#5. Write a Python program to calculate the sum and average of n integer numbers (input from the user). Input 0 to finish
sum=0.0
count=0
integer=1
while (integer!=0):
    integer=int(input(""))
    sum+=integer
    count+=1
avg=sum/(count-1)
print("sum= ",sum,"average= ",avg)

