import json
import xml.etree.ElementTree
import urllib.request


class BoardGameFromInternet:
    def __init__(self, game):
        self.game_Tesera = game
        with urllib.request.urlopen(f"https://api.tesera.ru/games/{self.game_Tesera}") as game_Tesera:
            self.game_JSON_Tesera = json.load(game_Tesera)
            self.game_BGG = self.game_JSON_Tesera["game"]["bggId"]
        with urllib.request.urlopen(
                f"https://boardgamegeek.com/xmlapi2/thing?id={self.game_BGG}&stats=1") as game_BGG_XML:
            self.tree = xml.etree.ElementTree.parse(game_BGG_XML)

    def game_from_Tesera_and_BGG(self):
        return (self.game_JSON_Tesera["game"]["title"],
                self.game_JSON_Tesera["game"]["n10Rating"],
                self.tree.find('.//item/name').get('value'),
                float(self.tree.find('.//*ratings/average').get('value')),
                float(self.tree.find('.//*ratings/bayesaverage').get('value')),
                int(self.tree.find(".//*ratings/ranks/*[@type='subtype']").get('value')),
                float(self.tree.find('.//*ratings/averageweight').get('value')))
