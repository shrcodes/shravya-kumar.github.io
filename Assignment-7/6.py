#6. Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x). 

dic={}
ele=int(input("enter the no' of elements to be added: "))
for i in range(1,ele+1):
    key=i
    value=i*i
    dic[key]=value
print(dic)