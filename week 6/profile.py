def profile():
    profile_dict = {}
    profile_dict['username'] = input("Enter user name: ")
    profile_dict['firstname'] = input("Enter your first name: ")
    profile_dict['lastname']= input("Enter your last name: ")
    profile_dict['password'] = input("Enter password: ")
    confirm_password = input("Retype your password: ")
    
    if len(profile_dict['password']) >= 8 and profile_dict['password'].isalnum() and profile_dict['password'] == confirm_password:
        with open(f"{str(profile_dict['username']) + '.csv'}" ,'w') as output:
            output.write(str(profile_dict))
    else:
        print("password incorrect")
        return profile()
        
        
    
print(profile())


    
