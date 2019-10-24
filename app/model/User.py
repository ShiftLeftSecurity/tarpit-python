class User:
    def __init__(self, userName, firstName, lastName, passportNumber, address1, address2, zipCode):
        self.userName = userName
        self.firstName = firstName
        self.lastName = lastName
        self.passportNumber = passportNumber
        self.address1 = address1
        self.address2 = address2
        self.zipCode = zipCode

    def toString(self):
        return "[userName: " + self.userName + ", firstName: " + self.firstName + ", lastName: " + self.lastName + ", passportNumber: " + self.passportNumber +\
            ", address1: " + self.address1 + ", address2: " + self.address2 + ", zipCode: " + self.zipCode + "]"
