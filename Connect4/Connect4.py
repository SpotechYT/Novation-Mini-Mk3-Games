import time, os
import numpy as np
import controler

lpDis = controler.Display()
lpDis.Clear()

ROW_COUNT = 8
COLUMN_COUNT = 8
 
def create_board():
    board = np.zeros((ROW_COUNT,COLUMN_COUNT))
    return board
 
def drop_piece(board,row,col,piece):
    board[row][col]= piece
 
def is_valid_location(board,col):
    #if this condition is true we will let the use drop piece here.
    #if not true that means the col is not vacant
    return board[ROW_COUNT-1][col]==0
 
def get_next_open_row(board,col):
    for r in range(ROW_COUNT):
        if board[r][col]==0:
            return r
     
def print_board(board):
    print(np.flip(board,0))
    
def winning_move(board, piece):
    # Check horizontal locations for win
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True
 
    # Check vertical locations for win
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True
 
    # Check positively sloped diaganols
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True
 
    # Check negatively sloped diaganols
    for c in range(COLUMN_COUNT-3):
        for r in range(3, ROW_COUNT):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return True
board = create_board()
game_over = False
turn = 0
played = False
col = 0
wins = [0, 0, 0, 0, 0, 0, 0, 0]
windex = 0
poi = 1
            
def reset():
    lpDis.Clear()
    lpDis.LiveMode()
    turn = 0
    board[:] = 0
    os.system('cls' if os.name == 'nt' else 'clear')
    print_board(board)
    
def winAnimR():
    c = 9
    while c >= 0:
        i = 1
        c-=1
        while i <= c:
            x = 0
            for x in range(0, 8):
                lpDis.setLED(x, i, 255, 0, 0,)
                if i > 1:
                    lpDis.setLED(x, i-1, 0, 0, 0)
            i+=1
            time.sleep(0.01)
        
def winAnimB():
    c = 9
    while c >= 0:
        i = 1
        c-=1
        while i <= c:
            x = 0
            for x in range(0, 8):
                lpDis.setLED(x, i, 0, 0, 255)
                if i > 1:
                    lpDis.setLED(x, i-1, 0, 0, 0)
            i+=1
            time.sleep(0.01)
 
while not game_over:
    #Turns
    if played:           
        if is_valid_location(board,col):
            row = get_next_open_row(board,col)
            played = False
            if turn == 0:
                drop_piece(board,row,col,1)
                i = poi
                while i <= ROW_COUNT-row:
                    lpDis.setLED(col, i, 0, 0, 255)
                    if i > 1:
                        lpDis.setLED(col, i-1, 0, 0, 0)
                    i+=1
                    time.sleep(0.03)
                
            else:
                drop_piece(board,row,col,2)
                i = poi
                while i <= ROW_COUNT-row:
                    lpDis.setLED(col, i, 255, 0, 0)
                    if i > 1:
                        lpDis.setLED(col, i-1, 0, 0, 0)
                    i+=1
                    time.sleep(0.03)
                  
            os.system('cls' if os.name == 'nt' else 'clear')
            print_board(board)
        
            turn += 1
            turn = turn % 2
    
    #Static Colors
    lpDis.setLED(8, 8, 255, 255, 0)
    lpDis.setLED(8, 1, 0, 255, 0)
    if turn == 0:
        lpDis.setLED(8, 0, 0, 0, 255)
    else:
        lpDis.setLED(8, 0, 255, 0, 0)
        
    #Updates Scoreboard LEDS
    i = 0
    for s in wins:
        if s == 1:
            lpDis.setLED(i, 0, 0, 0, 255)
            
        elif s == 2:
            lpDis.setLED(i, 0, 255, 0, 0)
            
        else:
            lpDis.setLED(i, 0, 0, 255, 0)
        i+=1
        
    #Checks For a winner
    if winning_move(board, 1):
        winAnimB()
        reset()
        if windex < len(wins):
            wins[windex] = 1
        windex+=1
        
    if winning_move(board, 2):
        winAnimR()
        reset()
        if windex < len(wins):
            wins[windex] = 2
        windex+=1
            
    #Checks for overall winner
    # for x in wins:
    #     if x == 1:
    #         wins1+=1
    #     elif x == 2:
    #         wins2+=1
            
    # totalWins = wins1+wins2
    # if len(wins) == totalWins:
    #     if wins1>wins2:
    #         print("Player 1 Wins!")
    #         winAnimB()
    #         game_over = True
            
    #     if wins2>wins1:
    #         print("Player 2 Wins!")
    #         winAnimR()
    #         game_over = True
            
    #     if wins1==wins2:
    #         print("It's a tie!")
    #         game_over = True
            
    # updates the buttons
    buts = lpDis.ButtonGet()
    if buts != []:
        if buts[0:2] == [8, 8] and buts[2]:
            break
        
        elif buts[0:2] == [8, 1] and buts[2]:
            reset()
            
        for x in range(1, 9):
            if buts[0:2] == [0, x] and buts[2]:
                col = 0
                poi = x
                played = True
                break
                
            elif buts[0:2] == [1, x] and buts[2]:
                col = 1
                poi = x
                played = True
                break
                
            elif buts[0:2] == [2, x] and buts[2]:
                col = 2
                poi = x
                played = True
                break
                
            elif buts[0:2] == [3, x] and buts[2]:
                col = 3
                poi = x
                played = True
                break
                
            elif buts[0:2] == [4, x] and buts[2]:
                col = 4
                poi = x
                played = True
                break
                
            elif buts[0:2] == [5, x] and buts[2]:
                col = 5
                poi = x
                played = True
                break
                
            elif buts[0:2] == [6, x] and buts[2]:
                col = 6
                poi = x
                played = True
                break
                
            elif buts[0:2] == [7, x] and buts[2]:
                col = 7
                poi = x
                played = True
                break

lpDis.Clear()
lpDis.LiveMode()
lpDis.Close()
