import requests

api_key = "a7d08052f1a08e9555931adc06a1a1c9"

# HTTP requests

# What's our endpoint (or a url)

# What is the HTTP method that we need?

"""
Endpoint 
/movie/{movie_id}
https://api.themoviedb.org/3/movie/550?api_key=a7d08052f1a08e9555931adc06a1a1c9

"""
movie_id = 500
api_version = 3
api_base_url = f"https://api.themoviedb.org/{api_version}"
endpoint_path = f"/movie/{movie_id}"
endpoint = f"{api_base_url}{endpoint_path}?api_key={api_key}"
r = requests.get(endpoint) #json={"api_key":api_key})
print(r.status_code)
print(r.text)