#16. Write a Python program to find the highest 3 values in a dictionary.

from collections import Counter

dict = {'A': 67, 'B': 23, 'C': 45,'D': 56, 'E': 12, 'F': 69}

c = Counter(dict)
highest = c.most_common(3)
print(highest)

