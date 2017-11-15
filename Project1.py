# This program will initialize a tick-tack-toe board #
import sys

class players:

    def __init__(self, alpha, name):
        self.alpha = alpha
        self.name = name

def reset(grid, p1, p2):

    grid = [["." for i in range(3)] for j in range(3)]
    play(grid, p1, p2)

def play(grid, p1, p2):

    cord = ""
    while done(grid) != True:

        cord = input('Player 1 enter coordinates: ')
        move(cord, grid, p1)

        str = ""
        for i in range(0, 3):
            str = ""
            for j in range(0, 3):
                str += grid[i][j]
            print (str)
        print (done(grid))
        # Player 1
        if done(grid):
            print("Player 1 wins")
            play_again = input("Would you like to play again? (y/n)")
            if play_again == 'y':
                reset(grid, p1, p2)
            else:
                break
            break
        # Player 2
        cord = input('Player 2 enter coordinates: ')
        move(cord, grid, p2)

        for i in range(0, 3):
            str = ""
            for j in range(0, 3):
                str += grid[i][j]
            print (str)
        print (done(grid))
        if done(grid):
            print("Player 2 wins")
            play_again = input("Would you like to play again? (y/n) ")
            if play_again == 'y':
                reset(grid, p1, p2)
            else:
                break
            break

def done(grid):

    if grid[0][1] == '0' and grid[0][0] == '0' and grid[0][2] == '0':
        return True
    elif grid[0][1] == 'X' and grid[0][0] == 'X' and grid[0][2] == 'X':
        return True
    # Top Row win cond

    elif grid[1][0] == '0' and grid[1][1] == '0' and grid[1][2] == '0':
        return True
    elif grid[1][0] == 'X' and grid[1][1] == 'X' and grid[1][2] == 'X':
        return True
    # Mid Row win cond

    elif grid[2][0] == '0' and grid[2][1] == '0' and grid[2][2] == '0':
        return True
    elif grid[2][0] == 'X' and grid[2][1] == 'X' and grid[2][2] == 'X':
        return True
    # Bottom Row win cond

    elif grid[0][1] == '0' and grid [1][1] == '0' and grid[2][1] == '0':
        return True
    elif grid[0][1] == 'X' and grid [1][1] == 'X' and grid[2][1] == 'X':
        return True
    # Mid down win cond

    elif grid[0][0] == '0' and grid[1][1] == '0' and grid[2][2] == '0':
        return True
    elif grid[0][0] == 'X' and grid[1][1] == 'X' and grid[2][2] == 'X':
        return True
    # Diagonal Right

    elif grid[2][0] == '0' and grid[1][1] == '0' and grid[0][2] == '0':
        return True
    elif grid[2][0] == 'X' and grid[1][1] == 'X' and grid[0][2] == 'X':
        return True
    # Diagonal Left

    elif grid[0][2] == '0' and grid[1][2] == '0' and grid[2][2] == '0':
        return True
    elif grid[0][2] == 'X' and grid[1][2] == 'X' and grid[2][2] == 'X':
        return True
    # Left Side Vertical

    elif grid[0][0] == '0' and grid[1][0] == '0' and grid[2][0] == '0':
        return True
    elif grid[0][0] == 'X' and grid[1][0] == 'X' and grid[2][0] == 'X':
        return True
    # Right Side Vertical

    else:
        return False

def move(cord, grid, player):

    cordx = None
    cordy = None
    for i in range(len(cord)):
        if cordx == None:
            if cord[i].isdigit():
                cordx = cord[i]
                i += 1
            else:
                i += 1
        if cordy == None:
            if cord[i].isdigit():
                cordy = cord[i]
                i += 1
            else:
                i += 1
    if grid[int(cordx)][int(cordy)] != '.':
        print("The spot you have chosen has already been used.")
        cord = input("Player" + ' ' + player.name + ' ' + "please enter different coordinates: ")
        move(cord, grid, player)

    else:
        grid[int(cordx)][int(cordy)] = player.alpha

    return

def main():

    grid = [["." for i in range(3)] for j in range(3)]
    p1 = players('0', '1')
    p2 = players('X', '2')

    play(grid, p1, p2)





main()