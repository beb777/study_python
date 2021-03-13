print('_________________________________________')
"""
loop
for
while 

"""
# looping on the lit to access each items
programming_language = ['c++', 'java', 'python']
# using list concept to display each items
print(programming_language[0])
print(programming_language[1])
print(programming_language[2])
print('_______________________')
for program in programming_language:# printing each items
    print(program)
print('______________________')
# range function
for numbers in range(10, 101, 10):
    print(numbers)
# printing each strings
for name in 'hanna':
    print(name)
print('____________________')
#break statement
for num in [1, 2, 3, 4, 5, 6]:
    print(num)
    if num == 3:
        break

for num in [1, 2, 3, 4, 5, 6]:
    if num == 4:
        continue

print('____________________')
# nested loop
names = ['hani', 'linda', 'alex', 'semira']
subjects = ['English', 'Mathematics']
for name in names:
    for subject in subjects:
        print(name, subject)

print('____________________')
# else statement
for num in range(1,5):
    print(num)
else:
    print('loop time ')
print('____________________')












