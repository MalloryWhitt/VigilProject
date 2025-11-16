import requests

base_url = "https://lda.senate.gov/api/v1/filings/"
API_KEY = "113c1022dade366197348afd43ec391d7c746e22"

def fetch_lobbying_data(year):
    params = {'filings_year': year, 'api_key': API_KEY}
    """
    Fetch lobbying data from the Senate LDA API.

    Args:
        endpoint (str): The API endpoint to fetch data from.
        params (dict, optional): Query parameters for the API request.

    Returns:
        dict: The JSON response from the API.
    """
    response = requests.get(base_url, params=params)
    response.raise_for_status()  # Raise an error for bad responses
    return response.json()
    
data = fetch_lobbying_data(2023)
print(data)



