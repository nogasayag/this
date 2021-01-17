import math
op = int(input("pick a number between 1 and 6: "))
num_1 = int(input("enter any number: "))
num_2 = int(input("enter any number: "))

if op == 1:
   print(num_1 + num_2)
elif op == 2:
    print(num_1 - num_2)
elif op == 3:
    print(num_1 * num_2)
elif op == 4 and num_2 != 0:
    print(num_1 / num_2)
elif op == 5:
    print(num_1 ** num_2)
elif op == 6:
    print("to calculate a square root, we will only use the first number.")
    print(math.sqrt(num_1))
else:
    print("wrong action!")
