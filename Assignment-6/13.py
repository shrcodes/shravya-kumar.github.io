#13. Take 10 integers from keyboard using loop and print their average value on the screen.
total=0.0
count=0
for i in range(10):
    integer=int(input(""))
    total+=integer
    count+=1
avg=total/count
print("average= ",avg)