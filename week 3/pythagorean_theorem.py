from itertools import combinations


def pythagorean_triplet(hypotenus, side1,side2):
    squared_hyp = hypotenus ** 2
    squared_side1 = side1**2
    squared_side2 = side2**2
    triplet = [(squared_hyp,squared_side1,squared_side2)]
    for side1,side2 in combinations(squared_side1,squared_side2):
        sum_sides = (squared_side1) + (squared_side1)
        if squared_hyp and sum_sides > 20:
            print("Enter number that the square will be less than 20")
        elif squared_hyp == sum_sides:
            print("Its obeys pythagorean_theorem")
        else: 
            print("Invalid result")