import json
import urllib.request

numberOfGame = input()
# with urllib.request.urlopen("https://api.tesera.ru/games/1704184") as descentTesera:
with urllib.request.urlopen(f"https://api.tesera.ru/games/{numberOfGame}") as descentTesera:
    descentJsonTesera = json.load(descentTesera)
    print(descentJsonTesera["game"]["title"], descentJsonTesera["game"]["n10Rating"])
    bggDescent = descentJsonTesera["game"]["bggId"]

with urllib.request.urlopen(f"https://bgg-json.azurewebsites.net/thing/{bggDescent}") as descentBGG:
    descentJsonBGG = json.load(descentBGG)
    print(descentJsonBGG["name"], descentJsonBGG["averageRating"], descentJsonBGG["bggRating"], descentJsonBGG["rank"])
