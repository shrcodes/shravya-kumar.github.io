#16. Take inputs from user to make a list. Again take one input from user and search it in the list and delete that element, if found. Iterate over list using for loop.
lists=[]
n=int(input('Enter the no. of elements: '))
for i in range(n):
    ele=int(input(''))
    lists.append(ele)
find=int(input("Enter the element to be deleted: "))
if find in lists:
    lists.remove(find)
print(lists)


