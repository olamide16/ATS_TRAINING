one = [ "", "one ", "two ", "three ", "four ",
    "five ", "six ", "seven ", "eight ",
    "nine ", "ten ", "eleven ", "twelve ",
    "thirteen ", "fourteen ", "fifteen ",
    "sixteen ", "seventeen ", "eighteen ",
    "nineteen "];
ten = [ "", "", "twenty ", "thirty ", "forty ",
        "fifty ", "sixty ", "seventy ", "eighty ",
        "ninety "];

def numToWords(n, s):
 
    str = "";
    if (n > 19):
        str += ten[n // 10] + one[n % 10];
    else:
        str += one[n];
    if (n):
        str += s;
 
    return str;
 

def convertToWords(n):
    out = "";
    out += numToWords(n // 10000) 
    out += numToWords(((n // 100000) % 100),)