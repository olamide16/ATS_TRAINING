from fractions import Fraction
from math import gcd


def lcm(a,b):
        return (a*b)//gcd(a,b)
    
class Rational_nums:
    def __init__(self, numerator, denominator) -> None:
        self.numerator = numerator
        self.denominator = denominator

    def add(self, Rational_num):
        # self.numerator = input(int("Enter the numerator: "))
        # self.denominator = input(int("Enter th denominator: "))
        numerator = (self.denominator * Rational_num.numerator) + (self.numerator * Rational_num.denominator) 
        denominator = (self.denominator * Rational_num.denominator)
        return Fraction(numerator, denominator)
    
    def multipliying(self, rational_num):
        numerator = self.numerator * rational_num.numerator
        denominator = self.denominator * rational_num.denominator
        return Fraction(numerator, denominator) 
    
    def subtract(self, rational_num):
        # if self.numerator == 0:
        #     return 0
        # else:
            # subtraction_inverse = gcd(self.denominator % self.numerator, self.numerator)
            # return Fraction(int(self.numerator// subtraction_inverse), int(self.denominator//subtraction_inverse))
        # def __str__(self):
            # numerator = (self.numerator * rational_num.denomiator * rational_num.denominator)/ self.denominator
            # denominator = (rational_num.numerator * self.denominator * self.denominator)/ rational_num.denominator 
            # Lcm = (self.denominator * rational_num.denominator)//gcd(self.denominator, rational_num.denominator)
            # the_lcm = lcm(self.denominator, rational_num.denominator)
            # numerator = (the_lcm*self.numerator /self.denominator) + (the_lcm * rational_num.numerator/ rational_num.denominator) 
            # return Rational_nums(int(numerator),the_lcm)
        numerator = (self.denominator * rational_num.numerator) - (self.numerator * rational_num.denominator) 
        denominator = (self.denominator * rational_num.denominator)
        return Fraction(numerator, denominator)
    def division(self, rational_num):
        # if self.numerator !=0:
        #     return 0
        # else:
            # multiplicative_inverse = gcd(self.denominator % self.numerator, self.numerator)
            numerator = self.numerator * rational_num.denominator
            denominator = self.denominator * rational_num.numerator
            return Fraction(numerator, denominator)
        
        # if multiplicative_inverse == 1:
        #     return self
        
        # return Rational_nums(int(self.numerator// multiplicative_inverse), int(self.denominator// multiplicative_inverse))
r1 = Rational_nums(2,5)
r2 = Rational_nums(1,10)
# print(r1.add(r2))
# print(r1.multipliying(r2))
# print(r1.division(r2))
print(r2.subtract(r1))