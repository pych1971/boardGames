import json
import xml.etree.ElementTree
import urllib.request


class BoardGameFromInternet:
    def __init__(self, game):
        self.game_Tesera = game
        with urllib.request.urlopen(f"https://api.tesera.ru/games/{self.game_Tesera}") as game_Tesera:
            self.game_JSON_Tesera = json.load(game_Tesera)
            self.game_BGG = self.game_JSON_Tesera["game"]["bggId"]
        with urllib.request.urlopen(f"https://bgg-json.azurewebsites.net/thing/{self.game_BGG}") as game_BGG:
            self.game_JSON_BGG = json.load(game_BGG)
        with urllib.request.urlopen(
                f"https://boardgamegeek.com/xmlapi2/thing?id={self.game_BGG}&stats=1") as game_BGG_XML:
            tree = xml.etree.ElementTree.parse(game_BGG_XML)
            root = tree.getroot()
            weight = root.findall('.//*[@ranks]')
            print(weight)

    def game_from_Tesera_and_BGG(self):
        return self.game_JSON_Tesera["game"]["title"], self.game_JSON_Tesera["game"]["n10Rating"], self.game_JSON_BGG[
            "name"], self.game_JSON_BGG["averageRating"], self.game_JSON_BGG["bggRating"], self.game_JSON_BGG["rank"]
