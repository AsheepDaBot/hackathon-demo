# Comments are cool! They make your code easier to understand.

# Print the possible imputs
print('''Please pick one:
            rock
            scissors
            paper''')

while True:
    # Create a dictionary of possible results
    game_dict = {'rock': 1, 'scissors': 2, 'paper': 3}
    # Get player inputs
    player_a = str(input("Player a: "))
    player_b = str(input("Player b: "))
    a = game_dict.get(player_a)
    b = game_dict.get(player_b)
    dif = a - b
    # Using result dictionary, find the difference. This difference determines the outcome
    if dif in [-1, 2]:
        print('player a wins.')
        if str(input('Do you want to play another game, yes or no?\n')) == 'yes':
            continue
        else:
            print('game over.')
            break
    elif dif in [-2, 1]:
        print('player b wins.')
        if str(input('Do you want to play another game, yes or no?\n')) == 'yes':
            continue
        else:
            print('game over.')
            break
    else:
        print('Draw.Please continue.')
        print('')