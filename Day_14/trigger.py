import requests

ngrok_url = 'https://ddb9-180-210-220-44.ngrok.io'
endpoint = f'{ngrok_url}/box_office_mojo_scraper'

r = requests.post(endpoint, json={})
print(r.json()['fastapi'])