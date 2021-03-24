class Students: # class name is Student
    def __init__(self, first_name, last_name, roll_num):#sepecal method with three argument
        ''' first_name, last_name and roll_num are a variables
        when we create an object we have to pass the value'''
        self.first_name = first_name
        self.last_name = last_name
        self.roll_num = roll_num
    def update(self):
        self.first_name = 'bob'

stud = Students('hannah', 'mark', 8)
print(stud.last_name, stud.first_name, stud.roll_num)
print(f'Name: {stud.first_name} {stud.last_name}. Roll number: {stud.roll_num}')
stud.update()
print(stud.last_name, stud.first_name, stud.roll_num)


