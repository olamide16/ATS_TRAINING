def creditCardNumber(num):
    num = input("Enter your credit card number: ")
    if len(num)< 16 and len(num) > 16:
        return False
    return '*' * (len(num) -4) + num[-4: ]
