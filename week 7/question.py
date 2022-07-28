class Student:
    def __init__(self,first_name,last_name,attendance) -> None:
        self.attendance = attendance
        self.first_name = first_name
        self.last_name = last_name
    def increase_attendance(self):
        self.attendance += 1
        
    
    def upadate_fullname(self,new_first_name,new_last_name):
        self.first_name = new_first_name
        self.last_name = new_last_name 
    
    
    def calculate_BMI(self):
        height = float(input("Enter your height in cm: "))
        weight = float(input("Enter your weight in kg: "))
        # for i in data:
            # if data[i]["height"] == height and data[i]["weight"] == weight: 
                # BMI = weight/ (height/100) ** 2
                # print(f"Your BMI is {BMI}")