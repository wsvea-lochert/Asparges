import pyrebase
import datetime
from db.confg import get_config

config = get_config()

firebase = pyrebase.initialize_app(config)


def login(username, password):  # Static for now.
    auth = firebase.auth()
    user = auth.sign_in_with_email_and_password(username, password)

    if user is not None:
        print('You are logged in!')
    else:
        print('try again.')
        user = auth.sign_in_with_email_and_password(input('Username: '), input('Password: '))
    return user


class User:  # User class to handle all of db connections.
    def __init__(self, name):
        self.name = name
        self.info = login(input('Username: '), input('Password: '))  # TODO: Change so its not hardcoded.
        self.idToken = self.info["idToken"]

    def append_data(self, model, price):
        db = firebase.database()
        db.child('product')
        data = {'model': model, 'price': price, 'time-stamp': str(datetime.datetime.now())}
        db.child('GPU').push(data)

    def verify_account(self):
        firebase.auth().send_email_verification(self.idToken)
