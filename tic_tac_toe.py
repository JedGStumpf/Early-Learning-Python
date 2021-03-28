from IPython.display import clear_output
import random

def tic_toe_table(table):
    print('_____________')
    print('|',table[0],'|',table[1],'|',table[2],'|')
    print('_____________')
    print('|',table[3],'|',table[4],'|',table[5],'|')
    print('_____________')
    print('|',table[6],'|',table[7],'|',table[8],'|')
    print('_____________')
    return 'Tic Tac Toe'

def first_turn():
    #board_list = list(range(1,10))
    global turn
    turn = random.randint(1,2)
    global user_one 
    user_one = input('User One please enter your name: ')
    global user_two 
    user_two = input('User Two please enter your name: ')
    
    if turn == 1:
        turn = user_one
        print(f'Your First {user_one}')
    else:
        turn = user_two
        print(f'Your First {user_two}')
        
def take_turn():
    global turn
    if turn == user_one:
        turn = user_two
    elif turn == user_two:
        turn = user_one

def play_again():
    again = input('would you like to play again? Y/N? : ')
    if again.upper().startswith('Y'):
        game_play()
        return True
    else:
        return False
        
def game_play(*args):
    first_turn()
    select = 0
    let = ""
    count = 0
    board_list = list(range(1,10))
    while count < 9:
        if turn == user_one:
            let = 'X'
        else:
            let = 'O'
        clear_output()
        print(tic_toe_table(board_list))
        select = input(f'{turn} Make your selection spaces available are: {board_list} // or press Q to quit:  ')
        if select == '':
            print('Invalid selection, pleasse select from the available list')
            continue
        elif select == 'X' or select == 'O':
            print('Invalid selection, pleasse select from the available list')
            continue
        elif select.isalpha():
            if select.lower().startswith('q'):
                break
        else: select = int(select)
        if select not in board_list:
            print('Invalid selection, pleasse select from the available list')
            continue

        else:
            board_list[board_list.index(select)] = let
            win_list = [board_list[0:3],board_list[3:6],board_list[6:9],board_list[0:8:3],board_list[1:9:3],board_list[2:9:3],board_list[0:9:4],board_list[2:8:2]]
            if list(let)*3 in win_list:
                print(f'Congratulations {turn}, you are the Winner!!!')
                print(tic_toe_table(board_list))
                if play_again() == False:
                    print('Goodbye')
                    break
            count+=1
            if count == 9:
                print('Cats Game...')
                play_again()
            else:
                take_turn()

                    
game_play()