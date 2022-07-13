def credit_num(num):
    input = int(input("Input your card number: "))
    if len(input) < 16 and len(input) > 16:
        return False
    else:
        return True
    