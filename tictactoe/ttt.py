import random
import itertools


class EndGame(Exception):
    pass


class TicTacToe:

    def __init__(self):
        self.board = []

    def create_board(self):
        return [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]

    def check_end_game(self, board):
        # check rows
        for player in ["X", "O"]:
            for i in range(3):
                if board[i].count(player) == 3:
                    print("Congrats! player ", player, " wins")
                    raise EndGame

        # check columns
        for player in ["X", "O"]:
            for i in range(3):
                if board[0][i] == board[1][i] == board[2][i] == player:
                    print("Congrats! player", player, " wins")
                    raise EndGame

        # check diagonal
        for player in ["X", "O"]:
            if board[0][0] == board[1][1] == board[2][2] == player:
                print("Congrats! player", player, " wins")
                raise EndGame

        # check diagonal
        for player in ["X", "O"]:
            if board[0][2] == board[1][1] == board[2][0] == player:
                print("Congrats! player", player, " wins")
                raise EndGame

        if (list(itertools.chain(*board)).count("X") + list(itertools.chain(*board)).count("O")) == 9:
            print("It's a draw!")
            raise EndGame

    def update_board(self, player_input, board, player):
        board[player_input[0]-1][player_input[1]-1] = player
        return board

    def ask_input(self, board, player):
        while True:
            # ask input
            try:
                player_input = list(map(int, input("Hello player {} what row and column do you want to play: ".format(player)).split()))
                # check if input is possible
                if board[player_input[0] - 1][player_input[1] - 1] == "-":
                    return player_input
                else:
                    print("Position is already taken, please try again")
            except (IndexError, ValueError) as e:
                print("Please input your results in the correct format: ")
                print("<row number><space><column number>")
                continue

    def print_board(self, board):
        print("Current board: ")
        for i in board:
            print(" ".join(map(str, i)))

    def play(self):
        board = self.create_board()

        try:
            while True:
                for player in ["X", "O"]:
                    player_input = self.ask_input(board, player)
                    board = self.update_board(player_input, board, player)
                    self.print_board(board)
                    self.check_end_game(board)
        except EndGame:
            pass

    def random_opponent(self, board):
        while True:
            random_play = [random.randrange(1, 4, 1), random.randrange(1, 4, 1)]
            if board[random_play[0] - 1][random_play[1] - 1] == "-":
                return random_play

    def play_with_random_opponent(self):
        board = self.create_board()

        try:
            while True:
                player = "X"
                player_input = self.ask_input(board, player)
                board = self.update_board(player_input, board, player)
                self.print_board(board)
                self.check_end_game(board)

                player = "O"
                player_input = self.random_opponent(board)
                board = self.update_board(player_input, board, player)
                self.print_board(board)
                self.check_end_game(board)

        except EndGame:
            pass


if __name__ == "__main__":
    game = TicTacToe()
    # game.play()
    game.play_with_random_opponent()

    # todo: randomize the player that begins
    # todo: train an algorithm that can be opponent
