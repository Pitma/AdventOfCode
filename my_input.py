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
day = 2
session = '53616c7465645f5f7180b3b4802ccbff114b40e4329501dedabaec68fe2e499d2bee8fe97706f2a67c2288084d6386d7e681d10862ecd54147b960d270e0f1e5'
user_agent = 'https://github.com/Pitma/AdventOfCode/blob/main/get_input.py by patrickmainka@gmail.com'
output_filename = 'input.txt'

# Funktion aufrufen
download_and_save_input(year, day, session, user_agent, output_filename)
