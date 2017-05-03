#!/usr/bin/env python3

from keypad import *
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--file", help="File with the list of directions to use", required=True)
args = parser.parse_args()

file = open(args.file,"r")
k = Keypad()
i=1
print("Numeric keypad result:")
for line in file:
    for char in line.rstrip():
        k.move(char)
    print("button {0} is {1}".format(i, k.button))
    i += 1
print("Goofy keypad result:")
i=1
g = Keypad("goofy")
file = open(args.file,"r")
for line in file:
    for char in line.rstrip():
        g.move(char)
    print("button {0} is {1}".format(i, g.button))
    i += 1
