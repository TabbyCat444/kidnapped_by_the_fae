# Kidnapped By The Fae

A simple text-based adventure game about being kidnapped by the fae and trying to find your way home.

## Story

You stepped into a mushroom circle while strolling through the woods and now you have found yourself in the fairy kingdom. A small fairy kindly provides you with a few tips when you ask where you are and how to get home.

You must find the **Fairy King** deep in the strange woods and plead your case to go back home. But do not go empty-handed — you must collect **six gifts** to appease him:

- A silver leaf
- A river pebble
- A small bone
- An exotic mushroom
- A pretty feather
- An opal

If you try to convince the Fairy King to release you without these gifts, you will be stuck in the fairy kingdom forever.

## How to Play

### Prerequisites

- Python 3.x

### Running the Game

```bash
python main.py
```

### Commands

| Command | Description |
| :--- | :--- |
| `go north` | Move north |
| `go east` | Move east |
| `go south` | Move south |
| `go west` | Move west |
| `collect <item name>` | Pick up an item in the current room |
| `exit` | Quit the game |

### Example

```text
Welcome to the Fairy Kingdom! You are in the Mushroom Circle.
Inventory: []
What would you like to do? go east
You are at the Weird Silver Trees.
You see a silver leaf.
Inventory: []
What would you like to do? collect silver leaf
You got a silver leaf!
Inventory: ['silver leaf']
```

## Game Mechanics

* **Randomized layouts:** Each time you start the game, one of four different room layouts is chosen at random. The rooms, exits, and item locations change, giving you a different experience on every playthrough.
* **Six collectible items** are scattered across the map. You must find all of them before reaching the Fairy King.
* **No backtracking required** — once you collect an item, it stays in your inventory.
* **Win condition:** Reach the Huge Fairy Tree with all six items.
* **Lose condition:** Reach the Huge Fairy Tree with fewer than six items.

## Project Structure

```text
.
├── main.py           # Entry point; orchestrates game flow
├── game_config.py    # Layout selection logic
├── fae_dicts.py      # Room definitions and layout data
├── fae_funcs.py      # Story, instructions, and game loop
└── README.md         # This file
```

## Module Responsibilities

| File | Responsibility |
| :--- | :--- |
| `main.py` | Game orchestrator — starts the story, instructions, and game loop |
| `game_config.py` | Selects a random layout at game start |
| `fae_dicts.py` | Defines room data and provides helpers to build and validate layouts |
| `fae_funcs.py` | Contains the story, instructions, and main game loop |

## Development

### Adding a New Layout

1. Add a new `LAYOUTX_DEFS` list in `fae_dicts.py` using the structured room format:

```python
LAYOUT5_DEFS = [
    {
        'name': 'Room Name',
        'exits': {'north': 'Adjacent Room', 'south': 'Another Room'},
        'item': 'item name',   # or None if the room has no item
    },
    # ... more rooms
]
```

1. Build and validate the layout:

```python
layout5 = build_room_data(LAYOUT5_DEFS)
validate_layout(layout5)
```

2. Add `layout5` to the `LAYOUT_OPTIONS` list in `game_config.py`.

### Running Validation

The `validate_layout()` function checks that every room in a layout is reachable from the starting room (`Mushroom Circle`). If a layout is broken, it raises a `ValueError` at module import time.

## Tech Stack

* **Language:** Python 3
* **No external dependencies** — the game runs with only the Python standard library.

## License

This project is open source and available for personal and educational use.
