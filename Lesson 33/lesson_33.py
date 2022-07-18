import requests
from datetime import datetime
import smtplib

EMAIL = ''
PASS = ''

response = requests.get(url="http://api.open-notify.org/iss-now.json")
iss_data = response.json()

MY_LAT = -22.819501
MY_LONG = -43.387907

iss_longitude = float(iss_data['iss_position']['longitude'])
iss_latitude = float(iss_data['iss_position']['latitude'])

distance_lat = (+(iss_latitude) - +(MY_LAT))
distance_long = (+(iss_longitude) - +(MY_LONG))

parameters = {
    'lat': MY_LAT,
    'long': MY_LONG,
    'formatted': 0,
}

response = requests.get(
    "https://api.sunrise-sunset.org/json", params=parameters)
data = response.json()

sunrise = int(data['results']['sunrise'].split("T")[1].split(":")[0])
sunset = int(data['results']['sunset'].split("T")[1].split(":")[0])

time_now = datetime.now()
now_hour = int(time_now.hour)

if distance_lat >= 5 and distance_lat <= 5:
    if distance_long >= 5 and distance_long <= 5:
        if now_hour >= sunset or now_hour <= sunrise:
            with smtplib.SMTP("smtp.office365.com") as connection:
                connection.starttls()
                connection.login(EMAIL, PASS)
                connection.sendmail(from_addr=EMAIL, to_addrs='williamgabriel@outlook.com',
                                    msg=f"Subject:Look Up\n\nThe ISS is near in your sky, and it's dark by now!")
