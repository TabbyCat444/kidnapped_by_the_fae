# The dictionary links rooms to each other, and items to rooms.
rooms = {
        'Weird Silver Trees': {'Name': 'Weird Silver Trees', 'go west': 'Mushroom Circle', 'item': 'silver leaf',
                               'collect silver leaf': 'silver leaf'},
        'Mushroom Circle': {'Name': 'Mushroom Circle', 'go east': 'Weird Silver Trees', 'go south': 'Forest River'},
        'Forest River': {'Name': 'Forest River', 'go north': 'Mushroom Circle', 'go east': 'Animal Trail',
                         'go south': 'Old Fallen Tree', 'go west': 'Bird Nest Shrubs', 'item': 'river pebble',
                         'collect river pebble': 'river pebble'},
        'Animal Trail': {'Name': 'Animal Trail', 'go north': 'Small Clearing', 'go west': 'Forest River',
                         'item': 'small bone', 'collect small bone': 'small bone'},
        'Small Clearing': {'Name': 'Small Clearing', 'go south': 'Animal Trail', 'item': 'exotic mushroom',
                           'collect exotic mushroom': 'exotic mushroom'},
        'Bird Nest Shrubs': {'Name': 'Bird Nest Shrubs', 'go east': 'Forest River', 'item': 'pretty feather',
                             'collect pretty feather': 'pretty feather'},
        'Old Fallen Tree': {'Name': 'Old Fallen Tree', 'go north': 'Forest River', 'go east': 'Huge Fairy Tree',
                            'item': 'opal', 'collect opal': 'opal'},
        'Huge Fairy Tree': {'Name': 'Huge Fairy Tree', 'go west': 'Old Fallen Tree'}
    }


# define story and instructions
def story():
    print('You stepped into a mushroom circle while strolling through the woods and now you have found yourself in\n'
          'the fairy kingdom. A small fairy kindly provides you with a few tips when you ask where you are and how to\n'
          'get home. You must find the Fairy King deep in the strange woods you have been transported too and plead\n'
          'your case to go back home. Do not go empty handed however, it is recommended that you first find a silver\n'
          'leaf, a river pebble, a small bone, an exotic mushroom, a pretty feather, and an opal. If you try to\n'
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
    player_loc = rooms['Mushroom Circle']
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
                player_loc = rooms[player_loc[player_move]]

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
                if player_loc['Name'] != 'Mushroom Circle':
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
