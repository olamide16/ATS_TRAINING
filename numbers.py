digits = ['one', 'two',   'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
teens  = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', *[d+'teen' for d in digits[5:]]]
tens   = ['twenty', 'thirty', 'fourty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

# One digit printing
for one in digits:
    print(one)

# Two digit printing
for teen in teens:
    print(teen)
for ten in tens:
    print(ten)          
    for one in digits:
        print(ten, one) 

# Three digit printing
hundred_word = 'hundred'
for hundred in digits:
    print(hundred, hundred_word)
    for one in digits:
        print(hundred, hundred_word, one)
    for teen in teens:
        print(hundred, hundred_word, teen)
    for ten in tens:
        print(hundred, hundred_word, ten)
        for one in digits:
            print(hundred, hundred_word, ten, one)
