import socket
import requests

def website_lookup():

    site = input("Enter Website (example.com): ")

    try:

        ip = socket.gethostbyname(site)

        print("\n[WEBSITE INFORMATION]")
        print("IP Address :", ip)

        response = requests.get("http://" + site)

        print("Status Code:", response.status_code)

        print("\n[HEADERS]")

        for key, value in response.headers.items():
            print(f"{key} : {value}")

    except:
        print("Unable to scan website")
