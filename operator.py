import math
from math import *
import numpy 
x = int(input('enter the first number '))
y = int(input('enter the second number '))
x += 1
print(x)
x *=2
print(x)
x = x + 3
print (x)
print('adition: ', x+y)
print('subtraction ', x-y)
print('multiplication', x*y)
print('division', x/y)
print('exponet',x**2)
print('multiply by two', x*2)
print('intger division', x//y)
print('module',x%y)
print('the square root of x  and y are  ',x**0.5 , 'and ', y**0.5)
print(x+y*(y**3+7%2-x))
print('minimum value', min(x,y))
print('maximum value is', max(x,y))
print('x the power of y is', pow(x,y))#x^y , x the power of y
print("absolut value of x is", abs(x))#absolute function
"""
Mathematcal operation using list

    """
whole_number = [i for i in range(31)]
natural_number = list(range(1,31))
print(whole_number)
print(sum(natural_number))
#print(numpy.prod(natural_number))
print(math.prod(natural_number))
print(natural_number)
print(sum(whole_number))
print(x<y)
print(x==y)
print(y>y)
print(x!=y)
y=-y
print(y)

