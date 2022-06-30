import calendar
profile = [
    {"first_name":" Awwal", "last_name":"Adeleke", "age":14, "attendance": 70, "weight":65, "height":79, "day_and_month":"16-07"},
    {"first_name":"Abdulwali", "last_name":"Tajudeen", "age":14, "attendance": 70, "weight":56, "height":45, "day_and_month":"03-08"},
    {"first_name":"Abraham", "last_name":"Adekunle", "age":14, "attendance": 71, "weight":49, "height":81, "day_and_month":"18-09"},
    {"first_name":"Yusuff", "last_name":"oyedele", "age":14, "attendance": 72, "weight":61, "height":74, "day_and_month":"19-01"},
    {"first_name":"Adebusola", "last_name":"Adeyeye", "age":14, "attendance": 69, "weight":70, "height":75, "day_and_month":"30-12"},
    {"first_name":"Basheer", "last_name":"Balogun", "age":14, "attendance": 68, "weight":45, "height":80, "day_and_month":"31-07"},
    {"first_name":"Abdullahi", "last_name":"salaam", "age":14, "attendance": 67, "weight":72, "height":63, "day_and_month":"07-04"},
    {"first_name":"Faith", "last_name":"Adeosun", "age":14, "attendance": 73, "weight":62, "height":74, "day_and_month":"20-05"},
    {"first_name":" Ahmad", "last_name":"Sharafudeen", "age":14, "attendance": 60, "weight":69, "height":65, "day_and_month":"06-07"},
    {"first_name":"Lukman", "last_name":"Abisoye", "age":14, "attendance": 74, "weight":49, "height":70, "day_and_month":"07-06"},
    {"first_name":"Toluwanimi", "last_name":"Ogunbiyi", "age":14, "attendance": 21, "weight":64, "height":64, "day_and_month":"05-11"}
]
def increment_attendance(first_name):
    user_profile = {}
    for x in profile:
        user_profile = x
        user_profile +=1
    return user_profile

def add_profile(profile):
    new_profile = {}
    f_name = input("What is your first name: ")
    l_name = input("What is your last name: ")
    age = int(input("What si your age: "))
    attendance = int("How frequent are you in class: ")
    height = int(input("What is your height: "))
    weight = int(input("What is your weight: "))
    day_and_month = input("what is your day and birth month")
def count_number_profile(profile):
    count = 0
    for i in enumerate(profile):
        count += 1
        return count


