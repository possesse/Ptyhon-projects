import os

os.system('cls' if os.name == 'nt' else 'clear')
print("Type Help to see all the commands available")

while True:

    general_input = input("> ").lower()
    if general_input == "help":
        os.system('cls' if os.system == 'nt' else 'clear')
        print("calc_weight - calculates any weight to K(kg), L(lbs), S(st)")
        print("quit - exits program")
    elif general_input == "calc_weight":
        weight = int(input("How much do you weigh: "))
        kg_lbs_st = input("K(kg), L(lbs), S(st): ").lower()

        if kg_lbs_st == "k":
            wtotal1 = weight * 0.45
            wtotal2 = weight / 6.35
            print(f"You weigh {wtotal1} in lbs and")
            print(f"You weigh {wtotal2} in stones.")
        elif kg_lbs_st == "l":
            wtotal3 = weight / 0.45
            wtotal4 = weight * 14
            print(f"You weigh {wtotal3} in kg and")
            print(f"You weigh {wtotal4} in stones.")
        elif kg_lbs_st == "s":
            wtotal5 = weight / 6.35
            wtotal6 = weight * 14
            print (f"You weigh {wtotal5} in kg and")
            print(f"You weigh {wtotal6} in lbs.")
        else:
            print("Sry I don't understand that.")
    elif general_input == "quit":
        os.system('cls' if os.system == 'nt' else 'clear')
        break
    else:
        print("Sry but I don't understand that.")
