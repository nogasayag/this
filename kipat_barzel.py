import math
threat = int(input("enter a number between 1 and 4: "))
X_coordinate = int(input("enter a number between 0 and 20: "))
Y_coordinate = int(input("enter a number between 0 and 20: "))
barzel_X = 0
barzel_Y = 0
d = math.sqrt((X_coordinate - barzel_X)**2 + (Y_coordinate - barzel_Y)**2)
area = (X_coordinate, Y_coordinate)

if threat == 4:
    print("don't worry, nothing happened :)")
elif threat > 4 or threat < 1:
    print("please specify threat!")
else:
    if threat == 3 or d > 13:
        take_down = "can't remove threat"
    else:
        take_down = "removing threat"

    if threat == 1:
        secs_left = "30 seconds left to get home"
    elif threat == 2:
        secs_left = "60 seconds left to get home"
    elif threat == 3:
        secs_left = "120 seconds left to get home"
    else:
        secs_left = "please specify threat."

    if 0 < X_coordinate < 10 and 0 < Y_coordinate < 10:
        area = "open land"
    elif 10 < X_coordinate < 20 and 10 < Y_coordinate < 20:
        area = "settlement a"
    elif 10 < X_coordinate < 20 and (0 < Y_coordinate < 10):
        area = "settlement b"
    elif 0 < X_coordinate < 10 and (10 < Y_coordinate < 20):
        area = "settlement c"
    
    print("the area is", area, ",", "you have", secs_left, ",", take_down)
