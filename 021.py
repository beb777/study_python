class Student:

    def __init__(self):
        #instance variable
        self.name = input("Enter your name:")
        self.cname = input("Enter your college name:")
        self.section = int(input("Enter your section:"))


class Test(Student):
    def display(self):
        print("============ Student info  ==========")
        print("Name is : ", self.name)
        print("College Name is:", self.cname)
        print("Roll number is:", self.section)


stud1 = Test()
stud1.display()
