import requests

API_KEY = "nnz8SGfzYuCPkuWtI4ZeYzg8ZxGNQRy0NkG7IJws"

def fetch_congress_data():
    url = "https://api.congress.gov/v3/congress"
    params = {
        "api_key": API_KEY,
        "format": "json",
    }

    resp = requests.get(url, params=params, timeout=15)
    resp.raise_for_status()          # crash loudly if bad key / params
    return resp.json()               # whole JSON response


data = fetch_congress_data()
congresses = data.get("congresses", [])

for c in congresses[:5]:
    print(f"{c['name']}  ({c['startYear']}–{c.get('endYear')})")
