import os
os.system('cls' if os.name == 'nt' else 'clear')
print("Type help to see all the commands available")
started = False
stopped = False
zerod = False

while True:

    ima_terminal = input("IMA> ").lower()

    if ima_terminal == "help":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("1. Start - starts and warms up the IMA machine")
        print("2. Stop - switches off the mechine")
        print("4. Zero - zeros every component in the machine so it works properly")
        print("5. Glue_wood - glues pvc on wood only when the machine is started")
        print("6. Quit - switches off the computer of the machine (computer shut down)")
    elif ima_terminal == "start":
        if started:
            print("Machine already started!")
        elif stopped and zerod and started:
            started = True
            print("Machine started, warming up...")
        elif not zerod:
            print("You need to zero the machine before starting!")     
        else:
            started = True
            print("Machine started, warming up...")
    elif ima_terminal == "stop":
        if not started:
            stopped = False
            print("Unable to shut down machine since it's not started!")
        else:
            started = False
            zerod = False
            print("Machine shutting down cooling off...")
    elif ima_terminal == "zero":
        if zerod: 
            print("Machine already zeroed!")
        else:
            zerod = True
            print("Machine zeroing ready for start...")
    elif ima_terminal == "glue_wood":
        if not started:
            print("You can start gluing once the machine is started")  
        elif stopped:
            started = True
            wood_width = input("Width of wood: ")
            wood_length = input("Length of wood: ")
            color_pvc = input("Color of pvc: ")
            print(f"Starting to glue width of wood {wood_width} with {color_pvc} pvc.")
            print(f"Starting to glue length of wood {wood_length} with {color_pvc} pvc.")      
        else:
            started = True
            wood_width = input("Width of wood: ")
            wood_length = input("Length of wood: ")
            color_pvc = input("Color of pvc: ")
            print(f"Starting to glue width of wood {wood_width} with {color_pvc} pvc.")
            print(f"Starting to glue length of wood {wood_length} with {color_pvc} pvc.")
    elif ima_terminal == "clear":
        os.system('cls' if os.name == 'nt' else 'clear')
    elif ima_terminal == "quit":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Thank you for using IMA have a nice day")
        break
    else:
        print("Sry I don't understand that")
    
