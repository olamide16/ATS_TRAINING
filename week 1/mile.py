# num1 = input("Enter your value: ")
# unit_converter = input("Which category would you like to convert? we support gallon(g) and mile(m): ")
# if unit_converter == ("g"):
#     convert = float(num1) * 22.421875
#     print(f'The gallon can go for {convert}')
# else:
#     convert = float(num1) / 22.421875
#     print(f'The gallon use is {convert}')

miles = []
gallons = []

while True:
    gallon= float(input("Enter the gallon used: "))
    mile = float(input("Enter the mile driven: "))
    if gallon == -1:
        break
    average = float(mile//gallon)
    print(f"average of this automobile is:{average}")
    miles.append(mile)
    gallons.append(gallon)

total_mile = sum(miles)
total_gallon = sum(gallons)
total_average = total_mile/total_gallon
print(f"Overall average is: {total_average}")