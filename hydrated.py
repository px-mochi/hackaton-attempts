def calc_manhatten_dist(bottle_pos, item_pos):
    if bottle_pos[0] >= item_pos[0] and bottle_pos[0] <= item_pos[2]:
        # Distance will be a straight line along the Y axis
        dist = min(abs(item_pos[1]-bottle_pos[1]), abs(item_pos[3]-bottle_pos[1]))
    elif bottle_pos[1] >= item_pos[1] and bottle_pos[1] <= item_pos[3]:
        # Distance will be a straight line along the X asis
        dist = min(abs(item_pos[0]-bottle_pos[0]), abs(item_pos[2]-bottle_pos[0]))
    
    elif abs(item_pos[0] - bottle_pos[0]) < abs(item_pos[2] - bottle_pos[0]):
        dist = min(abs(item_pos[0] - bottle_pos[0]) + abs(item_pos[1] - bottle_pos[1]),\
                abs(item_pos[0] - bottle_pos[0]) + abs(item_pos[3] - bottle_pos[1]),
                )
    else:
        dist = min(abs(item_pos[2] - bottle_pos[0]) + abs(item_pos[1] - bottle_pos[1]),\
                abs(item_pos[2] - bottle_pos[0]) + abs(item_pos[3] - bottle_pos[1])
                )

    # elif abs(item_pos[0] - bottle_pos[0]) < abs(item_pos[2] - bottle_pos[0]):  # Left X is nearest
    #     # Source: https://www.omnicalculator.com/math/manhattan-distance#what-is-the-formula-for-the-manhattan-distance
    #     # d = |a1-b1| + |a2-b2|
        
    #     if abs(item_pos[1] - bottle_pos[1]) < abs(item_pos[3] - bottle_pos[1]):  # Bottom left corner is nearest
    #         dist = abs(item_pos[0] - bottle_pos[0]) + abs(item_pos[1] - bottle_pos[1])
    #     else:  # Top left corner is nearest
    #         dist = abs(item_pos[0] - bottle_pos[0]) + abs(item_pos[3] - bottle_pos[1])

    # else:  # Right X is nearest
    #     if abs(item_pos[1] - bottle_pos[1]) < abs(item_pos[3] - bottle_pos[1]):  # Bottom right corner is nearest
    #         dist = abs(item_pos[2] - bottle_pos[0]) + abs(item_pos[1] - bottle_pos[1])
    #     else:  # Top Right corner is nearest
    #         dist = abs(item_pos[2] - bottle_pos[0]) + abs(item_pos[3] - bottle_pos[1])
        
    return dist

def testing(furnitures):
    min_x = 1000000000
    max_x = -1000000000

    min_y = 1000000000
    max_y = -1000000000

    for furniture in furnitures:
        if furniture[0] < min_x:  # x1
            min_x = furniture[0]
        if furniture[1] < min_y:  # y1
            min_y = furniture[1]
        if furniture[2] > max_x:  # x2
            max_x = furniture[2]
        if furniture[3] > max_y:  # y2
            max_y = furniture[3]
        
    ## Brute forcing the seach process
    min_distance = abs(-1000000000 - 1000000000) + abs(-1000000000 - 1000000000)
    min_dist_x = None
    min_dist_y = None
    for x_loc in range(min_x, max_x+1):
        for y_loc in range(min_y, max_y+1):
            total_distances = 0
            bottle_pos = (x_loc, y_loc)
            for furniture in furnitures:  # Urgh too many loops
                item_distance = calc_manhatten_dist(bottle_pos, furniture)
                total_distances += item_distance
            if total_distances < min_distance:
                min_distance = total_distances
                min_dist_x = x_loc
                min_dist_y = y_loc
            
            # Debug
            # if x_loc == 0 and y_loc == 3:
            #     print(f"({x_loc},{y_loc}) total_distances = {total_distances}")
            # if x_loc == 1 and y_loc == 3:
            #     print(f"({x_loc},{y_loc}) total_distances = {total_distances}")
    
    return min_dist_x, min_dist_y

def main():
    T = int(input())  # Number of test cases
    test_case_num = 1

    for test_case in range(T):
        K = int(input())  # Num. Objects in room
        
        furnitures = []
        for _ in range(K):
            line = input()
            #  xi,1, yi,1, xi,2, yi,2 (1 = Bottom left, 2 Top Right)
            furniture = [int(i) for i in line.split()]
            furnitures.append(furniture)
        
        x, y  = testing(furnitures)
        print(f"Case #{test_case_num}: {x} {y}")
        test_case_num += 1

if __name__ == "__main__":
    main()