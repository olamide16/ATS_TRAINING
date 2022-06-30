
header = ['username', 'first_name','last_name', 'password']
def signin():
    username = get_username()
    password = get_password()
    if
def signup():
    username = get_username()
    first_name = get_first_name()
    last_name = get_last_name()
    password = get_password()
    confirm_password = get_confirm_password()
    
    if not validate_username():
        print(f"username{username} already exists")
        return False
    if not validate_confirm_password():
        print(f"Error! Password and confirm password are different")
        return False


def get_username():
    return input("Enter your prefferd username: ")
def get_first_name():
    return input("Enter your first name")
def password():
    return input("Enter a password: ")
def get_last_name():
    return input("Enter your last name: ")
def get_password():
    return input("Enter a strong password")
def get_confirm_password():
    return input("Enter a confirm password")
def validate_confirm_password(password, confirm_password):
    return password != confirm_password
def validate_username(username):
    save(username=username, first_name=get_first_name, ignore_expires=False)
    
def get_data():
    with open('user_db.csv', 'r') as f:
        csv_file = csv.DictReader(f, fieldnames=header)
        return list(csv_file)

def save_data(**kwargs):
    with open('user_db.csv', 'a') as f: 
        csv = csv.DictWriter(f, fieldnames= header)
        csv_file.writerow(kwargs)
        
    
        
def main():
    option = input("Enter 1 to signup or 2 to signup")
    if option == '1':
        signup()
    else:
        invalid