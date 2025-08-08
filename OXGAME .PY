board = [[' ', ' ', ' '],
         [' ', ' ', ' '],
         [' ', ' ', ' ']]
Already = []
Taken = []


class Player:
    def __init__(self, name, Taken):
        self.name = name
        run = True
        while run:
            if 'X' in Taken:
                self.pawn = 'O'
                run = False
            elif 'O' in Taken:
                self.pawn = 'X'
                run = False
            else:
                self.pawn = input(f"Enter 'X' or 'O' for {name}: ").upper()
                if self.pawn in ['X', 'O']:
                    Taken.append(self.pawn)
                    run = False
                else:
                    print("Please enter only 'X' or 'O'")

    def check(self, board):
        for i in range(3):
            if board[i][0] == board[i][1] == board[i][2] == self.pawn:
                return True
        for i in range(3):
            if board[0][i] == board[1][i] == board[2][i] == self.pawn:
                return True
        if board[0][0] == board[1][1] == board[2][2] == self.pawn:
            return True
        if board[0][2] == board[1][1] == board[2][0] == self.pawn:
            return True
        return False


class MainBoard:
    def game_board(self, board):
        print("\n" + " " * 10 + "TIC - TAC - TOE\n")

        def large_symbol(sym):
            if sym == 'X':
                return ["\\   /", "  X  ", "/   \\"]
            elif sym == 'O':
                return [" /-\\ ", "|   |", " \\-/ "]
            else:
                return ["     ", "     ", "     "]

        for i in range(3):
            row_lines = ["", "", ""]
            for j in range(3):
                big = large_symbol(board[i][j])
                for k in range(3):
                    row_lines[k] += big[k]
                    if j != 2:
                        row_lines[k] += "  |  "
            for line in row_lines:
                print("  " + line)
            if i != 2:
                print(" " + "-" * 23)
        print()

    def enter_position(self, board, Already):
        run = True
        while run:
            try:
                self.position = int(input("Enter a position (1-9): "))
            except:
                print("Invalid input. Enter a number between 1 and 9.")
                continue
            if 1 <= self.position <= 9:
                if self.position not in Already:
                    Already.append(self.position)
                    run = False
                else:
                    print("This position is already taken. Try another.")
            else:
                print("Number must be between 1 and 9.")

    def place_hold(self, board, choice):
        pos = self.position
        if 1 <= pos <= 3:
            board[0][pos - 1] = choice
        elif 4 <= pos <= 6:
            board[1][pos - 4] = choice
        elif 7 <= pos <= 9:
            board[2][pos - 7] = choice


# ==== Game Start ====
print("!!!! WELCOME TO TIC-TAC-TOE !!!!\n")
print("Position Guide:")
print("\n  1  |  2  |  3  ")
print("_____|_____|_____")
print("  4  |  5  |  6  ")
print("_____|_____|_____")
print("  7  |  8  |  9  \n")

name1 = input("Player 1 name: ").capitalize()
name2 = input("Player 2 name: ").capitalize()

P1 = Player(name1, Taken)
P2 = Player(name2, Taken)

print(f"\n{name1} is '{P1.pawn}' and {name2} is '{P2.pawn}'")
print("\nLet's start!\n")

game = MainBoard()
running = True

while running:
    # Player 1 Turn
    if len(Already) < 9:
        game.game_board(board)
        print(f"{P1.name}'s Turn ({P1.pawn})")
        game.enter_position(board, Already)
        game.place_hold(board, P1.pawn)
        if P1.check(board):
            game.game_board(board)
            print(f"{P1.name} Wins!")
            break
    else:
        print("It's a Draw!")
        break

    # Player 2 Turn
    if len(Already) < 9:
        game.game_board(board)
        print(f"{P2.name}'s Turn ({P2.pawn})")
        game.enter_position(board, Already)
        game.place_hold(board, P2.pawn)
        if P2.check(board):
            game.game_board(board)
            print(f"{P2.name} Wins!")
            break
    else:
        print("It's a Draw!")
        break
