
from bs4 import BeautifulSoup
import requests
import os
import json
from dotenv import load_dotenv
from supabase import create_client, Client



page_to_scrape = requests.get("https://www.basketball-reference.com/leagues/NBA_2025_per_game.html")

soup = BeautifulSoup(page_to_scrape.text, "html.parser")

names = soup.find_all("td", attrs ={"data-stat": "name_display"})
positions = soup.find_all("td", attrs ={"data-stat": "pos"})
GP = soup.find_all("td", attrs ={"data-stat": "games"})
fg_per_g = soup.find_all("td", attrs ={"data-stat": "fg_per_g"})
fga_per_g = soup.find_all("td", attrs ={"data-stat": "fga_per_g"})
fg_pct = soup.find_all("td", attrs ={"data-stat": "fg_pct"})
fg3_per_g = soup.find_all("td", attrs ={"data-stat": "fg3_per_g"})
fg3a_per_g = soup.find_all("td", attrs ={"data-stat": "fg3a_per_g"})
fg3_pct = soup.find_all("td", attrs ={"data-stat": "fg3_pct"})
ft_per_g = soup.find_all("td", attrs ={"data-stat": "ft_per_g"})
fta_per_g = soup.find_all("td", attrs ={"data-stat": "fta_per_g"})
ft_pct = soup.find_all("td", attrs ={"data-stat": "ft_pct"})
trb_per_g = soup.find_all("td", attrs ={"data-stat": "trb_per_g"})
ast_per_g = soup.find_all("td", attrs ={"data-stat": "ast_per_g"})
stl_per_g = soup.find_all("td", attrs ={"data-stat": "stl_per_g"})
blk_per_g = soup.find_all("td", attrs ={"data-stat": "blk_per_g"})
tov_per_g = soup.find_all("td", attrs ={"data-stat": "tov_per_g"})
pts_per_g = soup.find_all("td", attrs ={"data-stat": "pts_per_g"})




NBAdict = []
for n,p,gp,fg,fga,fgp,fg3,fg3a,fg3p,ft,fta,ftp,trb,ast,stl,blk,tov,pts in zip(names,positions,GP,fg_per_g,fga_per_g,fg_pct,fg3_per_g,fg3a_per_g,fg3_pct,ft_per_g,fta_per_g,ft_pct,trb_per_g,ast_per_g,stl_per_g,blk_per_g,tov_per_g,pts_per_g):
    main_list = {}
    main_list["name"] = (n.get_text())
    main_list["position"] = (p.get_text())
    main_list["GP"] = (gp.get_text())
    main_list["fg_per_g"] = (fg.get_text())
    main_list["fga_per_g"] = (fga.get_text())
    main_list["fg_pct"] = (fgp.get_text())
    main_list["fg3_per_g"] = (fg3.get_text())
    main_list["fg3a_per_g"] = (fg3a.get_text())
    main_list["fg3_pct"] = (fg3p.get_text())
    main_list["ft_per_g"] = (ft.get_text())
    main_list["fta_per_g"] = (fta.get_text())
    main_list["ft_pct"] = (ftp.get_text())
    main_list["trb_per_g"] = (trb.get_text())
    main_list["ast_per_g"] = (ast.get_text())
    main_list["stl_per_g"] = (stl.get_text())
    main_list["blk_per_g"] = (blk.get_text())
    main_list["tov_per_g"] = (tov.get_text())
    main_list["pts_per_g"] = (pts.get_text())
    NBAdict.append(main_list)

    
unique_players = []
seen_names = set()

def populate_nba_stats(supabase):
    for player in NBAdict:  
        name = player["name"]
        if name not in seen_names:
            unique_players.append(player)
            seen_names.add(name)
    data = supabase.table('NBAStats').insert(unique_players).execute()

def main():
    load_dotenv()
    url: str = os.environ.get("SUPABASE_URL")
    key: str = os.environ.get("SUPABASE_KEY")
    supabase: Client = create_client(url, key)
    populate_nba_stats(supabase)

main()
