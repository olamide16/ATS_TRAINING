class Student:
    
    profilelist ={"abdulwali": {"first_name" :"Abdulwali", "last_name":"Tajudeen","attendance": 11,"height": 78, "weight": 23,"age":27, "birthday": {"day":17, "month": "July",}},
                "basheer":{"first_name" :"Basheer", "last_name":"Balogun","attendance": 11,"height": 46, "weight": 23,"age":22, "birthday": {"day":8, "month": "april",}},
                "abdullahi":{"first_name" :"Abdullahi", "last_name":"Salam","attendance": 11,"height": 25, "weight": 23,"age":23, "birthday": {"day":8, "month": "May",}},
                "faith":{"first_name" :"Faith", "last_name":"Adeosun","attendance": 11,"height": 50, "weight": 23,"age":23, "birthday": {"day":8, "month": "Agu",}},
                "ahmad": {"first_name" :"Ahmad", "last_name":"Sharafudeen","attendance": 11,"height": 71, "weight": 23,"age":23, "birthday": {"day":8, "month": "July",}},
                "toluwanimi":  {"first_name" :"Toluwanimi", "last_name":"Ogunbiyi","attendance": 11,"height": 34, "weight": 24,"age":21, "birthday": {"day":8, "month": "Nov",}},
                "awwal": {"first_name" :"Awwal", "last_name":"Adeleke","attendance": 11,"height":49 ,"weight": 23,"age":23, "birthday": {"day":8, "month": "Dec",}},
                "abraham": {"first_name" :"Abraham", "last_name":"Adekunle","attendance": 11,"height": 65, "weight": 23,"age":23, "birthday": {"day":8, "month": "May",}},
                "yusuff": {"first_name" :"Yusuff", "last_name":"Oyedele","attendance": 11,"height": 52, "weight": 23,"age":23, "birthday": {"day":8, "month": "Oct",}},
                "adebusola": {"first_name" :"Adebusola", "last_name":"Adeyeye","attendance": 11,"height": 43, "weight": 23,"age":26, "birthday": {"day":8, "month": "Feb",}},
                "lukman": {"first_name" :"Lukman", "last_name":"Abisoye","attendance": 11,"height": 35, "weight": 54,"age":29, "birthday": {"day":4, "month": "Jan",}}}
    
    new_profilelist = {}

    def __init__(self, **kwargs):
        self.kwargs = kwargs
    
    def increment_attendance(self,attendance):
        attendance = attendance['abdulwali']['attendance'] + 1
        print("Attendance of Abdulwali has being increase by one")
    
    
    def update_first_and_lastname(self,fname):
        fname = input("Enter your first name: ")
        
        if fname[input]:
            f_name = input("Enter your first name: ")
            l_name = input("Enter your last name: ")
        
        fname[input]["first_name"] = f_name
        fname[input]["last_name"] = l_name
        print(f"Your full name now :{f_name} {l_name}")
        print(fname[input])
    
    
    def number_of_student(self,data,new):
        fname = input("Enter your first name: ")
        
        if data[input]:
            return len(new)
    
    
    def calculate_BMI(self,data):
        height = float(input("Enter your height in cm: "))
        weight = float(input("Enter your weight in kg: "))
        for i in data:
            if data[i]["height"] == height and data[i]["weight"] == weight: 
                BMI = weight/ (height/100) ** 2
                print(f"Your BMI is {BMI}")
    
    
    def max_age(self,data):
        age_list = []
        for i in data:
            age_list.append(i["age"])
        age_list.sort()
        print("The max age is:", age_list[:-1])
    
    
    def min_age(self,data):
        age_list = []
        for i in data:
            age_list.append[i["age"]]
        age_list.sort()
        print("The min age is:", age_list[0])
    
    
    def average_age(self,data):
        age_list = []
        for i in data:
            age_list.append[i["age"]]
        average = sum(age_list)/len(age_list)
        print(f"Average of the age is {average}")
        
    def add_new_profile(self,data):
        new_profile = {}
        fname = input("Enter your first name: ")
        
        new_profile["first_name"] = input("Enter your first name: ")
        new_profile["lastname"] = input("Enter your last name: ")
        new_profile["attendance"] = input("Enter your first name: ")
        new_profile["height"] = input("Enter your first name: ")
        new_profile["weight"] = input("Enter your first name: ")
        new_profile["age"] = input("Enter your first name: ")
        day_and_month = {}
        day_and_month["day"] = int("Enter your birthday day: ")
        day_and_month["day"] = str("Enter your birthday month: ")
        new_profile["Birthday"] = day_and_month
        
        data[fname] = new_profile
        new_profile["1"] = data
        print(data)
        
        return new_profile
    
    
    def remove_profile(self,data):
        fname = input("Enter your first name")
        if data[fname]:
            data.pop(fname)
            return len(data)
        print(data)
        
    
    def title_case(self,fname):
        key = input("Enter your first name: ")
        if fname[key]:
            first_name = fname[key]["frist_name"].title()
            last_name = fname[key]["frist_name"].title()
            fullname = first_name + " "+ last_name
            return fullname
        
        
    def birth_month(self,data):
        input = input("Enter your first name: ")
        
        if data[input]:
            return data[input]["birthday"]["month"]
        
        
    def list_inti(self,data):
        for i in data:
            first_name_init = data[i]["first_name"][0]
            last_name_init = data[i]["last_name"][0]
            print(first_name_init + last_name_init)
            
            
    def birth_year(self,data,year):
        
        current = 2022
        for i in data:
            if data[i]["age"] == year:
                dob_year = current - year
            return dob_year
        

def main():

    p = Student()
    data = p.profilelist

    n = Student()
    new = n.new_profilelist
    new["1"] = data

    print("""
    Choose your option
    1)  To increment your attendance
    2)  update firstname and lastname
    3)  list of fullnames in title case
    4)  add profile
    5)  return number of student
    6)  remove profile
    7)  return name of birth month
    8)  group profile by birth month
    9)  list of initial profile names
    10) calculate BMI
    11) calculate average age
    12) minimum age
    13) minimum_age
    14) calc birth year
    """)
    ask = int(input("option : "))
    if ask == 1:
    #calling increase method to increase attendance value by 1
        print(p.increase_attendance(data))
    elif ask == 2:
        print(p.update_first_and_lastname(data))
    elif ask == 3:
        full=p.fullname_in_titlecase(data)
        print(full)
    elif ask == 4:
        newpro = p.add_new_profile(data)
        print(newpro)
    elif ask == 5 :
        print(p.number_of_student(data,new))
    elif ask == 6:
        print(p.remove_profile(data))
    elif ask == 7:
        print(p.name_of_birth_month(data))
    elif ask == 8:
         print(p.group_profile_by_birth_month(data))
    elif ask == 9:
        print(p.return_list_of_initials(data))
    elif ask == 10:
        print(p.calculate_BMI(data))
    elif ask == 11:
        print(p.average_age(data))
    elif ask == 12:
        print(p.max_age(data))
    elif ask == 13:
        print(p.minimum_age())
    elif ask == 14:
        print(p.birth_year(data))

if __name__ == "__main__":
    main()   
    