from data_from_Internet import BoardGameFromInternet, UserFromInternet

user_from_internet = UserFromInternet('pych1971')

game_from_internet = BoardGameFromInternet(2199596)

print(game_from_internet.game_from_tesera_and_bgg())
