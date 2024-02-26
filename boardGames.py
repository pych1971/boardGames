import json
import urllib.request

number_of_game = input()
with urllib.request.urlopen(f"https://api.tesera.ru/games/{number_of_game}") as game_Tesera:
    game_JSON_Tesera = json.load(game_Tesera)
    print(game_JSON_Tesera["game"]["title"], game_JSON_Tesera["game"]["n10Rating"])
    game_BGG = game_JSON_Tesera["game"]["bggId"]

with urllib.request.urlopen(f"https://bgg-json.azurewebsites.net/thing/{game_BGG}") as descentBGG:
    game_JSON_BGG = json.load(descentBGG)
    print(game_JSON_BGG["name"], game_JSON_BGG["averageRating"], game_JSON_BGG["bggRating"], game_JSON_BGG["rank"])
