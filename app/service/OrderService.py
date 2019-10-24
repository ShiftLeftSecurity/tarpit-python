from app.model.Order import Order
import datetime

class OrderService:

    def getAccount(self):
        order = Order("WS123456", "485322", datetime.date.today(), "Pending", datetime.date.today(), "4444444444444444", "1110 Acorn Lane", "Rocklin", "CA", "95765", "jmcdonald@shiftleft.io")
        return order.toString()
