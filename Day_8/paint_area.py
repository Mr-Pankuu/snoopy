import math
def wall(height,width,cover):
    num_of_cans = (height * width) / cover
    round = int(math.ceil(num_of_cans))
    print(f"You need {round} paint cans to paint the wall.")

test_h = float(input("Height of wall : "))
test_w = float(input("Width of wall : "))
coverage = 5
wall (height= test_h,width= test_w,cover= coverage)
