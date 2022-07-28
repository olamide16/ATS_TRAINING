class User:
    def __init__(self,first_name,last_name,email,password):
        self.first_name = first_name 
        self.last_name = last_name 
        self._email = email 
        self.__password = password  
    
    
    def firstname(self):
        return self.first_name
    
    
    def lastname(self):
        return self.last_name
    
    
    def email(self):
        return self._email
    # 
    
    def password(self):
        return self.__password 
    
    
    def update_firstname(self, new_first_name): 
        self.first_name = new_first_name
        
    
    def update_last_name(self,new_last_name):
        self.last_name = new_last_name
        
        
    def update_email(self,new_email):
        self._email = new_email
        
        
    def update_password(self,new_password):
        self.__password = new_password
# user1 = User()
# user1.first_name = "Olamide"
# user1.last_name = "Adewale"
# user1._email = "adewale@gmail.com"
# user1.__password = "123409784352" 
user = User("olamide","Adewale","adewale@gmail.com","1234509821345")
# print(user.first_name)
# print(user._email)
user.update_password("1234509825617")
print(user.password())
# user.update_firstname("Adekunle")
user.__password = "1234509825617"
# print(user._User__password("12345678"))
# print(user)