#10. Write a Python program to remove a key from a dictionary. 

dic={1:10,2:10,3:20,4:5,7:80}
rem=int(input("enter the key to be deleted: "))
del dic[rem]
print("After deletion: ",dic)
