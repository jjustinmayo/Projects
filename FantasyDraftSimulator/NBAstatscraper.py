
from bs4 import BeautifulSoup
import requests
import os
import json
from dotenv import load_dotenv
from supabase import create_client, Client



page_to_scrape = requests.get("https://www.basketball-reference.com/leagues/NBA_2025_per_game.html")

soup = BeautifulSoup(page_to_scrape.text, "html.parser")

names = soup.find("td", attrs ={"data-stat": "name_display"})
positions = soup.find("td", attrs ={"data-stat": "pos"})
GP = soup.find("td", attrs ={"data-stat": "games"})
fg_per_g = soup.find("td", attrs ={"data-stat": "fg_per_g"})
fga_per_g = soup.find("td", attrs ={"data-stat": "fga_per_g"})
fg_pct = soup.find("td", attrs ={"data-stat": "fg_pct"})
fg3_per_g = soup.find("td", attrs ={"data-stat": "fg3_per_g"})
fg3a_per_g = soup.find("td", attrs ={"data-stat": "fg3a_per_g"})
fg3_pct = soup.find("td", attrs ={"data-stat": "fg3_pct"})
ft_per_g = soup.find("td", attrs ={"data-stat": "ft_per_g"})
fta_per_g = soup.find("td", attrs ={"data-stat": "fta_per_g"})
ft_pct = soup.find("td", attrs ={"data-stat": "ft_pct"})
trb_per_g = soup.find("td", attrs ={"data-stat": "trb_per_g"})
ast_per_g = soup.find("td", attrs ={"data-stat": "ast_per_g"})
stl_per_g = soup.find("td", attrs ={"data-stat": "stl_per_g"})
blk_per_g = soup.find("td", attrs ={"data-stat": "blk_per_g"})
tov_per_g = soup.find("td", attrs ={"data-stat": "tov_per_g"})
pts_per_g = soup.find("td", attrs ={"data-stat": "pts_per_g"})



def populate_nba_stats(supabase):
    main_list = {}
    for n,p,gp,fg,fga,fgp,fg3,fg3a,fg3p,ft,fta,ftp,trb,ast,stl,blk,tov,pts in zip(names,positions,GP,fg_per_g,fga_per_g,fg_pct,fg3_per_g,fg3a_per_g,fg3_pct,ft_per_g,fta_per_g,ft_pct,trb_per_g,ast_per_g,stl_per_g,blk_per_g,tov_per_g,pts_per_g):
        main_list["name"] = (n.text)
        main_list["position"] = (p.text)
        main_list["GP"] = (gp.text)
        main_list["fg_per_g"] = (fg.text)
        main_list["fga_per_g"] = (fga.text)
        main_list["fg_pct"] = (fgp.text)
        main_list["fg3_per_g"] = (fg3.text)
        main_list["fg3a_per_g"] = (fg3a.text)
        main_list["fg3_pct"] = (fg3p.text)
        main_list["ft_per_g"] = (ft.text)
        main_list["fta_per_g"] = (fta.text)
        main_list["ft_pct"] = (ftp.text)
        main_list["trb_per_g"] = (trb.text)
        main_list["ast_per_g"] = (ast.text)
        main_list["stl_per_g"] = (stl.text)
        main_list["blk_per_g"] = (blk.text)
        main_list["tov_per_g"] = (tov.text)
        main_list["pts_per_g"] = (pts.text)
    data = supabase.table('NBAStats').insert(main_list).execute()
    


def main():
    load_dotenv()
    url: str = os.environ.get("SUPABASE_URL")
    key: str = os.environ.get("SUPABASE_KEY")
    supabase: Client = create_client(url, key)
    populate_nba_stats(supabase)

main()
