# importing the requests library
import requests

URL = "https://catfact.ninja/fact?max_length=20"

api_data = requests.get(url=URL)


if api_data.status_code == 200:
    try:
        json_data = api_data.json()
    except Exception:
        exit('ERROR: the API_DATA provided ("{}") is not working'.format(api_data))
else:
    print("Error with API")

print(f"::set-output name=cat_fact::{json_data['fact']}")
