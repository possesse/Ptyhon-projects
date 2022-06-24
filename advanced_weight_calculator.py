while True:

    weight = input("How much do you weigh: ")
    kg_lbs_st = input("K(kg), L(lbs), S(st): ")

    if kg_lbs_st in ['K', 'k']:
        wtotal1 = int(weight) * 2.205
        wtotal2 = int(weight) / 6.35
        print("You weigh " + str(wtotal1) + " in lbs and")
        print("You weigh " + str(wtotal2) + " in stones.")

    elif kg_lbs_st in ['L', 'l']:
        wtotal3 = int(weight) / 2.205
        wtotal4 = int(weight) * 14
        print("You weigh " + str(wtotal3) + " in kg and")
        print("You weigh " + str(wtotal4) + " in stones.")

    elif kg_lbs_st in ['S', 's']:
        wtotal5 = int(weight) / 6.35
        wtotal6 = int(weight) * 14
        print ("You weigh " + str(wtotal5) + " in kg and")
        print("You weigh " + str(wtotal6) + " in lbs.")
    
    next_calculation = input("Would you like to calculate more weight (yes/no): ")
    if next_calculation == "no":
        break
    else:
        print("Invalid Input")
    