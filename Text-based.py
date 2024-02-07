import random

def get_player_choice(player_name):
    user_choice = input(f"{player_name}, enter your choice (rock, paper, or scissors): ").lower()
    while user_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Please enter rock, paper, or scissors.")
        user_choice = input(f"{player_name}, enter your choice (rock, paper, or scissors): ").lower()
    return user_choice


def determine_winner(player1_choice, player2_choice):
    outcomes = {
        "rock": {"rock": "Tie", "paper": "Player 2", "scissors": "Player 1"},
        "paper": {"rock": "Player 1", "paper": "Tie", "scissors": "Player 2"},
        "scissors": {"rock": "Player 2", "paper": "Player 1", "scissors": "Tie"}
    }
    return outcomes[player1_choice][player2_choice]


def display_scores(player1_name, player1_score, player2_name, player2_score):
    print(f"Scores - {player1_name}: {player1_score}, {player2_name}: {player2_score}")


def get_riddle():
    riddles = {
        "I speak without a mouth and hear without ears. I have no body, but I come alive with the wind. What am I?": "echo",
        "The more you take, the more you leave behind. What am I?": "footsteps",
        "I have keys but open no locks. I have space but no room. You can enter, but you can't go inside. What am I?": "keyboard",
        "The person who makes it, sells it. The person who buys it never uses it. What is it?": "coffin",
        "What has a heart that doesn't beat?": "artichoke",
        "Forward I am heavy, but backward I am not. What am I?": "ton",
        "What comes once in a minute, twice in a moment, but never in a thousand years?": "m",
        "What has keys but can't open locks?": "piano",
        "I can be cracked, made, told, and played. What am I?": "joke",
        "The more you have of it, the less you see. What is it?": "darkness",
        "What has a head, a tail, is brown, and has no legs?": "penny",
        "I'm tall when I'm young, and short when I'm old. What am I?": "candle",
        "What has one eye but can't see?": "needle",
        "I'm not alive, but I grow; I don't have lungs, but I need air; I don't have a mouth, but water kills me. What am I?": "fire",
        "What has cities, but no houses; forests, but no trees; and rivers, but no water?": "map"
    
    }
    return random.choice(list(riddles.items()))


class Stack:
    def __init__(self):
        self._list = []

    def __len__(self):
        return len(self._list)

    def push(self, element):
        if len(self._list) <= 6:
            self._list.append(element)
        else:
            return

    def peek(self):
        return self._list[-1]


def init_board():
    rows = ['a', 'b', 'c', 'd', 'e', 'f']
    board = [[' '] * 7 for _ in range(len(rows))]
    return board


def init_stacks():
    return [Stack() for _ in range(7)]


def print_board(board):
    rows = ['a', 'b', 'c', 'd', 'e', 'f']
    top = '    1   2   3   4   5   6   7   '
    row = [[''] for _ in range(7)]
    row[0][0] = 'f | '
    row[1][0] = 'e | '
    row[2][0] = 'd | '
    row[3][0] = 'c | '
    row[4][0] = 'b | '
    row[5][0] = 'a | '
    print('')
    print('  ' + '-' * (len(top) - 3))
    for j in range(0, len(rows)):
        for i in range(1, 8):
            row[j][0] = row[j][0] + str(board[j][i - 1]) + ' | '
        print(row[j][0])
        print('  ' + '-' * ((len(row[j][0]) - 3)))
    print(top)
    print('')


def move(piece, board, stacks):
    set0 = {'1', '2', '3', '4', '5', '6', '7'}
    pos = str(input(f'{piece} player, enter your move (1-7): '))
    
    if pos not in set0:
        print('Input must be an integer between 1 and 7')
        return move(piece, board, stacks)
    else:
        pos = int(pos)
        if len(stacks[pos - 1]) < 6:
            stacks[pos - 1].push(piece)
            board[6 - len(stacks[pos - 1])][pos - 1] = stacks[pos - 1].peek()
        else:
            print('Column full, try again...')
            return move(piece, board, stacks)
    return board, stacks


