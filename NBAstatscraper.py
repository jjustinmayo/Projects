
from basketball_reference_scraper.teams import get_roster, get_team_stats  #instructions on how to use
import pandas as pd
import requests

# API documentation: https://github.com/vishaalagartha/basketball_reference_scraper/blob/master/API.md

#print(get_roster('TOR',2019))
print(get_team_stats('TOR', 2019, data_format='TOTALS'))