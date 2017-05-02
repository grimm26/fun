#!/usr/bin/env python3
import sys

DIRECTIONS = tuple(['west', 'north', 'east', 'south'])

def get_direction(turn_sum):
    return DIRECTIONS[turn_sum % 4]

def split_input(input):
    return input.split(", ")

def print_location_info(x,y):
    print("Total north movement (y coordinate) is {0}".format(y))
    print("Total east movement (x coordinate) is {0}".format(x))

    print("Total distance from start: {0}".format(abs(y) + abs(x)))
    print("We're at location {0},{1}".format(x,y))

def walkx(steps, x, y, travels):
    print("Walking {0} steps east-west from location {1},{2}.".format(steps,x,y))
    for i in list(range(abs(steps))):
        if steps > 0:
            x += 1
        else:
            x -= 1
        new_loc = "{0},{1}".format(x,y)
        print("Our new location after a step is {0}".format(new_loc))
        if new_loc in travels:
            print("We've visited a dupe location: {0}".format(new_loc))
            print_location_info(x,y)
            sys.exit(0)
        else:
            travels.append(new_loc)
    print("Done with this walk.")
    return travels

def walky(steps, x, y, travels):
    print("Walking {0} steps north-south from location {1},{2}.".format(steps,x,y))
    for i in list(range(abs(steps))):
        if steps > 0:
            y += 1
        else:
            y -= 1
        new_loc = "{0},{1}".format(x,y)
        print("Our new location after a step is {0}".format(new_loc))
        if new_loc in travels:
            print("We've visited a dupe location: {0}".format(new_loc))
            print_location_info(x,y)
            sys.exit(0)
        else:
            travels.append(new_loc)
    print("Done with this walk.")
    return travels

def calc_abs_movement(movement,travels,turn_sum):

    turn = movement[0]
    steps = movement[1:]
    
    if turn == 'R':
        turn_sum += 1
    elif turn == 'L':
        turn_sum  -= 1
    else:
        raise ValueError('Move is not L or R!')

    prev_x, prev_y = list(map(int,travels[-1].split(",")))
    direction = get_direction(turn_sum)
    if direction == 'north':
        travels = walky(int(steps), prev_x, prev_y, travels)
    elif direction == 'south':
        travels = walky(-int(steps), prev_x, prev_y,travels)
    elif direction == 'east':
        travels = walkx(int(steps), prev_x, prev_y, travels)
    elif direction == 'west':
        travels = walkx(-int(steps), prev_x, prev_y, travels)
    else:
        raise ValueError('Bad direction!')
    return travels,turn_sum

def main():
    input = "L4, L3, R1, L4, R2, R2, L1, L2, R1, R1, L3, R5, L2, R5, L4, L3, R2, R2, L5, L1, R4, L1, R3, L3, R5, R2, L5, R2, R1, R1, L5, R1, L3, L2, L5, R4, R4, L2, L1, L1, R1, R1, L185, R4, L1, L1, R5, R1, L1, L3, L2, L1, R2, R2, R2, L1, L1, R4, R5, R53, L1, R1, R78, R3, R4, L1, R5, L1, L4, R3, R3, L3, L3, R191, R4, R1, L4, L1, R3, L1, L2, R3, R2, R4, R5, R5, L3, L5, R2, R3, L1, L1, L3, R1, R4, R1, R3, R4, R4, R4, R5, R2, L5, R1, R2, R5, L3, L4, R1, L5, R1, L4, L3, R5, R5, L3, L4, L4, R2, R2, L5, R3, R1, R2, R5, L5, L3, R4, L5, R5, L3, R1, L1, R4, R4, L3, R2, R5, R1, R2, L1, R4, R1, L3, L3, L5, R2, R5, L1, L4, R3, R3, L3, R2, L5, R1, R3, L3, R2, L1, R4, R3, L4, R5, L2, L2, R5, R1, R2, L4, L4, L5, R3, L4"
# Need a method to calc sum of turns.  R = ++, L = --
    turn_sum = 1
    locations_visited = [ "0,0" ]
    for d in split_input(input):
        locations_visited,turn_sum = calc_abs_movement(d,locations_visited,turn_sum)

if __name__ == "__main__":
    main()
