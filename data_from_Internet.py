import json
import xml.etree.ElementTree
import urllib.request


class BoardGameFromInternet:
    def __init__(self, game):
        self.tesera_id = game
        with urllib.request.urlopen(f"https://api.tesera.ru/games/{self.tesera_id}") as game_tesera_json:
            self.game_tesera = json.load(game_tesera_json)
            self.bgg_id = self.game_tesera["game"]["bggId"]

            self.tesera_name = self.game_tesera["game"]["title"]
            self.tesera_rating_user = self.game_tesera["game"]["ratingUser"]
            self.tesera_n10_rating = self.game_tesera["game"]["n10Rating"]

        with urllib.request.urlopen(
                f"https://boardgamegeek.com/xmlapi2/thing?id={self.bgg_id}&stats=1") as game_bgg_xml:
            self.game_bgg = xml.etree.ElementTree.parse(game_bgg_xml)

            self.bgg_name = self.game_bgg.find('.//item/*[@type="primary"]').get('value')
            self.bgg_average_rating = float(self.game_bgg.find('.//*ratings/average').get('value'))
            self.bgg_bayes_average_rating = float(self.game_bgg.find('.//*ratings/bayesaverage').get('value'))
            self.bgg_rank = int(self.game_bgg.find(".//*ratings/ranks/*[@type='subtype']").get('value'))
            self.bgg_weight = float(self.game_bgg.find('.//*ratings/averageweight').get('value'))

    def game_from_tesera_and_bgg(self):
        return self.tesera_name, self.tesera_rating_user, self.tesera_n10_rating, self.bgg_name, self.bgg_average_rating, self.bgg_bayes_average_rating, self.bgg_rank, self.bgg_weight
