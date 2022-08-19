import random
from fae_dicts import *


# define random selection of four possible player maps
x = random.randint(1, 4)

if x == 1:
    player_map = dict(layout1)
elif x == 2:
    player_map = dict(layout2)
elif x == 3:
    player_map = dict(layout3)
elif x == 4:
    player_map = dict(layout4)


# define story and instructions
def story():
    print('You stepped into a mushroom circle while strolling through the woods and now you have found yourself in '
          'the fairy kingdom. A small fairy kindly provides you with a few tips when you ask where you are and how to '
          'get home. You must find the Fairy King deep in the strange woods you have been transported too and plead '
          'your case to go back home. Do not go empty handed however, it is recommended that you first find a silver '
          'leaf, a river pebble, a small bone, an exotic mushroom, a pretty feather, and an opal. If you try to '
          'convince the Fairy King to release you without these gifts you will be stuck here forever.')
    print('\n***************************\n')


def instructions():
    print('Explore by choosing go north, go east, go south, and go west.')
    print('Exit the game by typing exit at any time.')
    print('Collect items with: collect "item name".')
    print('\n***************************\n')


# define inventory
inventory = []

# define valid direction move and item collection
val_move = ['go north', 'go east', 'go south', 'go west']
val_item = ['collect silver leaf', 'collect river pebble', 'collect small bone', 'collect exotic mushroom',
            'collect pretty feather', 'collect opal']


# main game
def game_play():
    player_loc = player_map['Mushroom Circle']
    print('Welcome to the Fairy Kingdom! You are in the {}.'.format(player_loc['Name']))
    print('Inventory:', inventory)

    while True:

        # get player input
        player_move = input('What would you like to do? ')
        player_move = player_move.lower().strip()

        # exit game
        if player_move == 'exit':
            print('Thanks for playing! Come back anytime!')
            break

        # navigate between rooms
        if player_move in val_move:
            if player_move in player_loc:
                # HERE IS THE POTENTIAL ISSUE, CHANGED NAMES TO PLAYER_MAP WHEN I SWITCHED TO MULTIPLE DICTIONARIES
                player_loc = player_map[player_loc[player_move]]

                # check for boss room upon entry
                if player_loc['Name'] == 'Huge Fairy Tree':
                    if len(inventory) == 6:
                        print(
                            'You made it to the Fairy King, offered your gifts and begged to go home. He is pleased '
                            'with your offerings and returns you to whence you came.')
                        break

                    elif len(inventory) != 6:
                        print(
                            'You made it to the Fairy King, unfortunately you did not bring enough gifts to appease '
                            'him and now you will reside in the fairy kingdom forever.')
                        break

                # handle the other room without an item
                if player_loc['Name'] != 'Mushroom Circle' and player_loc['item'] not in inventory:
                    print('You are at the {}'.format(player_loc['Name']))
                    print('You see a(n) {}.'.format(player_loc['item']))
                    print('Inventory:', inventory)
                    print('\n***************************\n')

                else:
                    print('You are at the {}'.format(player_loc['Name']))
                    print('Inventory:', inventory)
                    print('\n***************************\n')

            # invalid direction
            else:
                print('Your path is blocked. Maybe try another direction? ')

            # add items to inventory if valid
        elif player_move in val_item:
            if player_move in player_loc:
                if player_loc['item'] not in inventory:
                    inventory.append(player_loc['item'])
                    print('You got a(n) {}!'.format(player_loc['item']))
                    print('Inventory:', inventory)
                    print('\n***************************\n')
                elif player_loc['item'] in inventory:
                    print('You already have that item!')
                    print('Inventory:', inventory)
                    print('\n***************************\n')
            else:
                print('Invalid item!')
                print('Inventory:', inventory)
                print('\n***************************\n')

        # invalid command
        else:
            print('Sorry, please enter a valid command: go north, go east, go south, go west, collect "item name" or '
                  'exit. Thanks.')
            print('\n***************************\n')
