# Import necessary libraries
import random
fruit_position = [0, 0]


def get_fruit_position(window_x, window_y):
    """Generate a random position for the fruit within the game window."""
    return [random.randrange(1, (window_x // 10)) * 10,
            random.randrange(1, (window_y // 10)) * 10]


def reset_fruit_position(window_x, window_y):
    """Reset the fruit position to a new random location."""
    global fruit_position
    fruit_position = get_fruit_position(window_x, window_y)
    return fruit_position
