def convertTemp(c):  
   f = (c * 1.8) + 32
   return f
    
cel = range(1,100)

fahr = convertTemp(cel)
print('%0.1f degrees Celsius is equivalent to %0.1f degrees Fahrenheit' %(cel, fahr))