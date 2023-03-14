#13. Write a Python program to remove duplicates from Dictionary.

dic={1:10,2:2,3:2,4:3}
dic2=[]
res={}
for key,val in dic.items():
    if val not in dic2:
        dic2.append(val)
        res[key]=val
print("The dictionary after removing the duplicates is:",res)