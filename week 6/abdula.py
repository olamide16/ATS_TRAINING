import csv

with open('new_file.csv', 'w') as file:
    fieldnames = ['SN', 'firstName','lastName','passWord']
    writer= csv.writer(file, fieldnames=fieldnames)
    
    writer.writeheader()
    writer.writerow([1,'Olamide','Abdulwali','123456t'])
    writer.writerow([2,'Ayo','Dele','09234y16'])