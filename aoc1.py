#!/usr/bin/env python3

def get_direction(turn_sum):
    directions = tuple(['west', 'north', 'east', 'south'])
    return directions[turn_sum % 4]

def split_input(input):
    return input.split(", ")

def calc_abs_movement(movement):
    global abs_travel
    global turn_sum

    turn = movement[0]
    steps = movement[1:]
    
    if turn[0] == 'R':
        turn_sum += 1
    elif turn[0] == 'L':
        turn_sum  -= 1
    else:
        raise ValueError('Move is not L or R!')
    dir = get_direction(turn_sum)
    if dir == 'north':
        abs_travel['northsouth'] += int(steps)
    elif dir == 'south':
        abs_travel['northsouth'] -= int(steps)
    elif dir == 'east':
        abs_travel['eastwest'] += int(steps)
    elif dir == 'west':
        abs_travel['eastwest'] -= int(steps)
    else:
        raise ValueError('Bad direction!')


input = "L4, L3, R1, L4, R2, R2, L1, L2, R1, R1, L3, R5, L2, R5, L4, L3, R2, R2, L5, L1, R4, L1, R3, L3, R5, R2, L5, R2, R1, R1, L5, R1, L3, L2, L5, R4, R4, L2, L1, L1, R1, R1, L185, R4, L1, L1, R5, R1, L1, L3, L2, L1, R2, R2, R2, L1, L1, R4, R5, R53, L1, R1, R78, R3, R4, L1, R5, L1, L4, R3, R3, L3, L3, R191, R4, R1, L4, L1, R3, L1, L2, R3, R2, R4, R5, R5, L3, L5, R2, R3, L1, L1, L3, R1, R4, R1, R3, R4, R4, R4, R5, R2, L5, R1, R2, R5, L3, L4, R1, L5, R1, L4, L3, R5, R5, L3, L4, L4, R2, R2, L5, R3, R1, R2, R5, L5, L3, R4, L5, R5, L3, R1, L1, R4, R4, L3, R2, R5, R1, R2, L1, R4, R1, L3, L3, L5, R2, R5, L1, L4, R3, R3, L3, R2, L5, R1, R3, L3, R2, L1, R4, R3, L4, R5, L2, L2, R5, R1, R2, L4, L4, L5, R3, L4"
# Need a method to calc sum of turns.  R = ++, L = --
turn_sum = 1
abs_travel =  { 'eastwest': 0, 'northsouth': 0 }
for d in split_input(input):
    calc_abs_movement(d)
print("Total north movement is %d" % abs_travel['northsouth'])
print("Total east movement is %d" % abs_travel['eastwest'])

print("Total distance from start: %d" % (abs(abs_travel['northsouth']) + abs(abs_travel['eastwest'])))
