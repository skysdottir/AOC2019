def manhattan(x, y):
    return abs(x) + abs(y)

def closest_intersection(vect, candidates):
    closest = 999999
    u, v_a, v_b = vect
    v_min = min(v_a, v_b)
    v_max = max(v_a, v_b)

    for cand in candidates:
        c_v, c_u_a, c_u_b = cand
        c_u_min = min(c_u_a, c_u_b)
        c_u_max = max(c_u_a, c_u_b)

        if (v_min <= c_v <= v_max and c_u_min <= u <= c_u_max and (manhattan(c_v, u) > 0)):
            print("found intersection at (u,v) (%i, %i)" % (u, c_v))
            closest = min(closest, manhattan(c_v, u))
    
    return closest


with open("Day03/input.txt", "r") as input:
    # We're going to use cartesian coords here - upwards is +y, right is +x

    rows = []
    cols = []

    first = input.readline().split(",")

    x = y = 0

    for move in first:
        dir = move[0]
        dist = int(move[1:])

        if ((dir == "D") | (dir == "L")):
            dist *= -1
        
        if ((dir == "U") | (dir == "D")):
            # It's a column!
            cols.append((x, y, y+dist))
            y += dist
        elif ((dir == "L") | (dir == "R")):
            # It's a row!
            rows.append((y, x, x+dist))
            x += dist

    print("rows: " + str(rows))
    print("cols: " + str(cols))

    second = input.readline().split(",")

    # housekeeping's going to look really familiar, here
    x = y = 0
    closest = 999999

    for move in second:
        dir = move[0]
        dist = int(move[1:])

        if ((dir == "D") | (dir == "L")):
            dist *= -1
        
        if ((dir == "U") | (dir == "D")):
            # It's a column!
            print("looking for row intersection with (%i, %i, %i)" % (x, y, y+dist))
            closest = min(closest, closest_intersection((x, y, y+dist), rows))
            y += dist
        elif ((dir == "L") | (dir == "R")):
            # It's a row!
            print("looking for column intersection with (%i, %i, %i)" % (y, x, x+dist))
            closest = min(closest, closest_intersection((y, x, x+dist), cols))
            x += dist

    print("And if that worked, the closest intersection is at distance %i" % closest)