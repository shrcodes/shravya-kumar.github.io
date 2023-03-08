'''17. Using range(1,101), make three list, 
one containing all even numbers
one containing all odd numbers 
One containing only prime numbers..
'''
even=[]
odd=[]
prime=[]

for i in range(1,101):
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
    num=2
    flag=0
    while i>num:
        if(i%num==0):
            flag=1
            break
        num+=1
    if flag==0 and i>1:
        prime.append(i)
    
    print("odd numbers= ",odd,"\neven numbers= ",even,"\nprime numbers= ",prime)