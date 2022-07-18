from ast import Num
import csv
import email

header = ['firstname','lastname','middlename','age','gender','dob','occupation','marital status','email']
with open('profile.csv','w') as file:
    csv_file = csv.DictWriter(file, fieldnames = header)
while True:
        firstname = input("Enter your first name: ")
        lastname = input('Enter last name: ')
        middlename = input('Enter your middlename: ')
        age = input('Enter your age: ')
        gender = input('Enter M for male and F for female: ')
        dob = input('Enter your date of birth: ')
        occupation = input('What is your occupation: ')
        marital_status = input('Enter your marital status: ')
        email = input('Enter your email: ')
        if gender == 'M' and gender == 'F':
            pass
        else:
            print("'Enter M for male and F for female: '")
        #     # return gender
        # if age is Num:
        #     pass
        # else:
        #     return age
        