'''Write a Python program to find the elements of a given list of strings that contain specific substring using lambda.
Original list: ['red', 'black', 'white', 'green', 'orange']
Substring to search: ack Elements of the said list that contain specific substring:['black']
Substring to search: abc Elements of the said list that contain specific substring: []'''
original_list = ['red', 'black', 'white', 'green', 'orange']
substring1 = 'ack'
substring2 = 'abc'
contains_substring = lambda s, sub: sub in s
result1 = list(filter(lambda x: contains_substring(x, substring1), original_list))
result2 = list(filter(lambda x: contains_substring(x, substring2), original_list))
print("Original list:", original_list)
print(f"Elements of the list that contain '{substring1}':", result1)
print(f"Elements of the list that contain '{substring2}':", result2)