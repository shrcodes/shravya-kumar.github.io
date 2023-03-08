'''10. A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years.
Ask user for their salary and year of service and print the net bonus amount.
'''
salary=int(input("salary= "))
year=int(input("year of service= "))
if year>5:
    salary+=0.05*salary
print(salary)