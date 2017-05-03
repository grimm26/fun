#!/user/bin/env python3

class Keypad:
    NUMERIC_NEIGHBORS = {
            "one": {
                "D": "four",
                "R": "two"
                },
            "two": {
                "D": "five",
                "R": "three",
                "L": "one"
                },
            "three": {
                "D": "six",
                "L": "two"
                },
            "four": {
                "U": "one",
                "D": "seven",
                "R": "five"
                },
            "five": {
                "U": "two",
                "D": "eight",
                "R": "six",
                "L": "four"
                },
            "six": {
                "U": "three",
                "D": "nine",
                "L": "five"
                },
            "seven": {
                "U": "four",
                "R": "eight"
                },
            "eight": {
                "U": "five",
                "R": "nine",
                "L": "seven"
                },
            "nine": {
                "U": "six",
                "L": "eight"
                }
            }
    GOOFY_NEIGHBORS = {
            "one": {
                "D": "three"
                },
            "two": {
                "D": "six",
                "R": "three"
                },
            "three": {
                "U": "one",
                "D": "seven",
                "R": "four",
                "L": "two"
                },
            "four": {
                "D": "eight",
                "L": "three"
                },
            "five": {
                "R": "six"
                },
            "six": {
                "U": "two",
                "D": "A",
                "R": "seven",
                "L": "five"
                },
            "seven": {
                "U": "three",
                "D": "B",
                "R": "eight",
                "L": "six"
                },
            "eight": {
                "U": "four",
                "D": "C",
                "R": "nine",
                "L": "seven"
                },
            "nine": {
                "L": "eight"
                },
            "A": {
                "U": "six",
                "R": "B",
                },
            "B": {
                "U": "seven",
                "R": "C",
                "L": "A",
                "D": "D"
                },
            "C": {
                "U": "eight",
                "L": "B"
                },
            "D": {
                "U": "B"
                }
            }

    def __init__(self, layout="numeric"):
        self.button = "five"
        self.layout = layout

    def move(self, direction):
        if self.layout == "numeric":
            self.button = self.numeric_neighbor(direction)
        elif self.layout == "goofy":
            self.button = self.goofy_neighbor(direction)

    def numeric_neighbor(self, direction):
        if direction in self.NUMERIC_NEIGHBORS[self.button]:
            return self.NUMERIC_NEIGHBORS[self.button][direction]
        else:
            return self.button

    def goofy_neighbor(self, direction):
        if direction in self.GOOFY_NEIGHBORS[self.button]:
            return self.GOOFY_NEIGHBORS[self.button][direction]
        else:
            return self.button

    def button(self):
        return self.button
