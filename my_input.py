import requests

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
        print(f'Download erfolgreich. Inhalt wurde in {filename} gespeichert.')
    else:
        print(f'Fehler beim Herunterladen. Statuscode: {response.status_code}')

# Setze deine Werte hier ein
year = 2023
day = 1
session = '<FILL_HERE>'
user_agent = 'https://github.com/Pitma/AdventOfCode/blob/main/get_input.py by patrickmainka@gmail.com'
output_filename = 'input.txt'

# Funktion aufrufen
download_and_save_input(year, day, session, user_agent, output_filename)
