from email import header
import requests

api_key = "a7d08052f1a08e9555931adc06a1a1c9"
api_key_v4 = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJhN2QwODA1MmYxYTA4ZTk1NTU5MzFhZGMwNmExYTFjOSIsInN1YiI6IjYyNDA0YzkyNDU3NjVkMDA5NDRiMThkMCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.SKNZJSJRuKYy-UjZoP3MCH669VDogRYFlrDroq3KUvM"

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
# r = requests.get(endpoint) #json={"api_key":api_key})
# print(r.status_code)
# print(r.text)

# Using v4
movie_id = 501
api_version = 4
api_base_url = f"https://api.themoviedb.org/{api_version}"
endpoint_path = f"/movie/{movie_id}"
endpoint = f"{api_base_url}{endpoint_path}"
headers = {
 'Authorization': f'Bearer {api_key_v4}',
 'Content-Type': 'application/json;charset=utf-8'
}
r = requests.get(endpoint, headers=headers) #json={"api_key":api_key})
print(r.status_code)
print(r.text)