def calculate_unique_places(start_x: int, start_y: int, commands: list) -> int:
    visited = set()
    current_x, current_y = start_x, start_y

    # Add starting position
    visited.add((current_x, current_y))

    for cmd in commands:
        direction = cmd.direction.lower()
        steps = cmd.steps

        for _ in range(steps):
            if direction == "north":
                current_y += 1
            elif direction == "south":
                current_y -= 1
            elif direction == "east":
                current_x += 1
            elif direction == "west":
                current_x -= 1

            visited.add((current_x, current_y))

    # The robot reports the number of unique places cleaned [cite: 11]
    return len(visited)
