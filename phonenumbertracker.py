import phonenumbers
from phonenumbers import geocoder, carrier

def phone_lookup():
    number = input("Enter Phone Number with country code: ")

    try:
        parsed = phonenumbers.parse(number)

        print("Location :", geocoder.description_for_number(parsed, "en"))
        print("Carrier  :", carrier.name_for_number(parsed, "en"))
        print("Valid    :", phonenumbers.is_valid_number(parsed))

    except:
        print("Invalid Number")
