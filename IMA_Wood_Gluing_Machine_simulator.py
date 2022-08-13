import os
os.system('cls' if os.name == 'nt' else 'clear')
print("Type help to see all the commands available")
started = False
stopped = False
restarted = False

while True:

    ima_terminal = input("IMA> ").lower()

    if ima_terminal == "help":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("1. Start - starts and warms up the IMA machine")
        print("2. Stop - switches off the mechine")
        print("3. Restart - Restarts the mechine")
        print("3. Glue_wood - glues pvc on wood only when the machine is started")
        print("4. quit - switches off the computer of the mechine (sleep mode)")
    elif ima_terminal == "start":
        if started:
            print("Mechine is already started!")        
        else:
            started = True
            print("Mechine started, warming up...")
    elif ima_terminal == "stop":
        if stopped:
            print("Mechine already stoped!")
        elif not started:
            print("Unable to shut down mechine since it's not started!")
        else:
            stopped = True
            print("Mechine shutting down cooling off...")
    elif ima_terminal == "restart":
        if stopped:
            print("Mechine restarting, warming up...")
        elif started:
            print("You cannot restart the mechine while it is on!")
        else:
            started = False
            print("You need to start the mechine and close it again to restart!")    
    elif ima_terminal == "glue_wood":
        if not started:
            print("You can start gluing once the machine is started")
        elif stopped:
            print("You need to restart the mechine after it has closed")  
        elif started: 
            wood_width = input("Width of wood: ")
            wood_length = input("Length of wood: ")
            color_pvc = input("Color of pvc: ")
            print(f"Starting to glue width of wood {wood_width} with {color_pvc} pvc.")
            print(f"Starting to glue length of wood {wood_length} with {color_pvc} pvc.")      
        else:
            stopped = True
            wood_width = input("Width of wood: ")
            wood_length = input("Length of wood: ")
            color_pvc = input("Color of pvc: ")
            print(f"Starting to glue width of wood {wood_width} with {color_pvc} pvc.")
            print(f"Starting to glue length of wood {wood_length} with {color_pvc} pvc.")
    elif ima_terminal == "clear" or "clr":
        os.system('cls' if os.name == 'nt' else 'clear')
    elif ima_terminal == "quit":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Thank you for using IMA have a nice day")
        break
    else:
        print("Sry I don't understand that")
