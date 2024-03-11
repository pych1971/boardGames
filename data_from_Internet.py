import json
import xml.etree.ElementTree
import urllib.request


class BoardGameFromInternet:
    def __init__(self, game):
        self.game_Tesera = game
        with urllib.request.urlopen(f"https://api.tesera.ru/games/{self.game_Tesera}") as game_Tesera:
            self.game_JSON_Tesera = json.load(game_Tesera)
            self.game_BGG = self.game_JSON_Tesera["game"]["bggId"]

            self.game_Tesera_title = self.game_JSON_Tesera["game"]["title"]
            self.game_Tesera_average_rating = self.game_JSON_Tesera["game"]["ratingUser"]
            self.game_Tesera_rating = self.game_JSON_Tesera["game"]["n10Rating"]

        with urllib.request.urlopen(
                f"https://boardgamegeek.com/xmlapi2/thing?id={self.game_BGG}&stats=1") as game_BGG_XML:
            self.tree_XML_BGG = xml.etree.ElementTree.parse(game_BGG_XML)

            self.game_BGG_name = self.tree_XML_BGG.find('.//item/*[@type="primary"]').get('value')
            self.game_BGG_average_rating = float(self.tree_XML_BGG.find('.//*ratings/average').get('value'))
            self.game_BGG_geek_rating = float(self.tree_XML_BGG.find('.//*ratings/bayesaverage').get('value'))
            self.game_BGG_rank = int(self.tree_XML_BGG.find(".//*ratings/ranks/*[@type='subtype']").get('value'))
            self.game_BGG_weight = float(self.tree_XML_BGG.find('.//*ratings/averageweight').get('value'))

    def game_from_Tesera_and_BGG(self):
        return self.game_Tesera_title, self.game_Tesera_average_rating, self.game_Tesera_rating, self.game_BGG_name, self.game_BGG_average_rating, self.game_BGG_geek_rating, self.game_BGG_rank, self.game_BGG_weight
