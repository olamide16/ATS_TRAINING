from math import remainder


conversion_table = {0:'0', 1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9',10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}



# def decimalToHexadecimal(decimal):
#     hexadecimal = ''
#     while(decimal > 0):
#         remainder = decimal % 16
#         hexadecimal = conversion_table[remainder] + hexadecimal
#         decimal = decimal // 16
#     return hexadecimal

# decimal_number = 90
def decimalToHexadecimal(decimal):
    if(decimal <= 0):
        return ''
    remainder = decimal % 16
    return decimalToHexadecimal(decimal//16) + conversion_table[remainder]
  
  
decimal_number = 69
print(decimalToHexadecimal(decimal_number))
        