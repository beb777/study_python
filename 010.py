print('_______________________________________')
"""
dictionaries 
key- value pair 
{key:value}


"""
student ={1: 'beb',
          2 :'carlos',
          4 :'ali'}
print(student[1])
print(student.keys())
print(student.values())
print(student.get('3')) # getting a value by inputting the key
student[4] = 'bob' # update the value
print(student)

customer = {
    'name': 'alex cool',
    'age': 25,
    'new': True
}
print(customer.items())# display using array
print(customer['age'])
#print(customer['phone'])
print(customer.get('phone'))
print(customer.get('phone', 'defult none'))
print('_______________________________________')