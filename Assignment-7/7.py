#7. Write a Python script to merge two Python dictionaries.
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={**dic1,**dic2}
print(dic3)