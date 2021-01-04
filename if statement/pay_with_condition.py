"""
 3.1 Write a program to prompt the user for hours and rate per hour using input to compute gross pay. 
 Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours. 
 Use 45 hours and a rate of 10.50 per hour to test the program 
 (the pay should be 498.75). You should use input to read a string and float() to convert the string to a number. 
  
"""
hours = float(input('enter the hours: '))
over_time= hours-40
rate = float(input('enter your rate: '))
if hours <= 40: 
    pay = hours*rate
    print(pay)
else:
    total_pay = 40*rate + (over_time*rate*1.5) 
    print(total_pay)