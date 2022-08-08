class User:
    def __init__(self, firstname, last_name, password, username):
        self.firstname = firstname
        self.last_name = last_name
        self.password = password
        self.username = username
        
    def get_username(self):
        return self.username
    
    def get_firstname(self):
        return self.firstname
    
    def get_lastname(self):
        return self.last_name
    
    def get_password(self):
        return self.password

class Wallet(User):
    def __init__(self):
        super().__init__()
    
    def balance(self):
        username = User.username
        password = User.password 
        
    def wallet_funding(self):
        pass
    
    
class LoggingTransaction(User):
    def __init__(self):
        super().__init__()
        
    def trasction(self):
        print ("""
        Enter your option
        1. New user
        2. Balance
        3. Delete Account
        4. Fund wallet
        """)
        

new_user = User()