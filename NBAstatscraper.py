
from bs4 import BeautifulSoup
import requests


page_to_scrape = requests.get("https://www.basketball-reference.com/leagues/NBA_2025_per_game.html")

soup = BeautifulSoup(page_to_scrape.text, "html.parser")

#names = soup.find_all("td", attrs ={"data-stat": "name_display"})
stop_at = soup.find("div", class_ ="placeholder")
names = stop_at.find_all_previous("td", attrs ={"data-stat": "name_display"})


for name in names:
    anchor = name.find("a")        # Try to find the <a> tag inside the <td>
    if anchor:                     # Only proceed if an <a> tag is actually found
        print(anchor.text)       # Safely access and print the text (e.g., player name)

