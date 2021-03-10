print('***************************************************')
#string
welcome_message = 'welcome to python hub' # single
print(welcome_message)
welcome_message = "welcome to python hub"   # double
print(welcome_message)
welcome_message = "welcome to python's hub"
print(welcome_message)
welcome_message = 'welcome to "python" hub'
print(welcome_message)
welcome_message = '''     welcome 
            to
             python hub  
'''
print(welcome_message)
# methode
print(len(welcome_message))# count the number of character
print(welcome_message.upper())
print(welcome_message.title())
print(welcome_message.find('x'))# its help to find the index the character
print(welcome_message.find('n'))
print(welcome_message.find('N'))
print(welcome_message.replace('hub', 'home'))# replacing the character
print('hub' in welcome_message)# to check the existance -- bolian  form
print('home' in welcome_message)
print('________________________________________________')

# index []
welcome_message ='welcome to python hubs'
print(welcome_message[0])# start index
print(welcome_message[-1])# end index
print(welcome_message[:])# same as print(welcome_message)
print(welcome_message[10:17])# printing python
print('_________________________________________')
# f-string
full_name = 'carol dyle '
age = str(25)
course = 'python'
info = full_name + ' *' + age + '* years old.' + ' study ' + course# string
print(info)
info_2 = f'{full_name} *{age}* years old. study {course}' # f- string
print(info_2)



print('******************************************************')