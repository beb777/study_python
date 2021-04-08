class phone_numbers:
    def __init__(self, name, number):
        self.name = input('your name: ')
        self.number = int(input('your number: '))

    def display(self):
        print(f'name: {self.name} >>>> phoneNumber: {self.number}')


num1 = phone_numbers('name', 'number')
num1.display()
