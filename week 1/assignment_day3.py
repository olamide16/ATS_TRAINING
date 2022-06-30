number = int(input("Please Enter any Value: "))
reverse = 0
temp = number
if number > 9999 and number < 100000:
        while(temp > 0):
            Reminder = temp % 10
            reverse = (reverse * 10) + Reminder
            temp = temp //10
        
        print("Reverse of it is = %d" %reverse)

        if(number == reverse):
            print("%d is a Palindrome" %number)
        else:
            print("%d is Not" %number)
else:
    print("invalid input")
    