def check_win(s, board):
    for j in range(0, 6):
        for i in range(3, 7):
            if (board[j][i] == board[j][i - 1] == board[j][i - 2] == board[j][i - 3] == s):
                return True
    for i in range(0, 7):
        for j in range(3, 6):
            if (board[j][i] == board[j - 1][i] == board[j - 2][i] == board[j - 3][i] == s):
                return True
    for i in range(0, 4):
        for j in range(0, 3):
            if (board[j][i] == board[j + 1][i + 1] == board[j + 2][i + 2] == board[j + 3][i + 3] == s or
                    board[j + 3][i] == board[j + 2][i + 1] == board[j + 1][i + 2] == board[j][i + 3] == s):
                return True
    return False


def choose_piece():
    piece = str(input(f"{player1_name }, choose 'X' or 'O': "))
    while piece not in {'X','x','o', 'O'}:
        print("Invalid choice. Please enter 'X' or 'O'.")
        piece = str(input("Player 1, choose 'X' or 'O': "))
    return piece


def main():
    global player1_score,player2_score,player1_name,player2_name
    print("")
    print("Welcome to the Game AdventuraVerse")
    print("")
    player1_name = input("Enter Player 1's name: ")
    player2_name = input("Enter Player 2's name: ")
    print("")
    player1_score = 0
    player2_score = 0

    print("Entering to Level-1")
    print("The Game is Rock Paper Scissors.")
    print("The winner is determined based on the rules: rock crushes scissors, scissors cuts paper, and paper covers rock .")
    print("The Game starts now....")

    player1_choice = get_player_choice(player1_name)
    player2_choice = get_player_choice(player2_name)

    winner = determine_winner(player1_choice, player2_choice)
    print("")
    if winner == "Tie":
        print("It's a tie!.Both of you scored one point.")
    else:
        print(f"{winner} wins!")

    if winner == ("Player 1"):
        player1_score += 1
    else:
        player2_score += 1
   
    display_scores(player1_name, player1_score, player2_name, player2_score)
    print("")
    print("Entering to Level-2")
    print("Have fun with a Riddles Game! Solve different puzzles, score points, and see how clever you are.")    
    print("The Game starts now....")
    print("")
    print(f"{player1_name} 's turn :") 
    riddle, answer = get_riddle()
    print("\nRiddle:")
    print(riddle)
    user_answer = input("\nYour answer: ").lower()

    if user_answer == answer:
        print("Correct! You got it right.")
        player1_score += 1
    else:
        print(f"Wrong! The correct answer is: {answer}")

    
    print(f"\n{player2_name}'s turn:")
    riddle, answer = get_riddle()
    print("\nRiddle:")
    print(riddle)
    user_answer = input("\nYour answer: ").lower()

    if user_answer == answer:
        print("Correct! You got it right.")
        player2_score += 1
    else:
        print(f"Wrong! The correct answer is: {answer}")
    print("")
    display_scores(player1_name, player1_score, player2_name, player2_score)    
    print("")
    print("Entering to level-3")
    print("Experience the excitement of Connect 4, strategically placing discs in a grid to achieve a winning combination of four in a row, either vertically, horizontally, or diagonally.")
    print("The Game starts now....")

    player1_piece = choose_piece()
    player2_piece = 'X' if player1_piece == 'O' else 'O'

    board = init_board()
    stacks = init_stacks()
    print_board(board)
    
    game = False
    while not game:
        board, stacks = move(player1_piece, board, stacks)
        print_board(board)
        game = check_win(player1_piece, board)
        if game:
            print(f'Player 1 ({player1_piece}) wins!')
            player1_score += 1
            break

        board, stacks = move(player2_piece, board, stacks)
        print_board(board)
        game = check_win(player2_piece, board)
        if game:
            print(f'Player 2 ({player2_piece}) wins!')
            player2_score += 1
            break
    print("")
    display_scores(player1_name, player1_score, player2_name, player2_score)   
    print("")
    if(player1_score>player2_score):
        print(f"{player1_name} , You won the game.....")
    else:
        print(f"{player1_name} , You won the game.....")

if __name__ == "__main__":
    main()
