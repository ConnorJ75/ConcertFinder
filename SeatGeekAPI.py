import requests

url = "https://api.seatgeek.com/2/events?client_id=Mzg0NzY2Mjl8MTcwMDcwNDA4NS45NjQ1Mzg&q={}"

response = requests.get(url)

print(response.status_code)