#18. From the two list obtained in previous question, make new lists, containing only numbers which are divisible by 4, 6, 8, 10, 3, 5, 7 and 9 in separate lists.
even=[]
odd=[]
three=[]
five=[]
seven=[]
four=[]
six=[]
eight=[]
nine=[]
ten=[]

for i in range(1,101):
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
all=odd+even
for i in all :
    if i%3==0  :
        three.append(i)
    if i%4==0  :
        four.append(i)
    if i%5==0  :
        five.append(i)
    if i%6==0  :
        six.append(i)
    if i%7==0  :
        seven.append(i)
    if i%8==0  :
        eight.append(i)
    if i%9==0  :
        nine.append(i)
print("divisible by\n3=",three,'\n4=',four,'\n5=',five,'\n6=',six,'\n7=',seven,'\n8=',eight,'\n9=',nine)
        
