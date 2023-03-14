#1.Write a Python script to sort (ascending and descending) a dictionary by value.
elements={'a':9,'d':2,'b':33,'c':1 }
asc=(sorted(elements))
desc=sorted(elements,reverse=True)
print("ascending order: ",asc,"\ndescending order: ",desc)
