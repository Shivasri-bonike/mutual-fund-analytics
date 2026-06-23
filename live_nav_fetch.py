import requests

url = "https://api.mfapi.in/mf/125497"

response = requests.get(url)

print("Status Code:", response.status_code)

data = response.json()

print("Fund Name:", data["meta"]["scheme_name"])
print("Latest NAV:", data["data"][0]["nav"])
print("Date:", data["data"][0]["date"])