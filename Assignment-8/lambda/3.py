''''Write a Python program to sort a list of dictionaries using Lambda.Original list of dictionaries : [{'make': 'Nokia', 'model': 216, 'color': 'Black'},
{'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7,'color': 'Blue'}]
Sorting the List of dictionaries : [{'make': 'Nokia', 'model': 216, 'color': 'Black'},{'make': 'Samsung', 'model': 7, 'color': 'Blue'}, {'make': 'Mi Max', 'model': '2','color': 'Gold’}]'''

dict_list = [{'make': 'Nokia', 'model': 216, 'color': 'Black'},{'make': 'Mi Max', 'model': '2', 'color': 'Gold'},
{'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
sorted_dict_list = sorted(dict_list, key=lambda x: x['make'])
print("Sorting the List of dictionaries:", sorted_dict_list)