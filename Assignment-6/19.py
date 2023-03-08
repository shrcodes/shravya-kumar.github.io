#19. From a list containing ints, strings and floats, make three lists to store them separately

array=[10,'Adam',10.8,40.00,50,'Mary']
integers=[]
floats=[]
strings=[]

for i in array:
    if type(i)==str:
        strings.append(i)
    if type(i)==int:
        integers.append(i)
    if type(i)==float:
        floats.append(i)

print("integers=",integers,"\nfloats=",floats,"\nstrings=",strings)




