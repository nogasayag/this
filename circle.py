mid_X = int(input("enter a center x coordinate: "))
mid_Y = int(input("enter a center y coordinate: "))
rand_X = int(input("enter an x coordinate: "))
rand_Y = int(input("enter a y coordinate: "))
R = int(input("enter a radius: "))
if R ^ 2 > (mid_X - rand_X) ^ 2 + (mid_Y - rand_Y) ^ 2 :
    print("the random coordinate is part of the circle")
else:
    print("the random coordinate is not part of the circle")
