import bisect
from collections import defaultdict


def calculate_unique_places(start_x: int, start_y: int, commands: list) -> int:
    horizontal_lines = defaultdict(list)
    vertical_lines = defaultdict(list)

    current_x, current_y = start_x, start_y

    # Add the starting point as a baseline 0-length horizontal line
    horizontal_lines[current_y].append([current_x, current_x])

    # 1. Map all movements to intervals
    for cmd in commands:
        direction = cmd.direction.lower()
        steps = cmd.steps

        if direction == "east":
            horizontal_lines[current_y].append([current_x, current_x + steps])
            current_x += steps
        elif direction == "west":
            horizontal_lines[current_y].append([current_x - steps, current_x])
            current_x -= steps
        elif direction == "north":
            vertical_lines[current_x].append([current_y, current_y + steps])
            current_y += steps
        elif direction == "south":
            vertical_lines[current_x].append([current_y - steps, current_y])
            current_y -= steps

    def merge_intervals(intervals):
        if not intervals:
            return []
        intervals.sort(key=lambda item: item[0])
        merged = [intervals[0]]
        for current in intervals[1:]:
            last = merged[-1]
            if current[0] <= last[1]:
                last[1] = max(last[1], current[1])
            else:
                merged.append(current)
        return merged

    merged_h = {
        y: merge_intervals(intervals) for y, intervals in horizontal_lines.items()
    }
    merged_v = {
        x: merge_intervals(intervals) for x, intervals in vertical_lines.items()
    }

    total_unique = 0
    events = []

    # 2. Process Horizontal Lines
    for y, intervals in merged_h.items():
        for x1, x2 in intervals:
            total_unique += x2 - x1 + 1
            # Event Type 1: Horizontal Line
            events.append((y, 1, x1, x2))

    # 3. Process Vertical Lines
    for x, intervals in merged_v.items():
        for y1, y2 in intervals:
            total_unique += y2 - y1 + 1
            # Event Type 0: Start of Vertical Line
            events.append((y1, 0, x, x))
            # Event Type 2: End of Vertical Line
            events.append((y2, 2, x, x))

    # 4. Sort Events (Sweep Line moving bottom to top)
    # Order of processing at the exact same Y coordinate is critical:
    # Start V-Line (0) -> Process H-Line (1) -> End V-Line (2)
    events.sort(key=lambda e: (e[0], e[1]))

    active_x = []
    intersections = 0

    # 5. Execute Sweep Line
    for event in events:
        y = event[0]
        typ = event[1]

        if typ == 0:
            # Vertical line starts: insert its X coordinate into the active list
            bisect.insort(active_x, event[2])
        elif typ == 2:
            # Vertical line ends: remove its X coordinate
            idx = bisect.bisect_left(active_x, event[2])
            if idx < len(active_x) and active_x[idx] == event[2]:
                active_x.pop(idx)
        elif typ == 1:
            # Horizontal line: perfectly count how many active vertical lines it crosses
            x1, x2 = event[2], event[3]
            idx1 = bisect.bisect_left(active_x, x1)
            idx2 = bisect.bisect_right(active_x, x2)
            intersections += idx2 - idx1

    return total_unique - intersections
