import requests
from datetime import datetime

API_BASE_URL = "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22"

def get_weather_data():
    response = requests.get(API_BASE_URL)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch weather data. Please try again later.")
        return None

def get_weather_by_date(weather_data, date):
    for data in weather_data['list']:
        dt_txt = data['dt_txt']
        if date in dt_txt:
            return data['main']['temp']
    return None

def get_wind_speed_by_date(weather_data, date):
    for data in weather_data['list']:
        dt_txt = data['dt_txt']
        if date in dt_txt:
            return data['wind']['speed']
    return None

def get_pressure_by_date(weather_data, date):
    for data in weather_data['list']:
        dt_txt = data['dt_txt']
        if date in dt_txt:
            return data['main']['pressure']
    return None

def main():
    weather_data = get_weather_data()
    if not weather_data:
        return
    
    while True:
        print("\nOptions:")
        print("1. Get weather")
        print("2. Get Wind Speed")
        print("3. Get Pressure")
        print("0. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            date = input("Enter the date (YYYY-MM-DD): ")
            temp = get_weather_by_date(weather_data, date)
            if temp is not None:
                print(f"Temperature on {date}: {temp} °C")
            else:
                print("Data not found for the given date.")
        elif choice == 2:
            date = input("Enter the date (YYYY-MM-DD): ")
            wind_speed = get_wind_speed_by_date(weather_data, date)
            if wind_speed is not None:
                print(f"Wind Speed on {date}: {wind_speed} m/s")
            else:
                print("Data not found for the given date.")
        elif choice == 3:
            date = input("Enter the date (YYYY-MM-DD): ")
            pressure = get_pressure_by_date(weather_data, date)
            if pressure is not None:
                print(f"Pressure on {date}: {pressure} hPa")
            else:
                print("Data not found for the given date.")
        elif choice == 0:
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
