# Python code to find student grade

class Students:
    def __init__(self):
        self.__roll = 0
        self.__name = ""
        self.__marks = []
        self.__total = 0
        self.__per = 0
        self.__grade = ""
        self.__result = ""

    def setStudent(self):
        self.__roll = int(input("Enter Roll: "))
        self.__name = input("Enter Name: ")
        print("Enter marks of 5 subjects: ")
        for i in range(5):
            self.__marks.append(int(input("Exam " + str(i + 1) + ": ")))

    def calculateTotal(self):
        for x in self.__marks:
            self.__total += x

    def calculatePercentage(self):
        self.__per = self.__total / 5

    def calculateGrade(self):
        if self.__per >= 85:
            self.__grade = "S"
        elif self.__per >= 75:
            self.__grade = "A"
        elif self.__per >= 65:
            self.__grade = "B"
        elif self.__per >= 55:
            self.__grade = "C"
        elif self.__per >= 50:
            self.__grade = "D"
        else:
            self.__grade = "F"

    def calculateResult(self):
        count = 0
        for x in self.__marks:
            if x >= 50:
                count += 1
        if count == 5:
            self.__result = "PASS"
        elif count >= 3:
            self.__result = "COMP."
        else:
            self.__result = "FAIL"

    def showStudent(self):
        self.calculateTotal()
        self.calculatePercentage()
        self.calculateGrade()
        self.calculateResult()
        print(self.__roll, "\t\t", self.__name, "\t\t", self.__total, "\t\t", self.__per, "\t\t", self.__grade, "\t\t",
              self.__result)


def main():
    # Student object
    s = Students()
    s.setStudent()
    s.showStudent()


if __name__ == "__main__":
    main()
