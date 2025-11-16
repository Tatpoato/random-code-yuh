import requests
from datetime import datetime

def format_iso_time(iso_string):
    """Convert ISO 8601 time to just HH:MM format."""
    dt = datetime.fromisoformat(iso_string)
    return dt.strftime("%H:%M")

will = input("Do you want to see the weather? (yes/no): ").strip().lower()

if will == "yes":
    url = (
        ""
    )
    headers = {"Accept": "application/json"}
    response = requests.get(url, headers=headers)

# REMEMBER TO USE AN OPEN METEO THINGY WITH YOUR OWN CORDINATES FOR THIS ONE GO TO https://open-meteo.com/en/docs AND CONFIGURE THEN PRINT IT AT LINE 13 (inside the quotes ofc) (for the things you select just select everything under daily weather variables and hourly weather variables)


    if response.ok:
        data = response.json()

        daily = data.get("daily", {})
        date = daily.get("time", ["N/A"])[0]
        uv_index_max = daily.get("uv_index_max", ["N/A"])[0]
        uv_clear_sky_max = daily.get("uv_index_clear_sky_max", ["N/A"])[0]
        sunrise_raw = daily.get("sunrise", ["N/A"])[0]
        sunset_raw = daily.get("sunset", ["N/A"])[0]

 
        hourly = data.get("hourly", {})
        times = hourly.get("time", [])
        temps = hourly.get("temperature_2m", [])

    
        if temps and times:
            min_temp = min(temps)
            max_temp = max(temps)
            min_time = format_iso_time(times[temps.index(min_temp)])
            max_time = format_iso_time(times[temps.index(max_temp)])
        else:
            min_temp = max_temp = min_time = max_time = "N/A"

        print(f"\nWeather for {date}:")
        print(f"- Max UV Index: {uv_index_max}")
        print(f"- Max UV Index (clear sky): {uv_clear_sky_max}")
        print(f"- Sunrise: {format_iso_time(sunrise_raw)}")
        print(f"- Sunset: {format_iso_time(sunset_raw)}")
        print(f"- Min Temperature: {min_temp}°C at {min_time}")
        print(f"- Max Temperature: {max_temp}°C at {max_time}")

        show_hourly = input("\nDo you want to see hourly temperatures? (yes/no): ").strip().lower()
        if show_hourly == "yes":
            print("\nHourly Temperatures (°C):")
            for time, temp in zip(times, temps):
                print(f"{format_iso_time(time)} - {temp}°C")
    else:
        print("Failed to retrieve weather data. Please try again later.")
elif will == "no":
    print("Hey, that is mean! The whole code is about the weather.")
else:
    print("Haha, you missed your chance to see the weather!")
# not my code at all btw
