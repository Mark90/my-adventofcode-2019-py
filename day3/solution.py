def is_vertical(l):
    return l[0][0] == l[1][0]


def x_from_a_between_b(line_a, line_b):
    return line_b[0][0] < line_a[0][0] < line_b[1][0]


def y_from_a_between_b(line_a, line_b):
    return line_b[0][1] < line_a[0][1] < line_b[1][1]


def lines_intersect_at(line1, line2):
    """Returns the intersection between two lines, if any.
    There's probably a smarter way to do this... oh well."""
    if is_vertical(line1) and not is_vertical(line2):
        if y_from_a_between_b(line2, line1) and x_from_a_between_b(line1, line2):
            return line1[0][0], line2[0][1]
    elif is_vertical(line2) and not is_vertical(line1):
        if y_from_a_between_b(line1, line2) and x_from_a_between_b(line2, line1):
            return line2[0][0], line1[0][1]


def generate_lines(path):
    """Parse the path instructions and yield each line as a tuple of 2 coordinates.
    The coordinate closest to the origin is returned first, to simplify the rest
    of the program easier."""
    xstart, ystart = 0, 0
    for item in path.split(","):
        direction, distance = item[0], int(item[1:])
        xstop, ystop = xstart, ystart
        if direction == "R":
            xstop += distance
            yield (xstart, ystart), (xstop, ystop)
        elif direction == "U":
            ystop += distance
            yield (xstart, ystart), (xstop, ystop)
        elif direction == "L":
            xstop -= distance
            yield (xstop, ystop), (xstart, ystart)
        elif direction == "D":
            ystop -= distance
            yield (xstop, ystop), (xstart, ystart)
        xstart, ystart = xstop, ystop


def md(coord):
    return abs(coord[0]) + abs(coord[1])


def part1(lines):
    path1, path2 = lines[:2]
    lines1, lines2 = list(generate_lines(path1)), list(generate_lines(path2))
    closest_intersection = None
    for line1 in lines1:
        for line2 in lines2:
            coord = lines_intersect_at(line1, line2)
            if not coord:
                continue
            if not closest_intersection or md(coord) < md(closest_intersection):
                closest_intersection = coord
    print(f"[part1] Closest coord is {closest_intersection} with MD:", md(closest_intersection))


def generate_lines_withsteps(path):
    """Same as generate_lines, but instead of only the coordinates also yield the
    number of steps taken until this coordinate, and the direction in which the
    line travels."""
    xstart, ystart = 0, 0
    steps = 0
    for item in path.split(","):
        direction, distance = item[0], int(item[1:])
        xstop, ystop = xstart, ystart
        if direction == "R":
            xstop += distance
            yield ((xstart, ystart), (xstop, ystop)), steps, direction
        elif direction == "U":
            ystop += distance
            yield ((xstart, ystart), (xstop, ystop)), steps, direction
        elif direction == "L":
            xstop -= distance
            yield ((xstop, ystop), (xstart, ystart)), steps, direction
        elif direction == "D":
            ystop -= distance
            yield ((xstop, ystop), (xstart, ystart)), steps, direction
        xstart, ystart = xstop, ystop
        steps += distance


def steps_to_coord(direction, coord, line):
    if direction == "R":
        return coord[0] - line[0][0]
    if direction == "L":
        return line[1][0] - coord[0]
    if direction == "U":
        return coord[1] - line[0][1]
    if direction == "D":
        return line[1][1] - coord[1]


def part2(lines):
    path1, path2 = lines[:2]
    path1lines, path2lines = list(generate_lines_withsteps(path1)), list(generate_lines_withsteps(path2))
    for line1, steps_until_line1, line1_direction in path1lines:
        for line2, steps_until_line2, line2_direction in path2lines:
            coord = lines_intersect_at(line1, line2)
            if not coord:
                continue
            print(
                "[part2] Fewest steps until intersection:",
                steps_until_line1
                + steps_until_line2
                + steps_to_coord(line1_direction, coord, line1)
                + steps_to_coord(line2_direction, coord, line2),
            )
            return
