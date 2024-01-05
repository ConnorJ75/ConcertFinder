import requests

apiKey = "https://api.seatgeek.com/2/events?client_id=Mzg0NzY2Mjl8MTcwMDcwNDA4NS45NjQ1Mzg&q={}"

response = requests.get(apiKey)

print(response.status_code)