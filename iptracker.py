import requests
import folium
import webbrowser

def ip_lookup():

    ip = input("Enter IP Address: ")

    url = f"http://ip-api.com/json/{ip}"

    response = requests.get(url)
    data = response.json()

    country = data.get("country")
    city = data.get("city")
    isp = data.get("isp")
    lat = data.get("lat")
    lon = data.get("lon")

    print("\n[IP INFORMATION]")
    print("Country :", country)
    print("City    :", city)
    print("ISP     :", isp)
    print("Latitude :", lat)
    print("Longitude:", lon)

    # Save results
    with open("results.txt", "a") as file:

        file.write(f"\nIP: {ip}\n")
        file.write(f"Country: {country}\n")
        file.write(f"City: {city}\n")
        file.write(f"ISP: {isp}\n")
        file.write(f"Latitude: {lat}\n")
        file.write(f"Longitude: {lon}\n")
        file.write("-" * 40 + "\n")

    print("\nResults saved to results.txt")

    # Create map
    map = folium.Map(location=[lat, lon], zoom_start=10)

    folium.Marker(
        [lat, lon],
        popup=f"{city}, {country}"
    ).add_to(map)

    map.save("map.html")
    
    print("\nOpen map manually using:")
    print("firefox map.html")
