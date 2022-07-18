def username():
    useername = input("Enter user name: ")
    firstname = input("Enter your first name: ")
    lastname= input("Enter your last name: ")
    password= input("Enter password: ")
    confirm_password = input("Retype your password: ")
    if len(password) < 8:
        return False
    elif password.isalnum():
        return True
    elif password == confirm_password:
        return True
    
