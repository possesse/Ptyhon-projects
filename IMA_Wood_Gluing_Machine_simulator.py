import os
from time import sleep
os.system('cls' if os.name == 'nt' else 'clear')
print(r"""








                                                                            ________________         ________        ________                  
                                                                           |                |       |      | \      / |      |                /‾‾‾‾\
                                                                           |______    ______|       |      |  \    /  |      |               /      \   
                                                                                 |    |             |      |   \  /   |      |              /        \     
                                                                                 |    |             |      |    \/    |      |             /          \
                                                                                 |    |             |      |\        /|      |            /     /\     \
                                                                                 |    |             |      | \      / |      |           /     /  \     \
                                                                                 |    |             |      |  \    /  |      |          /     / /\ \     \
                                                                                 |    |             |      |   \  /   |      |         /     / /__\ \     \
                                                                           |‾‾‾‾‾‾    ‾‾‾‾‾‾|       |      |    \/    |      |        /     /________\     \
                                                                           |                |       |      |          |      |       /     /          \     \
                                                                            ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾         ‾‾‾‾‾‾            ‾‾‾‾‾‾        ‾‾‾‾‾‾            ‾‾‾‾‾‾
                                                                                                            IMA Scheling




""")
sleep(3)
os.system('cls' if os.name == 'nt' else 'clear')
print("Type help to see all the commands")

started = False
stopped = False
zerod = False
cbelt = False

while True:
    try:
       ima_terminal = input("IMA> ").lower()        
    except KeyboardInterrupt:
        print("Just use the exit command")

    if ima_terminal == "help":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("1. Start - starts and warms up the IMA machine")
        print("2. Stop - switches off the mechine")
        print("3. Zero - zerpes every component in the machine so it works properly")
        print("4. Cbelt - switches on the conveyor belt so you can glue wood")
        print("4. Glue_wood - glues pvc on wood only when the machine is started")
        print("5. Exit - switches off the computer of the mechine (computer shut down)")

#------------------------------------------------------------------------------------------

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

#------------------------------------------------------------------------------------------

    elif ima_terminal == "stop": 
        if not started:
            stopped = False
            print("Unable to shut down machine since it's not started!")
        else:
            cbelt = False
            started = False
            zerod = False
            print("Machine shutting down cooling off...")   
    
#------------------------------------------------------------------------------------------

    elif ima_terminal == "zero":
        if zerod: 
            print("Machine already zeroed!")
        else:
            zerod = True
            print("Machine zeroing ready for start...")

#------------------------------------------------------------------------------------------

    elif ima_terminal == "cbelt":
        if cbelt:
            print("Conveyor is already on!")
        elif not started:
            print("Machine must be on to start conveyor belt!")
        else:
            cbelt = True
            print("Conveyor belt on")

