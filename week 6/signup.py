import csv
headers = ['firstname','lastname','middlename','age','gender','dob','occupation','marital status','email']
def signup():
    username = input("Enter your username: ")
    firstname= input("Enter your first name:")
    lastname = input("Enter your last name: ")
    password = input("Enter a strong password: ")
    confirm_password = input("Retype password: ")
    
    if password == confirm_password:
        pass
    else:
        print('input wrong password')
        return password
with open('profile.csv','a') as file:
    csv_file = csv.DictWriter(file, fieldnames=headers)
    csv_file.writerow(file)

def signin():
    username1 = input("Enter username: ")
    password = input("Enter password: ") 

for profile in data:
    if profile['username'] == username: 