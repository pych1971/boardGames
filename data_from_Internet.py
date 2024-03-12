import json
import xml.etree.ElementTree
import urllib.request


class BoardGameFromInternet:
    def __init__(self, tesera_id):
        self.tesera_id = tesera_id
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
        return (
            self.tesera_id, self.tesera_name, self.tesera_rating_user, self.tesera_n10_rating, self.bgg_id,
            self.bgg_name,
            self.bgg_average_rating, self.bgg_bayes_average_rating, self.bgg_rank, self.bgg_weight)


class UserFromInternet:
    def __init__(self, user_alias):
        self.tesera_user_alias = user_alias
        with urllib.request.urlopen(f"https://api.tesera.ru/user/{self.tesera_user_alias}") as user_tesera_json:
            self.user_tesera = json.load(user_tesera_json)
            self.games_in_collection = self.user_tesera['gamesInCollection']
        for page in range(self.games_in_collection // 100 + 1):
            with urllib.request.urlopen(
                    f"https://api.tesera.ru/collections/base/own/{self.tesera_user_alias}?Limit=100&Offset={page}") as user_tesera_json:
                self.next_page = json.load(user_tesera_json)
                for game in self.next_page:
                    print(BoardGameFromInternet(game['game']['teseraId']).game_from_tesera_and_bgg())
