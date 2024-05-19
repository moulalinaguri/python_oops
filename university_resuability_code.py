class Member:
    def __init__(self, firstName, lastName, email, memberId, address, mobileNumber, dateJoined):
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.memberId = memberId
        self.address = address
        self.mobileNumber = mobileNumber
        self.dateJoined = dateJoined

    def getFullName(self):
        print(self.firstName+" "+self.lastName)

    def changeAddress(self, newAddress):
        self.address = newAddress
        print("Address changed successfully")

    def changeNumber(self, newNumber):
        self.mobileNumber = newNumber
        print("Mobile number changed successfully")


class Faculty(Member):
    def __init__(self, firstName, lastName, email, memberId, address, mobileNumber, subjectsTeaching, salary, dateJoined):
        self.subjectsTeaching = subjectsTeaching
        self.salary = salary
        Member.__init__(self, firstName, lastName, email, memberId, address, mobileNumber, dateJoined)

    def getSalary(self):
        print("Your Salary is : ", self.salary)


class Student(Member):
    def __init__(self, firstName, lastName, email, memberId, address, mobileNumber, subjectsLearning, GPA, dateJoined):
        self.subjectsLearning = subjectsLearning
        self.GPA = GPA
        Member.__init__(self, firstName, lastName, email, memberId, address, mobileNumber, dateJoined)

    def getGPA(self):
        print("Your Salary is : ", self.GPA)


