import copy
import random
from fae_dicts import layout1, layout2, layout3, layout4

LAYOUT_OPTIONS = [layout1, layout2, layout3, layout4]

def generate_player_map():
    """Return a deep copy of a randomly chosen room layout."""
    return copy.deepcopy(random.choice(LAYOUT_OPTIONS))