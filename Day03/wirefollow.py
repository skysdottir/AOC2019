def manhattan(x, y):
    return abs(x) + abs(y)

def closest_intersection(vect, candidates):
    closest = 999999
    u, v_a, v_b, vect_t = vect
    v_min = min(v_a, v_b)
    v_max = max(v_a, v_b)

    for cand in candidates:
        c_v, c_u_a, c_u_b, cand_t = cand
        c_u_min = min(c_u_a, c_u_b)
        c_u_max = max(c_u_a, c_u_b)

        if (v_min <= c_v <= v_max and c_u_min <= u <= c_u_max and (manhattan(c_v, u) > 0)):
            print("found intersection at (u,v) (%i, %i)" % (u, c_v))

            # brace yourself - that is to say, the distance to each start point (the 'a' points),
            # plus the distance down each edge here from the start point to the intersection.
            total_dist = vect_t + abs(v_a - c_v) + cand_t + abs(c_u_a - u)
            closest = min(closest, total_dist)
    
    return closest


with open("Day03/input.txt", "r") as input:
    # We're going to use cartesian coords here - upwards is +y, right is +x

    rows = []
    cols = []

    first = input.readline().split(",")

    x = y = traveled = 0

    for move in first:
        dir = move[0]
        dist = int(move[1:])

        if ((dir == "D") | (dir == "L")):
            dist *= -1
        
        if ((dir == "U") | (dir == "D")):
            # It's a column!
            cols.append((x, y, y+dist, traveled))
            y += dist
        elif ((dir == "L") | (dir == "R")):
            # It's a row!
            rows.append((y, x, x+dist, traveled))
            x += dist
        
        traveled += (abs(dist))

    print("rows: " + str(rows))
    print("cols: " + str(cols))

    second = input.readline().split(",")

    # housekeeping's going to look really familiar, here
    x = y = traveled = 0
    closest = 999999

    for move in second:
        dir = move[0]
        dist = int(move[1:])

        if ((dir == "D") | (dir == "L")):
            dist *= -1
        
        if ((dir == "U") | (dir == "D")):
            # It's a column!
            print("looking for row intersection with (%i, %i, %i)" % (x, y, y+dist))
            closest = min(closest, closest_intersection((x, y, y+dist, traveled), rows))
            y += dist
        elif ((dir == "L") | (dir == "R")):
            # It's a row!
            print("looking for column intersection with (%i, %i, %i)" % (y, x, x+dist))
            closest = min(closest, closest_intersection((y, x, x+dist, traveled), cols))
            x += dist
        
        traveled += (abs(dist))

    print("And if that worked, the closest intersection is at distance %i" % closest)