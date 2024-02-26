import json
import urllib.request


class BoardGameFromInternet:
    def __init__(self, number):
        self.number = number

    def game_from_Tesera(self):
        with urllib.request.urlopen(f"https://api.tesera.ru/games/{self.number}") as game_Tesera:
            self.game_JSON_tesera = json.load(game_Tesera)
            self.game_BGG = self.game_JSON_tesera["game"]["bggId"]
            print(self.game_JSON_tesera["game"]["title"], self.game_JSON_tesera["game"]["n10Rating"])

    def game_from_Tesera(self):
        with urllib.request.urlopen(f"https://bgg-json.azurewebsites.net/thing/{self.game_BGG}") as game_BGG:
            self.game_JSON_BGG = json.load(game_BGG)
            print(self.game_JSON_BGG["name"], self.game_JSON_BGG["averageRating"], self.game_JSON_BGG["bggRating"],
                  self.game_JSON_BGG["rank"])
