import requests

def username_lookup(username):
    sites = {
        "GitHub": f"https://github.com/{username}",
        "Instagram": f"https://www.instagram.com/{username}/",
        "Twitter": f"https://twitter.com/{username}"
    }

    print("\nChecking Username Availability...\n")

    for site, url in sites.items():
        response = requests.get(url)

        if response.status_code == 200:
            print(f"[FOUND] {site}: {url}")
        else:
            print(f"[NOT FOUND] {site}")
