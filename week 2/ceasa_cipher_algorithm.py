message = 'KIQRAUrGMTIuIVrHIQS'
letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
 
for key in range (len(letters)):
    tanslate = " "
    for symbol in message:
        if symbol in letters:
            num = letters.find(symbol)
            num -= key
            if num < 0:
                num += len(letters)
            tanslate += letters
        else:
            tanslate += symbol 
print('Hacking key #%s: %s' % (key, tanslate))