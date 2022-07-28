import csv
# def signup():
#         signup_info= {}
#         signup_info['username'] = input("Enter your username: ")
#         signup_info['firstname'] = input("Enter your firstname: ")
#         signup_info['lastname'] = input("Enter your lastname: ")
#         signup_info['password'] = input("Enter your password: ")
#         confirm_password = input("retype password: ")
#         if len(signup_info['password']) <= 8 and signup_info['password'] == confirm_password:
#             with open('signup.csv','w') as f:
#                 f.write(str(signup_info))
#         else:
#             print("wrong input")
#             return (signup_info['password']) and (confirm_password)

# def signin():
#     username = get_username()
#     password = get_password()

#     data = get_data()
#     for profile in data:
#         if profile['username'] == username and profile['password'] == password:
#             print(f'Login successful')
#             return
#     print(f"Invalid login credentials")
# def get_username():
#     return input("Enter your username: ")
# def get_password():
#     return input("Enter password: ")

# def get_data():
#     with open('signup.csv', 'r') as f:
#         csv_file = csv.DictReader(f)
#         return list(csv_file)

# def main():
#     option = input("Enter 1 to signup or 2 to signin (Default is 'Sign-In'): ")
#     if option == '1':
#         signup()
#     else:
#         signin()
# def edit_profile():
#     phone_number = int(input("Input your phone number: "))
#     address = input("Enter your house address: ")
#     dob = ("Enter your date of birth: ")
#     gender = input("Enter 'M' for male and 'F' for female")
# if __name__ == "__main__":
#     main()
# account = ""
# def change_password():
#     old_password = input("Enter old password: ")
#     if old_password == get_password():
#         return input("Enter new password")
#         with open("signup.csv['passowrd'], 'a'") as file:
#             csv.append(file)
#     else:
#         return("not corresponding with your former one")
    
# while True:
#     account = input("choose:\n 1. Edit profile\n 2. Change password\n 3. logout ")
#     if account == 1:
#         edit_profile()
#     if account == 2:
#         change_password()
#     if account == 3:
#         signin()

def signup():
    username = input("Enter your username: ")
    firstname = input("Enter your firstname: ")
    lastname = input("Enter your lastname: ")
    password = input("Enter your password: ")
    confirm_password = input("retype password: ")
    if len(password) < 8:
        print("Length of password is not up to 8 ")
        return
    
    if password != confirm_password:
        print("Password and retype password are not the same")
        return
    csv_rowlist = [["username","firstname","lastname","password"],
                   [username,firstname,lastname,password]]
    with open("signup.csv","w") as f:
        writer = csv.writer(f)
        writer.writerows(csv_rowlist)
    main()
           

def signin():
    check = open("signup.csv","r")
    csvfile = csv.reader("signup.csv")
    username = input("please enter your username: ")
    password = input("Please enter your password: ")
    for line in csvfile:
    
        if  line[0] == username and line[1] == password:
            print("Login successful")
        else: 
            print("Invalid login credentials")
    while True:
        account = input("choose:\n 1. Edit profile\n 2. Change password\n 3. logout\n ")
        if account == 1:
            edit_profile()
        if account == 3:
            break
        
        
def edit_profile():
    phone_number = int(input("Input your phone number: "))
    address = input("Enter your house address: ")
    dob = ("Enter your date of birth: ")
    gender = input("Enter 'M' for male and 'F' for female")
    csv_list = [["phone_number","address","dob","gender"],
                [phone_number,address,dob,gender]]  
    with open("signup.csv","a") as file:
        writer = csv.writer(file)
        writer.writerows(csv_list)

def main():
    option = input("Enter 1 to signup or 2 to signin (Default is 'Sign-In'): ")
    if option == '1':
        signup()
    else:
        signin()

if __name__ == "__main__":
    main()      