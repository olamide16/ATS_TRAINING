from re import M


automoblie = int(input("How many automobile: "))
m = []
g = []
for i in range(0,automoblie):
    mile = float(input("Enter the mile covered: "))
    m.append(mile)
for j in range(0,automoblie):
    gallon = float(input("Enter the gallon of fuel used: "))
    g.append(gallon)
average = sum(m)/sum(g)
print("Average of the each automobile", round(average,2))

# m = float(input("Enter the miles covered: "))
# g = float(input("Enter the gasolin in gallon used: "))
# print(f"The average used is: {m/g}")    
