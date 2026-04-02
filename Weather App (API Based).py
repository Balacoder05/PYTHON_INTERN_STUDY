import requests

city = input("Enter city: ")
api_key = "your_api_key"

url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
data = requests.get(url).json()

print("Temperature:", data['main']['temp'])