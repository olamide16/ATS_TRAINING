n = int(input("Enter number of data items: "))
list = []
for i in range(n):
   x = input("Enter data:") 
   list.append(x)
print("Unsorted data is")
print(list)

for i in range(0,len(list)):
   for j in range(1,len(list)-i):
       if(list[j-1] > list[j]):
           tmp = list[j-1];
           list[j-1] = list[j]; 
           list[j] = tmp;

print("Sorted data is")
print(list)