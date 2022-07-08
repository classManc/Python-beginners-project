import random
game_action = ['Rock', 'Paper', 'Scissors']# These are the valid actions for this game.
# a score-board  to keep the score of both players.
Player1_score = 0
Player2_score = 0
break_out = True
while break_out:
    try:
        #Asks the player for the number of rounds.
        #input must be of only integer types greater than zero.
        rounds = int(input('How many rounds will you like to play? '))
        assert rounds > 0, print('invalid value for rounds')
    #Handles a possible error that might occur incase an invalid number is entered by the player.
    except:
        print('invalid value for rounds')
        continue
    else:
        #repeats the game for x number of times the user has entered in rounds
        for i in range(rounds):
            #requests for the player's choice of game_action 
            Player1_choice = input('What would you like to play  Rock, Paper or Scissors? ')
            if Player1_choice not in game_action:
                print('invalid action')
                continue
            else:
                Player2_choice = random.choice(game_action)
                print(Player1_choice)
                print(Player2_choice)
                if Player1_choice == Player2_choice:
                    result = 'This is a tie'
                    print(result)
                    print(Player1_score)
                    print(Player2_score)
                elif (Player1_choice == 'Paper' and Player2_choice == 'Rock') or  (Player1_choice == 'Scissors' and Player2_choice == 'Paper') or (Player1_choice == 'Rock' and Player2_choice == 'Scissors') :
                    result = 'Player1 is the winner of this round'
                    Player1_score += 1
                    print(Player1_score)
                    print(Player2_score)
                else:
                    result = 'Player2 is the winner of this round'
                    Player2_score += 1
                    print(result)
                    print(Player1_score)
                    print(Player2_score)
        if Player1_score > Player2_score:
             print('\nPlayer1 wins the game')
        elif Player2_score > Player1_score:
            print('\nPlayer2 wins the game')
        else:
             print('\nThe game ends in a tie')
    if rounds == 0:
            break
    break_out = False
        
        
