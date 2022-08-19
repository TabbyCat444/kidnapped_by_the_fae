# The dictionary links rooms to each other, and items to rooms.
# Room layout options defined as appropriate dictionaries
layout1 = {
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

layout2 = {
    'Huge Fairy Tree': {'Name': 'Huge Fairy Tree', 'go west': 'Mushroom Circle'},
    'Mushroom Circle': {'Name': 'Mushroom Circle', 'go east': 'Huge Fairy Tree', 'go south': 'Forest River'},
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
    'Weird Silver Trees': {'Name': 'Weird Silver Trees', 'go west': 'Old Fallen Tree', 'item': 'silver leaf',
                           'collect silver leaf': 'silver leaf'}
}

layout3 = {
    'Weird Silver Trees': {'Name': 'Weird Silver Trees', 'go west': 'Mushroom Circle', 'item': 'silver leaf',
                           'collect silver leaf': 'silver leaf'},
    'Mushroom Circle': {'Name': 'Mushroom Circle', 'go east': 'Weird Silver Trees', 'go south': 'Forest River'},
    'Forest River': {'Name': 'Forest River', 'go north': 'Mushroom Circle', 'go east': 'Animal Trail',
                     'go south': 'Old Fallen Tree', 'go west': 'Bird Nest Shrubs', 'item': 'river pebble',
                     'collect river pebble': 'river pebble'},
    'Animal Trail': {'Name': 'Animal Trail', 'go north': 'Huge Fairy Tree', 'go west': 'Forest River',
                     'item': 'small bone', 'collect small bone': 'small bone'},
    'Huge Fairy Tree': {'Name': 'Huge Fairy Tree', 'go south': 'Animal Trail'},
    'Bird Nest Shrubs': {'Name': 'Bird Nest Shrubs', 'go east': 'Forest River', 'item': 'pretty feather',
                         'collect pretty feather': 'pretty feather'},
    'Old Fallen Tree': {'Name': 'Old Fallen Tree', 'go north': 'Forest River', 'go east': 'Huge Fairy Tree',
                        'item': 'opal', 'collect opal': 'opal'},
    'Small Clearing': {'Name': 'Small Clearing', 'go west': 'Old Fallen Tree', 'item': 'exotic mushroom',
                       'collect exotic mushroom': 'exotic mushroom'}
}

layout4 = {
    'Weird Silver Trees': {'Name': 'Weird Silver Trees', 'go west': 'Mushroom Circle', 'item': 'silver leaf',
                           'collect silver leaf': 'silver leaf'},
    'Mushroom Circle': {'Name': 'Mushroom Circle', 'go east': 'Weird Silver Trees', 'go south': 'Forest River'},
    'Forest River': {'Name': 'Forest River', 'go north': 'Mushroom Circle', 'go east': 'Animal Trail',
                     'go south': 'Old Fallen Tree', 'go west': 'Huge Fairy Tree', 'item': 'river pebble',
                     'collect river pebble': 'river pebble'},
    'Animal Trail': {'Name': 'Animal Trail', 'go north': 'Small Clearing', 'go west': 'Forest River',
                     'item': 'small bone', 'collect small bone': 'small bone'},
    'Small Clearing': {'Name': 'Small Clearing', 'go south': 'Animal Trail', 'item': 'exotic mushroom',
                       'collect exotic mushroom': 'exotic mushroom'},
    'Huge Fairy Tree': {'Name': 'Huge Fairy Tree', 'go east': 'Forest River'},
    'Old Fallen Tree': {'Name': 'Old Fallen Tree', 'go north': 'Forest River', 'go east': 'Huge Fairy Tree',
                        'item': 'opal', 'collect opal': 'opal'},
    'Bird Nest Shrubs': {'Name': 'Bird Nest Shrubs', 'go west': 'Old Fallen Tree', 'item': 'pretty feather',
                         'collect pretty feather': 'pretty feather'}
}
