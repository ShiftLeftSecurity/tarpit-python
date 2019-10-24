import datetime
import app

class Order:

    def __init__(self, orderId, custId, orderDate, orderStatus, shipDate, creditCardNumber,
                 street, city, state, zipCode, emailAddress):
        self.orderId = orderId
        self.custId = custId
        self.orderDate = orderDate
        self.orderStatus = orderStatus
        self.shipDate = shipDate
        self.creditCardNumber = creditCardNumber
        self.street = street
        self.city = city
        self.state = state
        self.zipCode = zipCode
        self.emailAddress = emailAddress

    def toString(self):
        return "[orderId: " + self.orderId + ", custId: " + self.custId + ", orderDate: " + self.orderDate.strftime(app.DATE_FORMAT) +\
               ", orderStatus: " + self.orderStatus + ", shipDate: " + self.shipDate.strftime(app.DATE_FORMAT) + ", creditCardNumber: " +\
               self.creditCardNumber + ", street: " + self.street + ", city: " + self.city + ", state: " + self.state +\
               ", zipCode: " + self.zipCode + ", emailAddress: " + self.emailAddress + "]"
