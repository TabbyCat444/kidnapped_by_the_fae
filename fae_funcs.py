from game_config import generate_player_map

# define story and instructions
def story():
    print('You stepped into a mushroom circle while strolling through the woods and now you have found yourself in '
          'the fairy kingdom. A small fairy kindly provides you with a few tips when you ask where you are and how to '
          'get home. You must find the Fairy King deep in the strange woods you have been transported to and plead '
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

# define valid direction move
val_move = ['go north', 'go east', 'go south', 'go west']

# define collectable items by name (not full command)
collectable_items = ['silver leaf', 'river pebble', 'small bone',
                     'exotic mushroom', 'pretty feather', 'opal']


# main game
def game_play():
    player_map = generate_player_map()
    player_room_key = 'Mushroom Circle'
    game_over = False

    print('Welcome to the Fairy Kingdom! You are in the {}.'.format(player_map[player_room_key]['Name']))
    print('Inventory:', inventory)

    while not game_over:

        # get player input and normalize whitespace
        player_move = input('What would you like to do? ')
        player_move = ' '.join(player_move.lower().split())

        # exit game
        if player_move == 'exit':
            print('Thanks for playing! Come back anytime!')
            break

        # navigate between rooms
        if player_move in val_move:
            current_room = player_map[player_room_key]
            if player_move in current_room:
                player_room_key = current_room[player_move]
                current_room = player_map[player_room_key]

                # check for boss room upon entry
                if current_room['Name'] == 'Huge Fairy Tree':
                    if len(inventory) == 6:
                        print(
                            'You made it to the Fairy King, offered your gifts and begged to go home. He is pleased '
                            'with your offerings and returns you to whence you came.')
                    else:
                        print(
                            'You made it to the Fairy King, unfortunately you did not bring enough gifts to appease '
                            'him and now you will reside in the fairy kingdom forever.')
                    game_over = True
                    print('Inventory:', inventory)
                    print('\n***************************\n')

                # handle the other room without an item
                elif current_room.get('item') and current_room['item'] not in inventory:
                    print('You are at the {}'.format(current_room['Name']))
                    print('You see a(n) {}.'.format(current_room['item']))
                    print('Inventory:', inventory)
                    print('\n***************************\n')

                else:
                    print('You are at the {}'.format(current_room['Name']))
                    print('Inventory:', inventory)
                    print('\n***************************\n')

            # invalid direction
            else:
                print('Your path is blocked. Maybe try another direction? ')

        # collect items
        elif player_move.startswith('collect '):
            item_name = player_move[len('collect '):]
            current_room = player_map[player_room_key]

            if item_name in collectable_items:
                if current_room.get('item') == item_name and item_name not in inventory:
                    inventory.append(item_name)
                    print('You got a(n) {}!'.format(item_name))
                elif current_room.get('item') != item_name:
                    print('There is no such item here!')
                else:
                    print('You already have that item!')
            else:
                print('Invalid item!')

            print('Inventory:', inventory)
            print('\n***************************\n')

        # invalid command
        else:
            print('Sorry, please enter a valid command: go north, go east, go south, go west, collect "item name" or '
                  'exit. Thanks.')
            print('\n***************************\n')
