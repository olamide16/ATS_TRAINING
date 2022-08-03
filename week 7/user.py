class User:
    def __init__(self,username,password) -> None:
        self.username = username
        self.password = password
    
    
    def get_username(self):
        return self.username 
    
    
    def get_password(self):
        return self.password
class Wallet(User):
    pass

class  Transcation(User):
    pass