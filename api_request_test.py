import requests
import json

base_url = 'http://127.0.0.1:5000/all_reviews'

params = {'max_records': 10, 'sort': 'DESC'}
# body = {'book': 'The Alchemist', 'rating': 7.2, 'notes': 'A classic!'}

response = requests.get(base_url, params=params)

print(response.json())