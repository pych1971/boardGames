from data_from_Internet import BoardGameFromInternet

# game = input('Введите название игры с Тесера: ')
game = 'bloodborne-board-game'
game_from_Internet = BoardGameFromInternet(game)
print(game_from_Internet.game_from_Tesera_and_BGG())
