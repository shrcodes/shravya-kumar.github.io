#4.Write a Python script to check if a given key already exists in a dictionary. 
dict={
    0: 10, 1: 20, 2: 30,2:10

}

key=int(input(""))
if key in dict.keys():
    print(key,"is present in dict")
else:
    print(key,"is not present in dict")
    