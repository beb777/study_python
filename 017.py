class Students:# class name is Students
    def __init__(self, first_name, last_name, grade):
        self.first_name = first_name
        self.last_name = last_name
        self.grade = grade
        self.email = first_name + '.' + last_name + '@stud.com'


student_1 = Students('bob','beb','A')# student_1 is an object
#student_2 = Students()
# student_1.first_name = 'beb'
# student_1.last_name = 'bob'
# student_1.course = 'python'
# student_1.grade = 'A'

# student_2.first_name = 'max'
# student_2.last_name = 'luies'
# student_2.course = 'python'
# student_2.grade = 'B'

#print(student_1.course)
print(student_1.email)