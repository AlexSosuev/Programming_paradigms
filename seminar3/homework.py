# Задача. Написать игру в “Крестики-нолики”. Можете использовать любые парадигмы, которые посчитаете наиболее
# подходящими. Можете реализовать доску как угодно - как одномерный массив или двумерный массив (массив массивов).
# Можете использовать как правила, так и хардкод, на своё усмотрение. Главное, чтобы в игру можно было поиграть через
# терминал с вашего компьютера.

class TicTacToe:
    def __init__(self):
        self.board = list(range(1, 10))
        self.players = ['X', 'O']
        self.counter = 0

    def draw_board(self):
        print("-" * 13)
        for i in range(3):
            print("|", self.board[0+i*3], "|", self.board[1+i*3], "|", self.board[2+i*3], "|")
            print("-" * 13)

    def take_input(self, player_token):
        valid = False
        while not valid:
            player_answer = input("Куда поставим " + player_token + "? ")
            try:
                player_answer = int(player_answer)
            except:
                print("Некорректный ввод. Вы уверены, что ввели число?")
                continue
            if player_answer >= 1 and player_answer <= 9:
                if(str(self.board[player_answer-1]) not in "XO"):
                    self.board[player_answer-1] = player_token
                    valid = True
                else:
                    print("Эта клетка уже занята!")
            else:
                print("Некорректный ввод. Введите число от 1 до 9.")

    def check_win(self):
        win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
        for each in win_coord:
            if self.board[each[0]] == self.board[each[1]] == self.board[each[2]]:
                return self.board[each[0]]
        return False

    def play(self):
        print("*" * 48)
        print("*", " " * 14, "Игра Крестики-нолики для двух игроков", " " * 14, "*")
        print("*" * 48)

        while True:
            self.draw_board()
            current_player = self.players[self.counter % 2]
            self.take_input(current_player)
            self.counter += 1

            if self.counter > 4:
                winner = self.check_win()
                if winner:
                    print(winner, "выиграл!")
                    break

            if self.counter == 9:
                print("Ничья!")
                break

        self.draw_board()
        input("Нажмите Enter для выхода!")

game = TicTacToe()
game.play()