#------------------------------------------------------------------------------------------

    elif ima_terminal == "glue_wood":
        os.system('cls' if os.name == 'nt' else 'clear')
        if not started:
            print("You can start gluing once the machine is started")
        elif stopped:       
            print(" 1┃ ┃001 Alles Aus      ┃                                                    ┃ 1.01.10")
            print(" 2┃ ┃002  PVC 2.0mm     ┃straight                                            ┃ 1.01.10")
            print(" 3┃ ┃003  PVC 2.0mm     ┃corner rounding                                     ┃ 1.01.10")
            print(" 4┃ ┃004  PVC 0.8mm     ┃straight                                            ┃ 1.01.10")
            print(" 5┃ ┃005  PVC 0.8mm     ┃corner rounding                                     ┃ 1.01.10")
            print(" 6┃ ┃006  PVC 0.4mm     ┃straight                                            ┃ 1.01.10")
            print(" 7┃ ┃007  PVC 0.4mm     ┃perasma2                                            ┃ 1.01.10")
            print(" 8┃ ┃008 pyxi2mm        ┃isio                                                ┃ 1.01.10")
            print(" 9┃ ┃009 pyxi2mmstogilo ┃stogilo                                             ┃ 1.01.10")
            print("10┃ ┃010 pyxi2mmstogilo ┃corner rounding                                     ┃ 1.01.10")
            print("11┃ ┃011 goma test      ┃                                                    ┃15.06.11\n")
            try:
                started = True
                try:
                    prog = int(input("Choose a program: "))
                    assert 0 < prog < 12
                except AssertionError:
                    print("This program does not exist")
                if prog == 1:
                    print("This program is unavailable!")
                elif prog == 11:
                    print("This is a glue test which will not be gluing pvc to the wood")
                    wood_width = int(input("Width of wood: "))
                    wood_length = int(input("Length of wood: "))
                    print(f"Gluing...")
                    sleep(2)
                    print(f"Glue test successful {wood_length}!")
                    sleep(2)
                    print(f"Glue test successful {wood_width}!")
                else:
                    wood_width = int(input("Width of wood: "))
                    wood_length = int(input("Length of wood: "))
                    color_pvc = input("Color of pvc: ")
                    print("Gluing wood width...")
                    sleep(2)
                    print(f"Finished gluing width of wood {wood_width} with {color_pvc} pvc on program {prog}.")
                    print("Gluing wood length...")
                    sleep(2)
                    print(f"Finished gluing length of wood {wood_length} with {color_pvc} pvc program {prog}.")
            except ValueError:
                print("Invalid Value! Exiting Program")        
        else:
            try:
                if not cbelt:
                    print("You need to start the conveyor belt to start gluing!")
                else:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    cbelt = True
                    started = True
                    print(" 1┃ ┃001 Alles Aus      ┃                                                    ┃ 1.01.10")
                    print(" 2┃ ┃002  PVC 2.0mm     ┃straight                                            ┃ 1.01.10")
                    print(" 3┃ ┃003  PVC 2.0mm     ┃corner rounding                                     ┃ 1.01.10")
                    print(" 4┃ ┃004  PVC 0.8mm     ┃straight                                            ┃ 1.01.10")
                    print(" 5┃ ┃005  PVC 0.8mm     ┃corner rounding                                     ┃ 1.01.10")
                    print(" 6┃ ┃006  PVC 0.4mm     ┃straight                                            ┃ 1.01.10")
                    print(" 7┃ ┃007  PVC 0.4mm     ┃perasma2                                            ┃ 1.01.10")
                    print(" 8┃ ┃008 pyxi2mm        ┃isio                                                ┃ 1.01.10")
                    print(" 9┃ ┃009 pyxi2mmstogilo ┃stogilo                                             ┃ 1.01.10")
                    print("10┃ ┃010 pyxi2mmstogilo ┃corner rounding                                     ┃ 1.01.10")
                    print("11┃ ┃011 goma test      ┃                                                    ┃15.06.11\n")
                    try:
                        prog = int(input("Choose a program: "))
                        assert 0 < prog < 12
                    except AssertionError:
                        print("This program does not exist")
                    if prog == 1:
                        print("This program is unavailable!")
                    elif prog == 11:
                        print("This is a glue test which will not be gluing pvc to the wood")
                        wood_width = int(input("Width of wood: "))
                        wood_length = int(input("Length of wood: "))
                        print(f"Gluing...")
                        sleep(2)
                        print(f"Glue test successful with wood length of {wood_length}!")
                        sleep(2)
                        print(f"Glue test successful with wood width of {wood_width}!")
                    else:
                        wood_width = int(input("Width of wood: "))
                        wood_length = int(input("Length of wood: "))
                        color_pvc = input("Color of pvc: ")
                        print("Gluing wood width...")
                        sleep(2)
                        print(f"Finished gluing width of wood {wood_width} with {color_pvc} pvc on program {prog}.")
                        print("Gluing wood length...")
                        sleep(2)
                        print(f"Finished gluing length of wood {wood_length} with {color_pvc} pvc on program {prog}.")
            except ValueError:
                    print("Invalid Value! Exiting Program")

#------------------------------------------------------------------------------------------

    elif ima_terminal == "clear":
        os.system('cls' if os.name == 'nt' else 'clear')

#------------------------------------------------------------------------------------------

    elif ima_terminal == "exit":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Thank you for using IMA have a nice day")
        break

#------------------------------------------------------------------------------------------

    else:
        print("Sry I don't understand that")
