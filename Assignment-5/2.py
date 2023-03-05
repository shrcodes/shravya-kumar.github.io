#Program to count the number of characters (character frequency) in a string. 

string = 'google.com'
chars=set(string)
counts=dict()
for i in chars:
    count=0
    for j in string:
        if i==j:
            count+=1
    counts[i]=count
print(counts)


