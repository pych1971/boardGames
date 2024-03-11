from data_from_Internet import BoardGameFromInternet

for game in ('great-western-trail-second-edition', 'great-western-trail-argentina', 'great-western-trail-new-zealand'):
    # game = input('Введите название игры с Тесера: ')
    game_from_Internet = BoardGameFromInternet(game)
    # print(game_from_Internet.game_from_Tesera_and_BGG())
