import random
print("This is a dice simulator")
x='y'

while(x=='y'):
    num=random.randint(1,6)
    if(num==1):
        print("-------")
        print("|      |")
        print("|  O   |")
        print("|      |")
        print("--------")
    elif(num==2):
        print("-------")
        print("|      |")
        print("| O  O |")
        print("|      |")
        print("--------")
    elif(num==3):
        print("-------")
        print("|   O  |")
        print("|      |")
        print("| O  O |")
        print("--------")
    elif(num==4):
        print("-------")
        print("| O  O |")
        print("|      |")
        print("| O  O |")
        print("--------")
    elif(num==5):
        print("-------")
        print("| O  O |")
        print("|   O  |")
        print("| O  O |")
        print("--------")
    elif(num==6):
        print("-------")
        print("| O  O |")
        print("| O  O |")
        print("| O  O |")
        print("--------")
    x=input("Press 'y' to repeat!")