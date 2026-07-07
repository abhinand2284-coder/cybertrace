import pyfiglet

from colorama import Fore, Style, init

from modules.ip_tracker import ip_lookup
from modules.phone_tracker import phone_lookup
from modules.username_tracker import username_lookup
from modules.website_scanner import website_lookup

import time

print(Fore.GREEN + "\nInitializing CyberTrace", end="")

for i in range(5):
    print(".", end="", flush=True)
    time.sleep(0.3)
    
print("\n")    

# Start colorama
init()

# Banner
banner = pyfiglet.figlet_format("CyberTrace", font="slant")

print(Fore.RED + banner)
print(Fore.GREEN + "=" * 55)
print(Fore.CYAN + """	CYBERTRACE - MULTI PURPOSE OSINT FRAMEWORK
        
 	Developer : Abhinand M R
        Platform  : Kali Linux
""")
print(Fore.GREEN + "=" * 55)

while True:

    print(Fore.YELLOW + """  
[1] IP Address Tracker
[2] Phone Number Tracker
[3] Username Tracker
[4] Website Info Scanner""")
    print(Fore.RED+"[5] Exit")

    choice = input(Fore.WHITE + "Select Option >> ")

    if choice == "1":
        ip_lookup()

    elif choice == "2":
        phone_lookup()

    elif choice == "3":
        username = input("Enter Username: ")
        username_lookup(username)
        
    elif choice == "4":
    	website_lookup()
    	
    elif choice == "5":
        print(Fore.RED + "\nExiting CyberTrace.....")
        break
        	
    else:
        print(Fore.RED + "Invalid Choice!")

print(Style.RESET_ALL)
