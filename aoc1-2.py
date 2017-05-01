#!/usr/bin/env python3
import sys

def get_direction(turn_sum):
    directions = tuple(['west', 'north', 'east', 'south'])
    return directions[turn_sum % 4]

def split_input(input):
    return input.split(", ")

def calc_abs_movement(movement):
    global abs_travel
    global turn_sum
    global locations_visited

    turn = movement[0]
    steps = movement[1:]
    
    if turn == 'R':
        turn_sum += 1
    elif turn == 'L':
        turn_sum  -= 1
    else:
        raise ValueError('Move is not L or R!')

    prev_x, prev_y = list(map(int,locations_visited[-1].split(",")))
    dir = get_direction(turn_sum)
    if dir == 'north':
        abs_travel['northsouth'] += int(steps)
        prev_y += int(steps)
    elif dir == 'south':
        abs_travel['northsouth'] -= int(steps)
        prev_y -= int(steps)
    elif dir == 'east':
        abs_travel['eastwest'] += int(steps)
        prev_x += int(steps)
    elif dir == 'west':
        abs_travel['eastwest'] -= int(steps)
        prev_x -= int(steps)
    else:
        raise ValueError('Bad direction!')

    return "{0},{1}".format(prev_x,prev_y)

def print_location_info(travel):
    print("Total north movement (y coordinate) is {0}".format(abs_travel['northsouth']))
    print("Total east movement (x coordinate) is {0}".format(abs_travel['eastwest']))

    print("Total distance from start: {0}".format(abs(abs_travel['northsouth']) + abs(abs_travel['eastwest'])))
    print("We're at location {0},{1}".format(abs_travel['eastwest'],abs_travel['northsouth']))

input = "L4, L3, R1, L4, R2, R2, L1, L2, R1, R1, L3, R5, L2, R5, L4, L3, R2, R2, L5, L1, R4, L1, R3, L3, R5, R2, L5, R2, R1, R1, L5, R1, L3, L2, L5, R4, R4, L2, L1, L1, R1, R1, L185, R4, L1, L1, R5, R1, L1, L3, L2, L1, R2, R2, R2, L1, L1, R4, R5, R53, L1, R1, R78, R3, R4, L1, R5, L1, L4, R3, R3, L3, L3, R191, R4, R1, L4, L1, R3, L1, L2, R3, R2, R4, R5, R5, L3, L5, R2, R3, L1, L1, L3, R1, R4, R1, R3, R4, R4, R4, R5, R2, L5, R1, R2, R5, L3, L4, R1, L5, R1, L4, L3, R5, R5, L3, L4, L4, R2, R2, L5, R3, R1, R2, R5, L5, L3, R4, L5, R5, L3, R1, L1, R4, R4, L3, R2, R5, R1, R2, L1, R4, R1, L3, L3, L5, R2, R5, L1, L4, R3, R3, L3, R2, L5, R1, R3, L3, R2, L1, R4, R3, L4, R5, L2, L2, R5, R1, R2, L4, L4, L5, R3, L4"
# Need a method to calc sum of turns.  R = ++, L = --
turn_sum = 1
abs_travel =  { 'eastwest': 0, 'northsouth': 0 }
locations_visited = [ "0,0" ]
for d in split_input(input):
    new_loc = calc_abs_movement(d)
    if new_loc in locations_visited:
        print("We've visited a dupe location: {0}".format(new_loc))
        print_location_info(abs_travel)
        sys.exit(0)
    else:
        locations_visited.append(new_loc)
