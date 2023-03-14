'''18. Write a Python program to check if all dictionaries in a list are empty or not.
Sample list : [{},{},{}]
Return value : True
Sample list : [{1,2},{},{}]
Return value : False'''

list = [{},{},{}]
list2 = [{1:2},{},{}]
print(all(not d for d in list))
print(all(not d for d in list2))
