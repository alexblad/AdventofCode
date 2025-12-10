import time

input = open("input.txt").read().splitlines()

# # Part 1 Check grid for accessible paper rolls
grid = []
for line in input:
    positions = []
    for c in line:
        positions.append(c)
    grid.append(positions)

# paper_count = 0
# GREEN = '\033[92m'
# RESET = '\033[0m'

# for y in range(len(grid)):
#     for x in range(len(grid[y])):
#         time.sleep(0.002)
#         if grid[y][x] == "@":
#             adjacent_count = 0
#             # Check 8 adjacent gridpoints
#             neighbors = [
#                 (x-1, y-1), (x, y-1), (x+1, y-1),
#                 (x-1, y),             (x+1, y),
#                 (x-1, y+1), (x, y+1), (x+1, y+1)
#             ]
            
#             for nx, ny in neighbors:
#                 # If any x is less than zero or greater than the range of y, skip
#                 # If any y is less than 0, or greater than the len of grid, skip
#                 if nx < 0 or nx >= len(grid[y]) or ny < 0 or ny >= len(grid):
#                     continue
                
#                 # If all coordinates are valid, check for an "@" symbol
#                 if grid[ny][nx] == "@":
#                     adjacent_count += 1
                
#                 # If the adjacent count becomes greater than 3, skip
#                 if adjacent_count > 3:
#                     break
            
#             # If the adjacent count is equal to or less than 3, add one to the paper count
#             if adjacent_count <= 3:
#                 paper_count += 1
#                 print(f"{GREEN}@{RESET}", end="", flush=True)
#             else:
#                 print("@", end="", flush=True)
#         else:
#             print(grid[y][x], end="", flush=True)
#     print()

# print(paper_count)

# Part 2 Check how many paper rolls can be removed
removed_count = 0
pass_num = 0

while True:
    removed_in_pass = 0
    direction = pass_num % 4
    
    # Define iteration ranges
    if direction == 0: # TL -> BR
        y_range = range(len(grid))
        x_range = range(len(grid[0]))
    elif direction == 1: # BR -> TL
        y_range = range(len(grid)-1, -1, -1)
        x_range = range(len(grid[0])-1, -1, -1)
    elif direction == 2: # TR -> BL
        y_range = range(len(grid))
        x_range = range(len(grid[0])-1, -1, -1)
    elif direction == 3: # BL -> TR
        y_range = range(len(grid)-1, -1, -1)
        x_range = range(len(grid[0]))
        
    # print(f"Pass {pass_num + 1} (Direction {direction})")
    
    for y in y_range:
        for x in x_range:
            # time.sleep(0.001)
            
            if grid[y][x] == "@":
                adjacent_count = 0
                neighbors = [
                    (x-1, y-1), (x, y-1), (x+1, y-1),
                    (x-1, y),             (x+1, y),
                    (x-1, y+1), (x, y+1), (x+1, y+1)
                ]
                
                for nx, ny in neighbors:
                    if nx < 0 or nx >= len(grid[0]) or ny < 0 or ny >= len(grid):
                        continue
                    if grid[ny][nx] == "@":
                        adjacent_count += 1
                    if adjacent_count > 3:
                        break
                
                if adjacent_count <= 3:
                    grid[y][x] = "."
                    removed_count += 1
                    removed_in_pass += 1
                    # print(f"{GREEN}@{RESET}", end="", flush=True)
                else:
                    # print("@", end="", flush=True)
                    pass
            else:
                # print(grid[y][x], end="", flush=True)
                pass
        # print()
        
    if removed_in_pass == 0:
        break
    pass_num += 1

print(f"Total removed in Part 2: {removed_count}")

    


