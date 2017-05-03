#!/user/bin/env python3

class Keypad:
    NEIGHBORS = {
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


    def __init__(self, button="five"):
        self.button = button

    def move(self, direction):
        self.button = self.neighbor(direction)

    def neighbor(self, direction):
        if direction in self.NEIGHBORS[self.button]:
            return self.NEIGHBORS[self.button][direction]
        else:
            return self.button

    def button(self):
        return self.button
