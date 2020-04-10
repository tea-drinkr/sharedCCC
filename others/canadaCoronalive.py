from bs4 import BeautifulSoup as bs
from color import Colortext

import requests

"python3 -m pip install -r others/requirements.txt"
# run this command

color = Colortext()
r = requests.get("https://www.worldometers.info/coronavirus/country/canada/")
s = bs(r.text, "html.parser")
data = s.find_all('div', class_ = "maincounter-number")

print("Total cases     : " + color.YELLOW + data[0].text.strip() + color.ENDC)
print("Total death     : " + color.RED + data[1].text.strip() + color.ENDC)
print("Total recovered : " + color.GREEN + data[2].text.strip() + color.ENDC)
