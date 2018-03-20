import pyowm
import getpass

#This is my first project on Python

owm = pyowm.OWM("3b70be4a67173929ceb874ebfcfd5497",language='ua')

try:
    if owm.is_API_online():
        print("API OK")
except:
    print("API недоступний, виходимо...")
    exit(1)

user = getpass.getuser()
print(str("Привіт, {username}! Глянемо на погоду?").format(username=user),end="\n\n")

city = input("Вкажи місто:\t")

try:
    observation = owm.weather_at_place(city)
except:
    print("Неправильне місто або якась інша помилка! Виходимо...")
    exit(2)

weather = observation.get_weather()
gettemp = weather.get_temperature('celsius')
status = weather.get_status()
humidity = weather.get_humidity()

if status == "Clear":
    status = "чисте небо"
elif status == "Clouds":
    status = "хмари"
elif status == "Rain":
    status = "дощ"
elif status == "Snow":
    status = "сніг"
elif status == "Mist":
    status = "туман"
elif status == "Thunderstorm":
    status = "гроза"

print(str("\nЗараз у місті {city} температура {temp} градусів за Цельсієм, відносна вологість {humidity}% та {status}.").format(city=city,temp=round(gettemp["temp"]),humidity=humidity,status=status))
print(str("Мінімальна температура сьогодні: {tempmin}, максимальна: {tempmax}.").format(tempmin=gettemp["temp_min"],tempmax=gettemp["temp_max"]))

input("\n\nEnter для виходу.")