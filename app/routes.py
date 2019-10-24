from app import app
from app.model.User import User
from app.model.Email import Email
from app.service.OrderService import OrderService
from app.service.EmailService import EmailService

@app.route('/')
@app.route('/')
def index():
    return "Default index page"

@app.route('/insider')
def insider():
    return "insider"

@app.route('/FileUploader')
def FileUploader():
    return "FileUploader"

@app.route('/login')
def login():
    return "login"

@app.route('/logout')
def logout():
    return "logout"

@app.route('/processOrder')
def processOrder():
    return "processOrder"

@app.route('/getOrderStatus')
def getOrderStatus():
    orderService = OrderService();
    return orderService.getAccount()

@app.route('/vulns')
def vulns():
    return "vulns"

@app.route('/user')
def user():
    user = User("jmcdonald", "John", "McDonald", "P304T63145", "1110 Acorn Lane", "Rockling, CA", " 95765")
    return user.toString()


@app.route('/emailService')
def emailService():
    emailService = EmailService()
    email = Email("jmcdonald@shiftleft.io", "Testing Service",
                  "This is a test of the emergency broadcasting service. This is only a test")
    return emailService.send(email)
