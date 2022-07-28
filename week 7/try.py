class Student:
    # profilelist ={"abdulwali": {"first_name" :"Abdulwali", "last_name":"Tajudeen","attendance": 11,"height": 78, "weight": 23,"age":27, "birthday": {"day":17, "month": "July",}},
    #             "basheer":{"first_name" :"Basheer", "last_name":"Balogun","attendance": 11,"height": 46, "weight": 23,"age":22, "birthday": {"day":8, "month": "april",}},
    #             "abdullahi":{"first_name" :"Abdullahi", "last_name":"Salam","attendance": 11,"height": 25, "weight": 23,"age":23, "birthday": {"day":8, "month": "May",}},
    #             "faith":{"first_name" :"Faith", "last_name":"Adeosun","attendance": 11,"height": 50, "weight": 23,"age":23, "birthday": {"day":8, "month": "Agu",}},
    #             "ahmad": {"first_name" :"Ahmad", "last_name":"Sharafudeen","attendance": 11,"height": 71, "weight": 23,"age":23, "birthday": {"day":8, "month": "July",}},
    #             "toluwanimi":  {"first_name" :"Toluwanimi", "last_name":"Ogunbiyi","attendance": 11,"height": 34, "weight": 24,"age":21, "birthday": {"day":8, "month": "Nov",}},
    #             "awwal": {"first_name" :"Awwal", "last_name":"Adeleke","attendance": 11,"height":49 ,"weight": 23,"age":23, "birthday": {"day":8, "month": "Dec",}},
    #             "abraham": {"first_name" :"Abraham", "last_name":"Adekunle","attendance": 11,"height": 65, "weight": 23,"age":23, "birthday": {"day":8, "month": "May",}},
    #             "yusuff": {"first_name" :"Yusuff", "last_name":"Oyedele","attendance": 11,"height": 52, "weight": 23,"age":23, "birthday": {"day":8, "month": "Oct",}},
    #             "adebusola": {"first_name" :"Adebusola", "last_name":"Adeyeye","attendance": 11,"height": 43, "weight": 23,"age":26, "birthday": {"day":8, "month": "Feb",}},
    #             "lukman": {"first_name" :"Lukman", "last_name":"Abisoye","attendance": 11,"height": 35, "weight": 54,"age":29, "birthday": {"day":4, "month": "Jan",}}}
    
    
    def __init__(self,fname,lname,attendance,height,weight,age) -> None:
        self.fname = fname
        self.lname = lname 
        self.attendance = attendance
        self.height = height
        self.weight = weight 
        self.age = age 
    
    
    def increase_attendance(self,profile):
        attendance = self.attendance + 1
        return attendance
    
    
    def update_firstname_and_lastname(self,pofile):
        pass