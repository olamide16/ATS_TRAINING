import random
def __init__(self):
        ## define the range
        self.LOWER = 1
        self.HIGHER = 100

    ## method to generate the random number
def get_random_number(self):
        return random.randint(self.LOWER, self.HIGHER)

   
def start(self):
        random_number = self.get_random_number()

        print(f"Guess the randomly generated number from {self.LOWER} to {self.HIGHER}")


        chances = 0
        while True:
            user_number = int(input("""
                                    I ahve a number between 1 and 1000
                                    Can you guess my number?
                                    Please type your first guess. 
                                    """))
            if user_number == random_number:
                print(f"-> Hurray! You got it in {chances + 1} step{'s' if chances > 1 else ''}!")
                break
            elif user_number < random_number:
                print("-> Your number is less than the random number")
            else:
                print("-> Your number is greater than the random number")
            chances += 1