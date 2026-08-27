# The dictionary links rooms to each other, and items to rooms.
# Room layout options defined as appropriate dictionaries

# Each layout uses a structured list of room definitions.
# 'exits' maps direction abbreviations to target room names.
# 'item' is the item found in that room (or None if there is none).


def build_room_data(room_definitions):
    """Convert a list of room definitions into a lookup dict.

    The resulting dict keys are room names, and each value contains:
      - 'Name': the room name
      - 'go <direction>': the target room name for each exit
      - 'item': the item found in this room (if any)
    """
    rooms = {}
    for room_def in room_definitions:
        room_data = {'Name': room_def['name']}
        for direction, target_name in room_def['exits'].items():
            room_data[f'go {direction}'] = target_name
        if room_def.get('item'):
            room_data['item'] = room_def['item']
        rooms[room_def['name']] = room_data
    return rooms


def validate_layout(layout):
    """Check that every room is reachable from Mushroom Circle."""
    visited = set()
    queue = ['Mushroom Circle']
    while queue:
        current = queue.pop()
        if current in visited:
            continue
        visited.add(current)
        for key, value in layout[current].items():
            if key.startswith('go ') and value in layout and value not in visited:
                queue.append(value)
    unreachable = set(layout.keys()) - visited
    if unreachable:
        raise ValueError(f"Unreachable rooms in layout: {unreachable}")


# ---------------------------------------------------------------------------
# Layout 1
# ---------------------------------------------------------------------------
LAYOUT1_DEFS = [
    {
        'name': 'Weird Silver Trees',
        'exits': {'west': 'Mushroom Circle'},
        'item': 'silver leaf',
    },
    {
        'name': 'Mushroom Circle',
        'exits': {'east': 'Weird Silver Trees', 'south': 'Forest River'},
        'item': None,
    },
    {
        'name': 'Forest River',
        'exits': {'north': 'Mushroom Circle', 'east': 'Animal Trail',
                  'south': 'Old Fallen Tree', 'west': 'Bird Nest Shrubs'},
        'item': 'river pebble',
    },
    {
        'name': 'Animal Trail',
        'exits': {'north': 'Small Clearing', 'west': 'Forest River'},
        'item': 'small bone',
    },
    {
        'name': 'Small Clearing',
        'exits': {'south': 'Animal Trail'},
        'item': 'exotic mushroom',
    },
    {
        'name': 'Bird Nest Shrubs',
        'exits': {'east': 'Forest River'},
        'item': 'pretty feather',
    },
    {
        'name': 'Old Fallen Tree',
        'exits': {'north': 'Forest River', 'east': 'Huge Fairy Tree'},
        'item': 'opal',
    },
    {
        'name': 'Huge Fairy Tree',
        'exits': {'west': 'Old Fallen Tree'},
        'item': None,
    },
]

layout1 = build_room_data(LAYOUT1_DEFS)
validate_layout(layout1)

# ---------------------------------------------------------------------------
# Layout 2
# ---------------------------------------------------------------------------
LAYOUT2_DEFS = [
    {
        'name': 'Huge Fairy Tree',
        'exits': {'west': 'Mushroom Circle'},
        'item': None,
    },
    {
        'name': 'Mushroom Circle',
        'exits': {'east': 'Huge Fairy Tree', 'south': 'Forest River'},
        'item': None,
    },
    {
        'name': 'Forest River',
        'exits': {'north': 'Mushroom Circle', 'east': 'Animal Trail',
                  'south': 'Old Fallen Tree', 'west': 'Bird Nest Shrubs'},
        'item': 'river pebble',
    },
    {
        'name': 'Animal Trail',
        'exits': {'north': 'Small Clearing', 'west': 'Forest River'},
        'item': 'small bone',
    },
    {
        'name': 'Small Clearing',
        'exits': {'south': 'Animal Trail'},
        'item': 'exotic mushroom',
    },
    {
        'name': 'Bird Nest Shrubs',
        'exits': {'east': 'Forest River'},
        'item': 'pretty feather',
    },
    {
        'name': 'Old Fallen Tree',
        'exits': {'north': 'Forest River', 'east': 'Huge Fairy Tree'},
        'item': 'opal',
    },
    {
        'name': 'Weird Silver Trees',
        'exits': {'west': 'Old Fallen Tree'},
        'item': 'silver leaf',
    },
]

layout2 = build_room_data(LAYOUT2_DEFS)
validate_layout(layout2)

# ---------------------------------------------------------------------------
# Layout 3
# ---------------------------------------------------------------------------
LAYOUT3_DEFS = [
    {
        'name': 'Weird Silver Trees',
        'exits': {'west': 'Mushroom Circle'},
        'item': 'silver leaf',
    },
    {
        'name': 'Mushroom Circle',
        'exits': {'east': 'Weird Silver Trees', 'south': 'Forest River'},
        'item': None,
    },
    {
        'name': 'Forest River',
        'exits': {'north': 'Mushroom Circle', 'east': 'Animal Trail',
                  'south': 'Old Fallen Tree', 'west': 'Bird Nest Shrubs'},
        'item': 'river pebble',
    },
    {
        'name': 'Animal Trail',
        'exits': {'north': 'Huge Fairy Tree', 'west': 'Forest River'},
        'item': 'small bone',
    },
    {
        'name': 'Huge Fairy Tree',
        'exits': {'south': 'Animal Trail'},
        'item': None,
    },
    {
        'name': 'Bird Nest Shrubs',
        'exits': {'east': 'Forest River'},
        'item': 'pretty feather',
    },
    {
        'name': 'Old Fallen Tree',
        'exits': {'north': 'Forest River', 'east': 'Huge Fairy Tree'},
        'item': 'opal',
    },
    {
        'name': 'Small Clearing',
        'exits': {'west': 'Old Fallen Tree'},
        'item': 'exotic mushroom',
    },
]

layout3 = build_room_data(LAYOUT3_DEFS)
validate_layout(layout3)

# ---------------------------------------------------------------------------
# Layout 4
# ---------------------------------------------------------------------------
LAYOUT4_DEFS = [
    {
        'name': 'Weird Silver Trees',
        'exits': {'west': 'Mushroom Circle'},
        'item': 'silver leaf',
    },
    {
        'name': 'Mushroom Circle',
        'exits': {'east': 'Weird Silver Trees', 'south': 'Forest River'},
        'item': None,
    },
    {
        'name': 'Forest River',
        'exits': {'north': 'Mushroom Circle', 'east': 'Animal Trail',
                  'south': 'Old Fallen Tree', 'west': 'Huge Fairy Tree'},
        'item': 'river pebble',
    },
    {
        'name': 'Animal Trail',
        'exits': {'north': 'Small Clearing', 'west': 'Forest River'},
        'item': 'small bone',
    },
    {
        'name': 'Small Clearing',
        'exits': {'south': 'Animal Trail'},
        'item': 'exotic mushroom',
    },
    {
        'name': 'Huge Fairy Tree',
        'exits': {'east': 'Forest River'},
        'item': None,
    },
    {
        'name': 'Old Fallen Tree',
        'exits': {'north': 'Forest River', 'east': 'Huge Fairy Tree'},
        'item': 'opal',
    },
    {
        'name': 'Bird Nest Shrubs',
        'exits': {'west': 'Old Fallen Tree'},
        'item': 'pretty feather',
    },
]

layout4 = build_room_data(LAYOUT4_DEFS)
validate_layout(layout4)
