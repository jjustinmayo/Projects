
from bs4 import BeautifulSoup
import requests
import csv
import os
import json
from supabase import create_client, Client


page_to_scrape = requests.get("https://www.basketball-reference.com/leagues/NBA_2025_per_game.html")

soup = BeautifulSoup(page_to_scrape.text, "html.parser")

#names = soup.find_all("td", attrs ={"data-stat": "name_display"})
stop_at = soup.find("div", class_ ="placeholder")
names = stop_at.find_all_previous("td", attrs ={"data-stat": "name_display"})
positions = stop_at.find_all_previous("td", attrs ={"data-stat": "pos"})
GP = stop_at.find_all_previous("td", attrs ={"data-stat": "games"})
fg_per_g = stop_at.find_all_previous("td", attrs ={"data-stat": "fg_per_g"})
fga_per_g = stop_at.find_all_previous("td", attrs ={"data-stat": "fga_per_g"})
fg_pct = stop_at.find_all_previous("td", attrs ={"data-stat": "fg_pct"})
fg3_per_g = stop_at.find_all_previous("td", attrs ={"data-stat": "fg3_per_g"})
fg3a_per_g = stop_at.find_all_previous("td", attrs ={"data-stat": "fg3a_per_g"})
fg3_pct = stop_at.find_all_previous("td", attrs ={"data-stat": "fg3_pct"})
ft_per_g = stop_at.find_all_previous("td", attrs ={"data-stat": "ft_per_g"})
fta_per_g = stop_at.find_all_previous("td", attrs ={"data-stat": "fta_per_g"})
ft_pct = stop_at.find_all_previous("td", attrs ={"data-stat": "ft_pct"})
trb_per_g = stop_at.find_all_previous("td", attrs ={"data-stat": "trb_per_g"})
ast_per_g = stop_at.find_all_previous("td", attrs ={"data-stat": "ast_per_g"})
stl_per_g = stop_at.find_all_previous("td", attrs ={"data-stat": "stl_per_g"})
blk_per_g = stop_at.find_all_previous("td", attrs ={"data-stat": "blk_per_g"})
tov_per_g = stop_at.find_all_previous("td", attrs ={"data-stat": "tov_per_g"})
pts_per_g = stop_at.find_all_previous("td", attrs ={"data-stat": "pts_per_g"})



#fg,fga,fgp,fg3,fg3a,fg3p,ft,fta,ftp,trb,ast,stl,blk,tov,pts in zip(names,positions,GP,fg_per_g,fga_per_g,fg_pct,fg3_per_g,fg3a_per_g,fg3_pct,ft_per_g,fta_per_g,ft_pct,trb_per_g,ast_per_g,stl_per_g,blk_per_g,tov_per_g,pts_per_g):
 #   print(n.text +", "+p.text+", "+gp.text+", "+fg.text+", "+fga.text+", "+fgp.text+", "+fg3.text+", "+fg3a.text+", "+fg3p.text+", "+ft.text+", "+fta.text+", "+ftp.text+", "+trb.text+", "+ast.text+", "+stl.text+", "+blk.text+", "+tov.text+", "+pts.text)

#file = open("testfile.csv", "w", encoding="utf-8",newline='') 


with open("NBAstats.csv", "w", encoding="utf-8",newline='') as file:
    headers = ['name', 'position', 'GP', 'fg_per_g','fga_per_g', 'fg_pct','fg3_per_g','fg3a_per_g','fg3_pct','ft_per_g','fta_per_g',
               'ft_pct','trb_per_g','ast_per_g','stl_per_g','blk_per_g','tov_per_g','pts_per_g']
    writer = csv.DictWriter(file, fieldnames=headers)
    writer.writeheader()
    for n,p,gp,fg,fga,fgp,fg3,fg3a,fg3p,ft,fta,ftp,trb,ast,stl,blk,tov,pts, in zip(names,positions,GP,fg_per_g,fga_per_g,fg_pct,fg3_per_g,fg3a_per_g,fg3_pct,ft_per_g,fta_per_g,ft_pct,trb_per_g,ast_per_g,stl_per_g,blk_per_g,tov_per_g,pts_per_g):
        writer.writerow({'name': n.text,'position': p.text,'GP': gp.text,'fg_per_g': fg.text,'fga_per_g': fga.text,'fg_pct': fgp.text,'fg3_per_g': fg3.text,'fg3a_per_g': fg3a.text,
                         'fg3_pct': fg3p.text,'ft_per_g':ft.text,'fta_per_g':fta.text,'ft_pct':ftp.text,'trb_per_g':trb.text,'ast_per_g':ast.text,'stl_per_g':stl.text,
                         'blk_per_g':blk.text,'tov_per_g':tov.text,'pts_per_g':pts.text})

