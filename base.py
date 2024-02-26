import data_from_Internet

game = input('Введите название игры с Тесера: ')
game_from_Internet = data_from_Internet.BoardGameFromInternet(game)
game_from_Internet.game_from_Tesera_and_BGG()
