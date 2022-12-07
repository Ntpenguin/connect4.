# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Nathanael Baron
#               Nathanael Kamat
#               Ajith Roy
#               Kyle Grimes
# Section:      524
# Assignment:   12.15.1
# Date:         11/28/22

# As a team, we have gone through all required sections of the
# tutorial, and each team member understands the material

from turtle import *
# imports turtle
screen = Screen()
board = []
rows = 7
cols = 6
x_init = -450
y_init = -450 * (rows / cols)
height = -2 * y_init
width = -2 * x_init
radius = 50
player = 1
# sets variables

textinput("Directions", "This is connect 4. You need to place a piece down one of the columns, and the first person to reach 4 consecutive pieces in any direction while win. Do you understand?")

def play(x, y):
    #makes the board and piece functionality
    fileIO = open('output.txt', 'wt')
    type(fileIO)
    global board, player
    board_legend = {0 : "white", 1 : "red", 2 : "yellow"}
    player_done = False
    for i in range(rows):
        for j in range(cols):
            left_x = x_init + j*(width/cols)
            right_x = x_init + (j+1)*(width/cols)
            if x >= left_x and x <= right_x:
                for k in range(rows):
                    if player_done:
                        break
                    if board[k][j] == 0:
                        left_y = y_init + (k)*(height/rows)
                        right_y = y_init + (k+1)*(height/rows)
                        board[k][j] = player
                        draw_circle((left_x+right_x)/2, (left_y+right_y)/2, radius, board_legend[player])
                        player = 2 if player == 1 else 1
                        player_done = True

    combinations = []
    for i in range(rows):
        for j in range(cols):
            combination_vertical, combination_horizontal, combination_diagonal_1, combination_diagonal_2 = [], [], [], []
            for k in range(4):
                if i+k < 7: combination_vertical.append(board[i+k][j])
                if j+k < 6: combination_horizontal.append(board[i][j+k])
                if i+k < 7 and j+k < 6: combination_diagonal_1.append(board[i+k][j+k])
                if j+k < 6 and i-k >= 0: combination_diagonal_2.append(board[i-k][j+k])
            combinations.append(combination_vertical)
            combinations.append(combination_horizontal)
            combinations.append(combination_diagonal_1)
            combinations.append(combination_diagonal_2)

    text = None
    for combination in combinations:
        if len(combination) == 4 and len(set(combination)) == 1 and combination[0] != 0:
            if combination[0] == 1:
                fileIO.write("Player red won!")
                fileIO.close()
                text = "Player red won!"
            elif combination[0] == 2:
                fileIO.write("Player yellow won!")
                fileIO.close()
                text = "Player yellow won!"
            else:
                text = "Null."

    if not text:
        empty = 0
        for i in range(rows):
            for j in range(cols):
                if board[i][j]: empty += 1
        if not empty:
            fileIO.write("It is a tie!")
            fileIO.close()
            text = "It is a tie!"

    try:
        if text:
            print(text)
            clear()
            board = []
            player = 1
            init_board()
            onclick(play)
            mainloop()
    except:
        print("Error! Restart game.")



def draw_circle(x, y, row, color):
    '''
    draws a circle

    :param x: x coord
    :param y: y coord
    :param row: row
    :param color: colors
    :return: returns circle
    '''
    penup()
    goto(x, y-row)
    pendown()
    fillcolor(color)
    begin_fill()
    circle(row)
    end_fill()


def draw_rectangle(x, y, width, height, color):
    '''
    draw rectangle

    :param x: x coord
    :param y: y coord
    :param width: width of the rectangle
    :param height: height of the rectangle
    :param color: color of the rectangle
    :return: returns rectangle
    '''
    penup()
    goto(x, y)
    pendown()
    fillcolor(color)
    begin_fill()
    goto(x+width, y)
    goto(x+width, y+height)
    goto(x, y+height)
    goto(x, y)
    end_fill()


def draw_board(board):
    '''
    draws a board for connect 4

    :param board: takes a board list
    :return: returns a graphical board
    '''
    draw_rectangle(x_init, y_init, width, height, "blue")
    draw_pieces(board, x_init, y_init, radius, width, height)


def draw_pieces(board, x, y, radius, i, j):
    board_legend = {0 : "white", 1 : "red", 2 : "yellow"}
    # draws pieces
    for i in range(rows):
        for j in range(cols):
            left_x = x_init + j*(width/cols)
            right_x = x_init + (j+1)*(width/cols)
            left_y = y_init + i*(height/rows)
            right_y = y_init + (i+1)*(height/rows)
            draw_circle((left_x+right_x)/2, (left_y+right_y)/2, radius, board_legend[board[i][j]])


def init_board():
    global board, screen

    screen.setup(750, 750)
    screen.setworldcoordinates(-500, -500, 500, 500)
    screen.title("Connect Four - Python Edition")
    screen.bgcolor("black")
    speed(0)
    hideturtle()
    screen.tracer(0, 0)

    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(0)
        board.append(row)

    draw_board(board)


if __name__ == "__main__":
    init_board()
    screen.onclick(play)
    screen.mainloop()