from datetime import datetime
import requests

tokyo_code = 130000
api_url = f"https://www.jma.go.jp/bosai/forecast/data/forecast/{tokyo_code}.json"
response = requests.get(api_url).json()
area_name = response[0]["timeSeries"][0]["areas"][0]["area"]["name"]
time_series = response[0]["timeSeries"][0]["timeDefines"]
weather_data = response[0]["timeSeries"][0]["areas"][0]["weathers"]

weathers = f"{area_name}の{len(time_series)}日間の天気予報\n"
for time, weather in zip(time_series, weather_data):
    time = datetime.strptime(time, "%Y-%m-%dT%H:%M:%S+09:00")
    weathers += f"　{time}の天気は{weather}です。\n"

detail_api_url = f"https://www.jma.go.jp/bosai/forecast/data/overview_forecast/{tokyo_code}.json"
weather_data = requests.get(detail_api_url).json()
weathers += "\n"
weathers += weather_data["text"]

print(weathers)
