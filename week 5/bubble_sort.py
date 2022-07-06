n = int(input("Enter number of data items: "))
lst = []
for i in range(n):
   x = input("Enter data:") 
   lst.append(x)
print("Unsorted data is")
print(lst)

for i in range(0,len(lst)):
   for j in range(1,len(lst)-i):
       if(lst[j-1] > lst[j]):
           tmp = lst[j-1];
           lst[j-1] = lst[j]; 
           lst[j] = tmp;

print("Sorted data is")
print(lst)