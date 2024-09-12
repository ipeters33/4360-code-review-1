import json
from user import User
from account import Account
from message import Message

message = Message()

class Auth:
    def __init__(self):
        pass

    def login(self, username, password):
        with open('db.json', 'r') as file:
            users = json.load(file)['users']

        for user in users:
            if user['name'] == username and user['password'] == password:
                    accounts = self.get_accounts(user['accounts'])
                    return User(user['name'], accounts)
            else:
                message.print("name or password not found")
        return None
    
    def get_accounts(self, userAccounts):
        accounts = {}
        for account in userAccounts:
            accounts[account['accountNumber']] = Account(account['balance'])

