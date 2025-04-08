import requests

# update const data from ddragon

DDRAGON_VERSION = "15.7.1"


def update_champions():
    url = f"https://ddragon.leagueoflegends.com/cdn/{DDRAGON_VERSION}/data/en_US/champion.json"
    response = requests.get(url).json()
    champions = response["data"]
    with open("./riot/constants/champions.py", "w") as file:
        for key in champions:
            champion = champions[key]
            file.write(f'{champion["id"]} = "{champion["key"]}"' + "\n")


update_champions()
