import requests
import time
from datetime import datetime, timedelta
from pytz import timezone, utc

# Function to get current time EST
def est_now() -> datetime:
    return datetime.now(tz=utc).astimezone(timezone("US/Eastern"))

# Funktion zum Herunterladen des Inhalts und Speichern in einer Datei
def download_and_save_input(year, day, session, user_agent, filename):
    url = f'https://adventofcode.com/{year}/day/{day}/input'
    headers = {
        'Cookie': f'session={session}',
        'User-Agent': user_agent
    }
  
    # GET-Anfrage senden
    response = requests.get(url, headers=headers)

    # Überprüfen, ob die Anfrage erfolgreich war (Statuscode 200)
    if response.status_code == 200:
        # Inhalt in Datei schreiben
        with open(filename, 'w') as file:
            file.write(response.text)
        with open(f'{year}/day{str(day).zfill(2)}/sample.txt', 'w') as file:
            file.write('')
        print(f'Download erfolgreich. Inhalt wurde in {filename} gespeichert.')
    else:
        print(f'Fehler beim Herunterladen. Statuscode: {response.status_code}')

    
with open(".token") as token:
    cookies =  token.read().strip()
    
# Setze deine Werte hier ein
year = 2024
day = 3
session = cookies
user_agent = 'https://github.com/Pitma/AdventOfCode/blob/main/get_input.py by patrickmainka@gmail.com'
output_filename = f'{year}/day{str(day).zfill(2)}/input.txt'

# Funktion aufrufen
download_and_save_input(year, day, session, user_agent, output_filename)
