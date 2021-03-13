#input form user
name = input('your name, please?\n')
print('hello ' +  name + ' welcome  to python hub')
email = """hello {}, 
This is our first mail.
nice to meet you.
how are you?
"""
print(email.format(name))