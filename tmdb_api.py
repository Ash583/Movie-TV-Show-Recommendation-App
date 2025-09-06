import requests

API_KEY = "put_your_tmdb_key_here"
BASE_URL = "https://api.themoviedb.org/3"

def search_movies(query):
    url = BASE_URL + "/search/multi"
    params = {
        "api_key": API_KEY,
        "query": query
    }
    r = requests.get(url, params=params)
    data = r.json()
    return data.get("results", [])
