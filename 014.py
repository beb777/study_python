"""
function
structure
def fun_name():
    statement
"""


def hello():
    print('this is function, you can call me again and again')
    print('have a nice day')


hello()
hello()
hello()
print('__________________________________________________')

number = int(input('inter the number: '))


def summation():
    odd_sum = number ** 2
    print(odd_sum)


summation()
print('_____________________________________________')


print('_____________________________________________')


def n_sum(n):
    pass


def amount(principal, rate, time):
    interest = (principal*rate*time)/100
    return principal + interest


total = amount(100, 6, 22)
print(total)

print('_____________________________________________')

def return_value():
    return 'welcome to python'

print(return_value().title())
