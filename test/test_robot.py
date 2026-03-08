from src.services.robot_service import calculate_unique_places


class MockCommand:
    def __init__(self, direction, steps):
        self.direction = direction
        self.steps = steps


def test_single_command():
    commands = [MockCommand("east", 2)]
    # Start + 2 steps = 3 unique places
    assert calculate_unique_places(10, 22, commands) == 3


def test_overlapping_path():
    commands = [MockCommand("east", 2), MockCommand("west", 2)]
    # Moves east 2, then west 2 over the exact same path.
    # Should only be 3 unique places.
    assert calculate_unique_places(0, 0, commands) == 3


def test_circular_path():
    commands = [
        MockCommand("north", 1),
        MockCommand("east", 1),
        MockCommand("south", 1),
        MockCommand("west", 1),
    ]
    # Forms a 1x1 square. (0,0), (0,1), (1,1), (1,0) = 4 unique points
    assert calculate_unique_places(0, 0, commands) == 4
