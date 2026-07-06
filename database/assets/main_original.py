import os
def cprint(szoveg=""):
    szelesseg = os.get_terminal_size().columns
    print(szoveg.center(szelesseg))
import json
from datetime import datetime

VEHICLE_DB = "database/vehicles"
USER_DB = "database/users/users.json"
LOG_FILE = "database/logs/system.log"

current_user = None

def clear():
    os.system("cls" if os.name == "nt" else "clear")
    
def log_action(action):
    with open(LOG_FILE, "a", encoding="utf-8") as log:
        log.write(f"[{datetime.now()}] USER={current_user} ACTION={action}\n")

def load_users():
    with open(USER_DB, "r", encoding="utf-8") as f:
        return json.load(f)

import time
import sys

def loading_bar():
    print("SYSTEM BOOTING")

    for i in range(101):
        bar = "█" * (i // 2)
        sys.stdout.write(f"\r[{bar:<50}] {i}%")
        sys.stdout.flush()
        time.sleep(60.03)

    print()

def login():
    global current_user

    users = load_users()

    while True:
        clear()
        cprint(" ______________________________________________________________________________________________________________________________")
        cprint("                                                                                                                               ")        
        cprint("          ██╗░░██╗░░░░░██╗██╗░░░              ███╗░░░███╗██╗░░░██╗██████╗░░█████╗░                ░░███╗░░░░░░█████╗░  ")
        cprint("          ██║░██╔╝░░░░░██║██║░░░              ████╗░████║╚██╗░██╔╝██╔══██╗██╔══██╗                ░████║░░░░░██╔══██╗  ")
        cprint("          █████═╝░░░░░░██║██║░░░              ██╔████╔██║░╚████╔╝░██████╔╝███████║                ██╔██║░░░░░██║░░██║  ")
        cprint("          ██╔═██╗░██╗░░██║██║░░░              ██║╚██╔╝██║░░╚██╔╝░░██╔══██╗██╔══██║                ╚═╝██║░░░░░██║░░██║  ")
        cprint("          ██║░╚██╗╚█████╔╝██║██╗              ██║░╚═╝░██║░░░██║░░░██║░░██║██║░░██║                ███████╗██╗╚█████╔╝  ")
        cprint("          ╚═╝░░╚═╝░╚════╝░╚═╝╚═╝              ╚═╝░░░░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝                ╚══════╝╚═╝░╚════╝░  ")
        cprint("                                                                                                                               ")
        cprint("           E N G E D É L Y E Z E T T   H O Z Z Á F É R É S I   M Ó D        A U T H O R I Z E D  A C C E S S   M O D E         ")
        cprint("           A N G O L   É S   M A G Y A R   N Y E L V Ű   V E R Z I Ó                     E N G / H U N   V E R S I O N         ")
        cprint("                                                                                                                               ")
        cprint("                 This terminal contains sensitive internal vehicle, registry and operational service information.              ")
        cprint("              **  Unauthorized access or manipulation of records is strictly prohibited and constantly monitored! **           ")
        cprint("                                                                                                                               ")
        cprint("                  Ez a terminál érzékeny belső jármű-, nyilvántartási és üzemeltetési információkat tartalmaz.                 ")
        cprint("    **  A nyilvántartásokhoz való jogosulatlan hozzáférés, adatok manipulálása szigorúan tilos, a megfigyelés folyamatos! **   ")
        cprint("                                                                                                                               ")
        cprint("                                                   𝗞𝗝𝗜. LTD. - 𝗖𝗢𝗣𝗬𝗥𝗜𝗚𝗛𝗧 © 𝟮𝟬𝟮𝟲                                                ")
        cprint(" ______________________________________________________________________________________________________________________________")
        cprint("                                                                                                                               ")
        cprint("                          𝗦𝗜𝗚𝗡 𝗜𝗡 𝗪𝗜𝗧𝗛 𝗔 𝗥𝗘𝗚𝗜𝗦𝗧𝗘𝗥𝗘𝗗 𝗨𝗦𝗘𝗥  |  JELENTKEZZEN BE EGY REGISZTRÁLT FELHASZNÁLÓVAL                   ")
        print()
        cprint("                            𝗖𝗢𝗡𝗧𝗔𝗖𝗧 𝗧𝗛𝗘 𝗖𝗢𝗠𝗣𝗔𝗡𝗬 𝗠𝗔𝗡𝗔𝗚𝗘𝗠𝗘𝗡𝗧 𝗪𝗜𝗧𝗛 𝗬𝗢𝗨𝗥 𝗔𝗣𝗣𝗥𝗢𝗩𝗘𝗗 𝗥𝗘𝗚𝗜𝗦𝗧𝗥𝗔𝗧𝗜𝗢𝗡 𝗥𝗘𝗤𝗨𝗘𝗦𝗧                     ")
        cprint("                                  JÓVÁHAGYOTT REGISZTÁCIÓS KÉRELMÉVEL FORDULJON A VÁLLALATVEZETÉSHEZ                           ")
        cprint(" ______________________________________________________________________________________________________________________________")
        print("                                                                                                                               ")
        print()
        cprint("𝗧𝗢 𝗘𝗫𝗜𝗧 𝗧𝗛𝗘 𝗣𝗥𝗢𝗚𝗥𝗔𝗠, 𝗣𝗥𝗘𝗦𝗦 𝗧𝗛𝗘 ALT + F4 𝗞𝗘𝗬 𝗖𝗢𝗠𝗕𝗜𝗡𝗔𝗧𝗜𝗢𝗡")
        cprint("A PROGRAMBÓL VALÓ KILÉPÉSHEZ NYOMJA LE A(Z) 𝗔𝗟𝗧 + 𝗙𝟰 BILLENTYŰKOMBINÁCIÓT")
            
        username = input("𝗨𝗦𝗘𝗥𝗡𝗔𝗠𝗘 | FELHASZNÁLÓNÉV:")
        password = input("𝗣𝗔𝗦𝗦𝗪𝗢𝗥𝗗 | JELSZÓ:")




        if username in users and users[username]["password"] == password:
            current_user = username
            log_action("𝗟𝗢𝗚𝗜𝗡 𝗦𝗨𝗖𝗖𝗘𝗦𝗦 | SIKERES BEJELENTKEZÉS")
            return
        else:
            print("[ ! ] 𝗜𝗡𝗩𝗔𝗟𝗜𝗗 𝗖𝗥𝗘𝗗𝗘𝗡𝗧𝗜𝗔𝗟𝗦 | HELYTELEN HITELESÍTŐADATOK  [ ! ]")
            input(" NYOMJA MEG A(Z) [ 𝗘𝗡𝗧𝗘𝗥 / 𝗥𝗘𝗧𝗨𝗥𝗡 ]  GOMBOT A VISSZALÉPÉSHEZ")

def load_vehicles():
    vehicles = []

    for file in os.listdir(VEHICLE_DB):
        if file.endswith(".json"):
            with open(os.path.join(VEHICLE_DB, file), "r", encoding="utf-8") as f:
                vehicles.append(json.load(f))

    return vehicles

def save_vehicle(vehicle):
    filename = f"{vehicle['vin']}.json"

    with open(os.path.join(VEHICLE_DB, filename), "w", encoding="utf-8") as f:
        json.dump(vehicle, f, indent=4)

def show_vehicle(vehicle):
    print(" __________________________________________________________________________________________________________")
    print(" ")
    print("      𝗩 𝗘 𝗛 𝗜 𝗖 𝗟 𝗘  𝗥 𝗘 𝗖 𝗢 𝗥 𝗗  𝗙 𝗢 𝗨 𝗡 𝗗    |    J Á R M Ű  F E L J E G Y Z É S  M E G T A L Á L V A      ")
    print(" __________________________________________________________________________________________________________")
    print(" ")
    print(f"𝗕𝗥𝗔𝗡𝗗                   MÁRKA:                                    {vehicle.get('brand')}")
    print(f"𝗠𝗢𝗗𝗘𝗟                   MODEL:                                    {vehicle.get('model')}")
    print(f"𝗧𝗬𝗣𝗘                     TÍPUS:                                    {vehicle.get('type')}")
    print(f"𝗙𝗨𝗘𝗟                 ÜZEMANYAG:                                    {vehicle.get('fuel')}")
    print(f"𝗔𝗦𝗣𝗜𝗥𝗔𝗧𝗜𝗢𝗡           ASPIRÁCIÓ:                                    {vehicle.get('boost')}")
    print(f"𝗩𝗜𝗡                   ALVÁZSZÁM:                                    {vehicle.get('vin')}")
    print(f"𝗗.𝗢.𝗠          GYÁRTÁS DÁTUMA:                                    {vehicle.get('dom')}")
    print(" ")
    print(f"𝗣𝗟𝗔𝗧𝗘                 RENDSZÁM:                                    {vehicle.get('plate')}")
    print(" ")
    print(f"𝗣𝗥𝗘𝗩. 𝗢𝗪𝗡𝗘𝗥  VOLT TULAJDONOS:                                    {vehicle.get('prevowner')}")
    print(f"𝗢𝗪𝗡𝗘𝗥             TULAJDONOS:                                     {vehicle.get('owner')}")
    print(f"𝗗.𝗢.𝗣         VÁSÁRLÁS DÁTUMA:                                     {vehicle.get('boost')}")
    print(" ")
    
    print(" __________________________________________________________________________________________________________")
    print(" ")
    print("                𝗦 𝗘 𝗥 𝗩 𝗜 𝗖 𝗘   𝗛 𝗜 𝗦 𝗧 𝗢 𝗥 𝗬     |     S Z E R V Í Z   T Ö R T É N E T                           ")
    print(" __________________________________________________________________________________________________________")

    for index, service in enumerate(vehicle.get("service_history", []), start=1):
        print(f"[{index}] {service['type']} | {service['date']}")
        print(f"𝗣𝗔𝗥𝗧𝗦              ALKATRÉSZEK: {', '.join(service['parts'])}")
        print(f"𝗥𝗘𝗔𝗦𝗢𝗡            JAVÍTÁS OKA: {service['reason']}")
        print(f"𝗣𝗘𝗥𝗙𝗢𝗥𝗠𝗘𝗗 𝗕𝗬       ELVÉGEZTE: {service['performed_by']}")
        print("-" * 50)

def search_vehicle():
    vehicles = load_vehicles()
    print(" __________________________________________________________________________________________________________")

    print("                                    𝗩𝗘𝗛𝗜𝗖𝗟𝗘 𝗦𝗘𝗔𝗥𝗖𝗛 | JÁRMŰ KERESÉSE                                               ")
    print(" __________________________________________________________________________________________________________")
    print("                                                                                                                  ")
    print("[ 𝗡𝗨𝗠 𝟭 ]    𝗕𝗔𝗦𝗘𝗗 𝗢𝗡 𝗩𝗜𝗡 | ALVÁZSZÁM ALAPJÁN")
    print("[ 𝗡𝗨𝗠 𝟮 ]    𝗕𝗔𝗦𝗘𝗗 𝗢𝗡 𝗟𝗜𝗖𝗘𝗡𝗦𝗘 𝗣𝗟𝗔𝗧𝗘 | RENDSZÁM ALAPJÁN")



    choice = input("> ")

    target = ""

    if choice == "1":
        target = input("𝗩𝗜𝗡 | ALVÁZSZÁM: ").strip().upper()

        for v in vehicles:
            if v.get("vin", "").upper() == target:
                vehicle_menu(v)
                return

    elif choice == "2":
        target = input("𝗟𝗜𝗖𝗘𝗡𝗦𝗘 𝗣𝗟𝗔𝗧𝗘 | RENDSZÁM: ").strip().upper()

        for v in vehicles:
            if v.get("plate", "").upper() == target:
                vehicle_menu(v)
                return

    print(" [ !!! ] 𝗩𝗘𝗛𝗜𝗖𝗟𝗘 𝗡𝗢𝗧 𝗙𝗢𝗨𝗡𝗗 | JÁRMŰ NEM TALÁLHATÓ [ !!! ] ")

def add_vehicle():
    clear()

    vehicle = {
        "brand": input("𝗕𝗥𝗔𝗡𝗗 | MÁRKA: "),
        "model": input("𝗠𝗢𝗗𝗘𝗟 | MODEL: "),
        "vin": input(" 𝗩𝗜𝗡 | ALVÁZSZÁM: "),
        "plate": input("𝗣𝗟𝗔𝗧𝗘 | RENDSZÁM: "),
        "owner": input("𝗢𝗪𝗡𝗘𝗥 | TULAJDONOS: "),
        "fuel": input("𝗙𝗨𝗘𝗟 | ÜZEMANYAG: "),
        "service_history": []
    }

    save_vehicle(vehicle)

    log_action(f"𝗥𝗘𝗚𝗜𝗦𝗧𝗘𝗥 𝗡𝗘𝗪 𝗩𝗘𝗛𝗜𝗖𝗟𝗘 | ÚJ JÁRMŰ REGISZTRÁCIÓJA: {vehicle['vin']}")

    print("𝗩𝗘𝗛𝗜𝗖𝗟𝗘 𝗔𝗗𝗗𝗘𝗗 | JÁRMŰ HOZZÁADVA")

def add_service(vehicle):
    clear()

    print("ADD SERVICE ENTRY")
    print("-" * 50)

    service = {
        "type": input("𝗦𝗘𝗥𝗩𝗜𝗖𝗘 𝗧𝗬𝗣𝗘 | SZERVÍZ TÍPUS: "),
        "date": input("𝗗𝗔𝗧𝗘 | DÁTUM: "),
        "parts": input("𝗣𝗔𝗥𝗧𝗦 | ALKATRÉSZEK: ").split(","),
        "reason": input("𝗥𝗘𝗔𝗦𝗢𝗡 | JAVÍTÁS OKA: "),
        "performed_by": input("𝗣𝗘𝗥𝗙𝗢𝗥𝗠𝗘𝗗 𝗕𝗬 | ELVÉGEZTE: ")
    }

    vehicle["service_history"].append(service)

    save_vehicle(vehicle)

    log_action(f"𝗦𝗘𝗥𝗩𝗜𝗖𝗘 𝗔𝗗𝗗𝗘𝗗 𝗧𝗢 | SZERVÍZ HOZZÁADVA {vehicle['vin']}")

    print("𝗦𝗘𝗥𝗩𝗜𝗖𝗘 𝗔𝗗𝗗𝗘𝗗 𝗦𝗨𝗖𝗖𝗘𝗦𝗙𝗨𝗟𝗟𝗬 | SZERVÍZ SIKERESEN HOZZÁADVA")

def vehicle_menu(vehicle):
    while True:
        clear()
        show_vehicle(vehicle)

        print()
        print("[ 𝗡𝗨𝗠 𝟭 ] 𝗔𝗗𝗗 𝗦𝗘𝗥𝗩𝗜𝗖𝗘 | SZERVÍZ HOZZÁADÁSA")
        print("[ 𝗡𝗨𝗠 2 ] 𝗥𝗘𝗧𝗨𝗥𝗡 | VISSZALÉPÉS")

        choice = input("> ")

        if choice == "1":
            add_service(vehicle)
            input("NYOMJA MEG A(Z) [ 𝗘𝗡𝗧𝗘𝗥 / 𝗥𝗘𝗧𝗨𝗥𝗡 ]  GOMBOT")

        elif choice == "2":
            return

def registry():
    clear()

    vehicles = load_vehicles()

    print("=" * 50)
    print(" 𝗩𝗘𝗛𝗜𝗖𝗟𝗘 𝗥𝗘𝗚𝗜𝗦𝗧𝗥𝗬 | JÁRMŰNYILVÁNTARTÁS")
    print("=" * 50)

    for v in vehicles:
        print(f"{v.get('brand')} {v.get('model')} | {v.get('plate')} | {v.get('vin')}")

    print()

def main():
    login()

    while True:
        clear()

        print(" __________________________________________________________________________________________________________")
        print("")
        print(" ███╗░░░███╗██╗░░░██╗██████╗░░█████╗░")
        print(" ████╗░████║╚██╗░██╔╝██╔══██╗██╔══██╗")
        print(" ██╔████╔██║░╚████╔╝░██████╔╝███████║            𝗜𝗡𝗧𝗘𝗥𝗡𝗔𝗟 𝗩𝗘𝗛𝗜𝗖𝗟𝗘 𝗥𝗘𝗚𝗜𝗦𝗧𝗘𝗥 𝗢𝗙 𝗧𝗛𝗘 𝗞𝗝𝗜 𝗖𝗢𝗠𝗣𝗔𝗡𝗬             ")
        print(" ██║╚██╔╝██║░░╚██╔╝░░██╔══██╗██╔══██║              A KJI. VÁLLALAT BELSŐ JÁRMŰNYILVÁNTARTÁSA               ")
        print(" ██║░╚═╝░██║░░░██║░░░██║░░██║██║░░██║")
        print(" ╚═╝░░░░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝")
        print(" __________________________________________________________________________________________________________")

        print()
        print("[ 𝗡𝗨𝗠 𝟭 ] 𝗩𝗘𝗛𝗜𝗖𝗟𝗘 𝗦𝗘𝗔𝗥𝗖𝗛 | JÁRMŰKERESÉS")
        print("[ 𝗡𝗨𝗠 𝟮 ] 𝗔𝗗𝗗 𝗩𝗘𝗛𝗜𝗖𝗟𝗘 | JÁRMŰ HOZZÁADÁSA")
        print("[ 𝗡𝗨𝗠 𝟯 ] 𝗥𝗘𝗚𝗜𝗦𝗧𝗥𝗬 | NYILVÁNTARTÁS")
        print(" ")
        print("[ 𝗡𝗨𝗠 𝟬 ] 𝗘𝗫𝗜𝗧 | KILÉPÉS")
        print()

        choice = input("> ")

        if choice == "1":
            clear()
            search_vehicle()
            input("NYOMJA MEG A(Z) [ 𝗘𝗡𝗧𝗘𝗥 / 𝗥𝗘𝗧𝗨𝗥𝗡 ]  GOMBOT")

        elif choice == "2":
            add_vehicle()
            input("NYOMJA MEG A(Z) [ 𝗘𝗡𝗧𝗘𝗥 / 𝗥𝗘𝗧𝗨𝗥𝗡 ]  GOMBOT")

        elif choice == "3":
            registry()
            input("NYOMJA MEG A(Z) [ 𝗘𝗡𝗧𝗘𝗥 / 𝗥𝗘𝗧𝗨𝗥𝗡 ]  GOMBOT")

        elif choice == "0":
            break

if __name__ == "__main__":
    main()
