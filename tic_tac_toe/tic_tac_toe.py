#!/usr/bin/env python3
import random
def players_info():
    player1_name=input("[+]Enter the name for player 1:")
    player2_name=input("[+]Enter the name for player 2:")
    print(f"[+]Player 1: {player1_name} \nPlayer 2: {player2_name}")
    return player1_name,player2_name

def first_player_choice(player1_name,player2_name):
    choice = input("[+]Enter either name of the player to go first or anything else for coin toss: \n")
    if choice.lower()==player1_name.lower():
        return True
    elif choice.lower()==player2_name.lower():
        return False
    else:
        print("[+]Tossing...")
        choice_player = random.choice([True,False])
        if choice:
            print(f"[+]{player1_name} goes First!")
        else:
            print(f"[+]{player2_name} goes First!")
        return choice_player

def display_grid(game):
    print(game[0]+"|"+game[1]+"|"+game[2])
    print("-"*5)
    print(game[3]+"|"+game[4]+"|"+game[5])
    print("-"*5)
    print(game[6]+"|"+game[7]+"|"+game[8])
    return

def move(grid,sign):
    entry = True
    dash = "="*10
    while entry:
        inp = True
        while inp:
            try:
                move_index = int(input(f"[+]Enter the Position \n {dash} \n"))
                print(dash)
                inp = False
            except ValueError:
                print("[-]Oops!  That was no valid number.  Try again...")
        if grid[move_index-1] == " " and  1<=move_index<=9 :
            grid[move_index-1] = sign
            entry = False
        else:
            print("[-]Invalid entry. Try again with different spot.")
    return grid

def check_victory(grid, sign):
    #for x
    if grid[0] == sign and grid[1] == sign and grid[2] == sign:
        return True
    elif grid[3] == sign and grid[4] == sign and grid[5] == sign:
        return True
    elif grid[6] == sign and grid[7] == sign and grid[8] == sign:
        return True
    elif grid[0] == sign and grid[4] == sign and grid[8] == sign:
        return True
    elif grid[2] == sign and grid[4] == sign and grid[6] == sign:
        return True
    elif grid[0] == sign and grid[3] == sign and grid[6] == sign:
        return True
    elif grid[1] == sign and grid[4] == sign and grid[7] == sign:
        return True
    elif grid[2] == sign and grid[5] == sign and grid[8] == sign:
        return True
    else:
        return False

def victory_message(sign,player1_name,player2_name,is_player_one_first):
    if sign == 'X':
        if is_player_one_first:
            print(f"[+]{player1_name} Wins!!!")
        else:
            print(f"[+]{player2_name} Wins!!!")
    else:
        if is_player_one_first:
            print(f"[+]{player2_name} Wins!!!")
        else:
            print(f"[+]{player1_name} Wins!!!")
    return

if __name__ == "__main__":
    print("Welcome to the game!")
    dash = "="*10
    player1_name,player2_name = players_info()
    play = True
    while play:
        is_player_one_first = first_player_choice(player1_name,player2_name)
        game = True
        grid_pos = [str(i) for i in range(1,10)]
        clear_game = [" "]*9
        grid = clear_game
        display_grid(grid_pos)
        # game = True
        move_num = 0
        while game:
            if move_num%2 == 0:
                print("...For X ", end="")
                sign = 'X'
            else:
                print("...For 0 ", end="")
                sign = '0'
            grid = move(grid,sign)
            display_grid(grid)
            print(dash)
            victory = check_victory(grid,sign)
            if victory:
                victory_message(sign,player1_name,player2_name,is_player_one_first)
                break
            move_num += 1
            if move_num > 8:
                print("[+]NO Moves Left!!! It's a DRAW.")
                game = False
        play_mode = input("[+]R for Restart. Any key to Quit.")
        if play_mode.lower() != 'r':
            print("[-]Quitting...")
            play = False
