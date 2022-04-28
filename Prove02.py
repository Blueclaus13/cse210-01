#Claudia Madrid 
#Prove 02


boardKeys =[]
#Function to display a board
def displayBoard(board):
    print(f"{board[0]} | {board[1]} | {board[2]} ")
    print("-+-+-")
    print(f"{board[3]} | {board[4]} | {board[5]} ")
    print("-+-+-")
    print(f"{board[6]} | {board[7]} | {board[8]} \n")
    #{"\n1|2|3\n-+-+-\n4|5|6\n-+-+-\n7|8|9"}

#Function to introduce the first data on the board
def createBoard():
    keys =[]
    for key in range(9):
        keys.append(key + 1)

    return keys

def Turn(player):
    No_valid = True
    while No_valid:
        if player.lower() == "x":
            space = int(input("X turn. Please choose a space (1-9): "))
            No_valid = False
        elif player.lower() == "o":
            space = int(input("O turn. Please choose a space (1-9): "))
            No_valid = False
        else:
            print("Invalid value. Please, introduce X or O")

    return space
            

def main():

    again = True
    turn = "X"

    print("Welcome to Tic-Tac-Toe game")

    
#Set uo the board
    board= createBoard()
    displayBoard(board)

    

    while again:
        for i in range(10):
            #moves
            space = Turn(turn)
            board[space - 1] = turn

            # We'll check if player X or O has won,for every move after 5 moves. 
            if i >= 4:
         
                if board[0] == board[1] == board[2]:
                    displayBoard(board)             
                    break
                elif board[3] == board[4] == board[5]:
                    displayBoard(board)
                    break
                elif board[6] == board[7] == board[8]:
                    displayBoard(board) 
                    break
                elif board[0] == board[3] == board[6]:
                    displayBoard(board)
                    break
                elif board[3] == board[4] == board[5]:
                    displayBoard(board)
                    break
                elif board[1] == board[4] == board[7]:
                    displayBoard(board)
                    break
                elif board[2] == board[5] == board[8]:
                    displayBoard(board) 
                    break
                elif board[0] == board[4] == board[8]:
                    displayBoard(board)
                    break
                elif board[2] == board[4] == board[6]:
                    displayBoard(board) 
                    break

            if i == 9:
                print("\nGame Over.\n")                
                print("It's a Tie!!")

            displayBoard(board)
            
            # We have to change the player after every move.
            if turn =="X":
                turn = "O"
            else:
                turn = "X"
           
        





        play_again = input('Do you want to play again (yes/no)? ')
        if play_again.lower() == 'yes':
            print("Welcome to Tic-Tac-Toe game")
            turn = "X"
            board = createBoard()
            displayBoard(board)
        elif play_again.lower() == 'no':
            again = False;
        else:
            play_again = input('Do you want to play again (yes/no)? ')
        
    displayBoard(board)
    print(f"Won the {turn}'s")
    print('Great game')

if __name__ == "__main__":
    main()