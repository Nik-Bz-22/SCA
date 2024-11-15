import requests


def validate_breeds(breeds):
    resp = requests.get("https://api.thecatapi.com/v1/breeds")
    if resp.status_code != 200:
        raise Exception("Bad request to API")
    cats_data = resp.json()

    for cat in cats_data:
        if cat["name"] == breeds:
            return True
    return False