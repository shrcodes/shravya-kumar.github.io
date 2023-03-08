'''12. A student will not be allowed to sit in exam if his/her attendence is less than 75%.
Take following input from user
Number of classes held
Number of classes attended.
And print
percentage of class attended
Is student is allowed to sit in exam or not.
'''

no_of_class=int(input(''))
class_attended=int(input(''))
percentage=(class_attended/no_of_class)*100
print("percentage of class attended= ",'{:.2f}'.format(percentage),"%")
if percentage<75:
    print("student is not allowed to sit in exam ")
else:
    print("student is allowed to sit in exam ")

