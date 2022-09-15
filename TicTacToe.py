#TicTacToe + MiniMax for TicTacToe
#Sahaj Bhakta


def checkWin(board):

    """
    Checks if there is a winner to the TicTacToe board
    :param board: an array of length 9 that represents the tictactoe board
    :return: the letter of the winner and a " " if there is no winner, and a "c" if the board is full
    """
    # Board Indexes
    # 0 1 2
    # 3 4 5
    # 6 7 8

    win_conditions = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7],
                     [2, 5, 8], [0, 4, 8], [2, 4, 6]]

    for win_condition in win_conditions:

        if (board[win_condition[0]] == board[win_condition[1]] and
                    board[win_condition[0]] == board[win_condition[2]] and
                    board[win_condition[0]] != " "):
            return board[win_condition[0]]

    for i in board:
        if (i == " "):
            return " "

    return "CAT"


def validPlay(index, board):
    """
    returns if a requested play is valid
    :param index: the index of the requested play
    :param board: the board that the play is requested to go on
    :return: True if the play is valid, False if otherwise
    """

    if (board[index] == " "):
        return True
    return False



def printBoard(board):

    """
    prints the TicTacToe board
    :param board: the board that is to be printe
    """

    string = ""

    for i in range(9):

        if (i % 3 == 0):
            string += "["

        if (board[i] == " "):
            string += str(i+1)
        else:
            string += board[i]

        if (i % 3 == 2):
            string += "]\n"
        else:
            string += " "

    print(string + "\n")


def copyArray(board):
    """
    returns a copy of the board
    :param board: board that is going to be copied
    :return: the copied board
    """

    return board[::]


def playerTurn(board):
    """
    Makes sure the player plays in a valid space
    :param board: the board that the piece is being played on
    :return: the index of a valid play location
    """
    while (True):
        location = int(input("Type the Location of Your Play: "))

        if (validPlay(location-1, board)):
            return location - 1

        print("That is not a valid location!\n\n")

def miniMaxAlgo(board, turn, original_turn):

    """
    recursive algorithm that finds the optimal move tracing every different possible move
    down to a winning board
    :param board: the board that is being played on
    :param turn: the turn, which changes each step up in the recursive algorithm
    :param original_turn: the turn that was originally passed in that specifies the
    base cases return
    :return: the best possible points associated to a move, the index of the best possible moved
    """

    if (turn == "X"):
        not_turn = "O"
    else:
        not_turn = "X"

    if (checkWin(board) == " "):
        pass
    elif (checkWin(board) == original_turn):
        return 1, "UNUSED"
    elif (checkWin(board) == "CAT"):
        return 0, "UNUSED"
    else:
        return -1, "UNUSED"

    evaluated = False
    best_score = 0
    best_index = 0

    for index, space in enumerate(board):
        if (space == " "):
            board_copy = copyArray(board)
            board_copy[index] = turn
            points, _ = miniMaxAlgo(board_copy, not_turn, original_turn)

            if (not evaluated):
                best_score = points
                best_index = index
                evaluated = True

            elif(turn == original_turn):

                if (points > best_score):
                    best_score = points
                    best_index = index
            else:

                if (points < best_score):
                    best_score = points
                    best_index = index



    return best_score, best_index


def playGame(player_one_cpu, player_two_cpu):
    """
    plays the TicTacToe game, and employs the minimax algorithm if a player is specified
    as a cpu
    :param player_one_cpu: specifies if the first player(X) is a cpu
    :param player_two_cpu: specifies if the second player(O) is a cpu
    """

    board = [" "]*9
    player_one_turn = True

    while (checkWin(board) == " "):

        printBoard(board)


        if (player_one_turn):

            TURN = "X"

            if (player_one_cpu):
                _, index = miniMaxAlgo(board, TURN, TURN)
                board[index] = TURN
            else:
                board[playerTurn(board)] = TURN

            player_one_turn = False

        else:

            TURN = "O"

            if (player_two_cpu):
                _, index = miniMaxAlgo(board, TURN, TURN)
                board[index] = TURN

            else:
                board[playerTurn(board)] = TURN

            player_one_turn = True

    printBoard(board)

    print("The Winner Is: " + checkWin(board))