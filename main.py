def direction(facing, turn):
    directions = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']
    turns = turn // 45
    start = directions.index(facing)
    pos = (start + turns) % len(directions)
    return directions[pos]
