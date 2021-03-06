board = [" " for i in range(9)]    //creating a board

def print_board():   
    row1 = "|{}|{}|{}|".format(board[0],board[1],board[2])
    row2 = "|{}|{}|{}|".format(board[3],board[4],board[5])
    row3 = "|{}|{}|{}|".format(board[6],board[7],board[8])

    print()
    print(row1)
    print(row2)
    print(row3)
    print()


def player_move(icon):   #player moves
    if icon == "X":
        no = 1
    elif icon=="O":
        no = 2

    print("your turn player {}".format(no))  //player turn


    choice = int(input("enter your move(1-9): ").strip())
    if board[choice-1]==" ":
        board[choice-1] = icon
    else:
        print()
        print("that space is taken")    
    

def is_victory(icon):            #checks if the player wins or not
    if((board[0] == icon and board[1] == icon and board[2]==icon)or
      (board[3] == icon and board[4] == icon and board[5]==icon)or 
      (board[6] == icon and board[7] == icon and board[8]==icon)or
      (board[0] == icon and board[3] == icon and board[6]==icon)or
      (board[1] == icon and board[4] == icon and board[7]==icon)or
      (board[2] == icon and board[5] == icon and board[8]==icon)or 
      (board[0] == icon and board[4] == icon and board[8]==icon)or 
      (board[2] == icon and board[4] == icon and board[6]==icon)):
        return True
    else:
        return False     
        


def is_draw():     #if its a draw or not
    if(" " not in board):
        return True
    else:
        return False


while True:           #game loop
    print_board() 
    player_move("X")
    print_board()
    if is_victory("X"):
        print("X wins! CONGRATULATIONS!!!!")
        break
    elif is_draw():
        print("Its a Draw!")
        break
    player_move("O")
    if is_victory("X"):
        print_board()
        print("X wins! CONGRATULATIONS!!!!")
        break
    elif is_draw():
        print("Its a Draw!")
        break
    
      

