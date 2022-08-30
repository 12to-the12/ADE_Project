import requests
response = requests.get('https://api.ipgeolocation.io/ipgeo?apiKey=afbe97fad1804fcc98f1f1be3009d99f&ip=98.171.184.107')

print(response.content)