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
print("Geben Sie help ein, um alle Befehle anzuzeigen")

started = False
stopped = False
zerod = False
cbelt = False

while True:
    try:
       ima_terminal = input("IMA> ").lower()        
    except KeyboardInterrupt:
        print("Verwenden Sie einfach den Exit-Befehl")

    if ima_terminal == "hilfe":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("1. Anfang – startet und wärmt die IMA-Maschine auf")
        print("2. Pause - schaltet die Maschine aus")
        print("3. Null - zerpetzt jede Komponente in der Maschine, damit sie richtig funktioniert")
        print("4. Gürtel - schaltet das Förderband ein, damit Sie Holz kleben können")
        print("4. Leim_Holz - klebt PVC nur auf Holz, wenn die Maschine gestartet wird")
        print("5. Exit - schaltet den Computer der Maschine aus (Computer heruntergefahren)")

#------------------------------------------------------------------------------------------

    elif ima_terminal == "anfang":
        if started:
            print("Maschine bereits gestartet!")
        elif stopped and zerod and started:
            started = True
            print("Maschine gestartet, wärmt auf...")
        elif not zerod:
            print("Sie müssen die Maschine vor dem Start auf Null stellen!")
        else:
            started = True
            print("Maschine gestartet, wärmt auf...")

#------------------------------------------------------------------------------------------

    elif ima_terminal == "pause": 
        if not started:
            stopped = False
            print("Maschine kann nicht heruntergefahren werden, da sie nicht gestartet wurde!")
        else:
            cbelt = False
            started = False
            zerod = False
            print("Maschine schaltet ab Abkühlen...")   
    
#------------------------------------------------------------------------------------------

    elif ima_terminal == "null":
        if zerod: 
            print("Maschine bereits genullt!")
        else:
            zerod = True
            print("Maschinennullung startbereit...")

#------------------------------------------------------------------------------------------

    elif ima_terminal == "gürtel":
        if cbelt:
            print("Förderband ist bereits eingeschaltet!")
        elif not started:
            print("Maschine muss eingeschaltet sein, um Förderband zu starten!")
        else:
            cbelt = True
            print("Förderband an")

#------------------------------------------------------------------------------------------

    elif ima_terminal == "leim_holz":
        os.system('cls' if os.name == 'nt' else 'clear')
        if not started:
            print("Sobald die Maschine gestartet ist, können Sie mit dem Kleben beginnen")
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
                    prog = int(input("Wählen Sie ein Programm: "))
                    assert 0 < prog < 12
                except AssertionError:
                    print("Dieses Programm existiert nicht")
                if prog == 1:
                    print("Dieses Programm ist nicht verfügbar!")
                elif prog == 11:
                    print("Dies ist ein Leimtest, bei dem kein PVC auf das Holz geklebt wird")
                    wood_width = int(input("Breite Holz: "))
                    wood_length = int(input("Länge Holz: "))
                    print(f"Kleben...")
                    sleep(2)
                    print(f"Klebetest erfolgreich {wood_length}!")
                    sleep(2)
                    print(f"Klebetest erfolgreich {wood_width}!")
                else:
                    wood_width = int(input("Breite Holz: "))
                    wood_length = int(input("Länge Holz: "))
                    color_pvc = input("PVC-Farbe: ")
                    print("Holzbreite verleimen...")
                    sleep(2)
                    print(f"Fertige Leimbreite von Holz {wood_width} mit {color_pvc} PVC auf Programm {prog}.")
                    print("Holzlänge verleimen...")
                    sleep(2)
                    print(f"Fertig verleimte Holzlänge {wood_length} mit {color_pvc} PVC-Programm {prog}.")
            except ValueError:
                print("Ungültiger Wert! Beenden des Programms")        
        else:
            try:
                if not cbelt:
                    print("Sie müssen das Förderband starten, um mit dem Kleben zu beginnen!")
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
                        try:
                            prog = int(input("Wählen Sie ein Programm: "))
                            assert 0 < prog < 12
                        except AssertionError:
                            print("Dieses Programm existiert nicht")
                      if prog == 1:
                          print("Dieses Programm ist nicht verfügbar!")
                      elif prog == 11:
                          print("Dies ist ein Leimtest, bei dem kein PVC auf das Holz geklebt wird")
                          wood_width = int(input("Breite Holz: "))
                          wood_length = int(input("Länge Holz: "))
                          print(f"Kleben...")
                          sleep(2)
                          print(f"Klebetest erfolgreich {wood_length}!")
                          sleep(2)
                          print(f"Klebetest erfolgreich {wood_width}!")
                     else:
                          wood_width = int(input("Breite Holz: "))
                          wood_length = int(input("Länge Holz: "))
                          color_pvc = input("PVC-Farbe: ")
                          print("Holzbreite verleimen...")
                          sleep(2)
                          print(f"Fertige Leimbreite von Holz {wood_width} mit {color_pvc} PVC auf Programm {prog}.")
                          print("Holzlänge verleimen...")
                          sleep(2)
                          print(f"Fertig verleimte Holzlänge {wood_length} mit {color_pvc} PVC-Programm {prog}.")
                    except ValueError:
                        print("Ungültiger Wert! Beenden des Programms") 

#------------------------------------------------------------------------------------------

    elif ima_terminal == "klar":
        os.system('cls' if os.name == 'nt' else 'clear')

#------------------------------------------------------------------------------------------

    elif ima_terminal == "ausfahrt":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Vielen Dank, dass Sie IMA verwenden. Ich wünsche Ihnen einen schönen Tag")
        break

#------------------------------------------------------------------------------------------

    else:
        print("Sry das verstehe ich nicht")
