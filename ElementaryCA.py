"""
Elementary Cellular Automata

This program generates a simulation of the evolution of a one dimensional celullar automata with binary states.
It consists in rules of a neighborhood that contains 3 cells with which 256 (2^8) diferent rulesets can be made.
It is based on the Elemenetary Cellular Automata designed by Wolfram in 1983.

FUNNY RULES*:
Common ones -> 30, 54, 60, 62, 90, 94, 102, 110, 122, 126, 150, 158, 182, 188, 190, 220, 222, 250
Cool ones -> 13, 69, 73, 99
Random ones -> 45, 75
White ones -> 129, 131, 133, 137, 147, 165, 177

BORING  RULES**:
Don't do nothing ones -> 0, 8, 32, 40, 64, 72, 96, 104, 128, 160, 168, 192, 200, 224, 232

*Actually, the funny part is to explore randomd different rules and see how much the cell behaviour can change
by just increasing a number.
** But let's be honest, these rules suck. At least, if you keep initial states of the cellular automata with 
only middle cell on.

Notes:
- Requires Numpy, OpenCV and Sys libraries
- The boundary condition are periodical, so the left boundry and right boundry of the cellular automata are linked.
- This video has a great explanation: https://www.youtube.com/watch?v=W1zKu3fDQR8&t=21s
- This links is useful and actually has images from all differenet rulsets:
https://mathworld.wolfram.com/ElementaryCellularAutomaton.html
- If you once find this code, I hope it is useful for you or at least have a bit of fun with the simulations.

by Daniel García Núñez
March 3rd, 2021
"""

import numpy as np
import cv2
import sys

class ElementaryCellularAutomata:

    def __init__(self, n, rule, numGenerations):
        self.n = n
        self.numGenerations = numGenerations
        self.cells = [0 for i in range(n)]
        self.cells[round(n/2)] = 1 # Arbitrary start with middle cell in state '1'
        self.getRuleset(rule)

    # Get ruleset from rule number
    def getRuleset(self, rule):
        bits = 8 # 256 different rules
        self.ruleset = [int(digit) for digit in bin(rule)[2:]]
        self.ruleset.reverse()  # Ruleset is kept inversed to match with array index
        self.ruleset.extend([0]*(bits-len(self.ruleset)))

    # Create all generations
    def generate(self):
        self.generations = [[0]*n for i in range(self.numGenerations)]
        self.generations[0] = self.cells
        neighbors = 2 # neighborhood of 3 cells
        leftNeighbors = int(np.floor(neighbors/2))
        rightNeighbors = int(np.ceil(neighbors/2))
        for idx, gen in enumerate(self.generations[1:]):
            for cell in range(self.n):
                if cell == 0:
                    neighborhood = [self.generations[idx][-leftNeighbors]]
                    neighborhood.extend(self.generations[idx][:rightNeighbors+1])
                elif cell == self.n-1:
                    neighborhood = self.generations[idx][cell-leftNeighbors:]
                    neighborhood.extend(self.generations[idx][:rightNeighbors])
                else:
                    neighborhood = self.generations[idx][cell-leftNeighbors : cell+rightNeighbors+1]    
                gen[cell] = self.ruleset[int("".join(str(c) for c in neighborhood),2)]

    # Print all generations in the command window
    def printResult(self):
        for gen in self.generations:
            line = ""
            for cell in gen:
                if cell:
                    line = line + '#'   # Cell state '1'
                else:
                    line = line + '_'   # Cell state '0'
            print(line)

    # Generate image
    def generateImage(self):
        pixels = 10 # length of the cells using pixels as units
        generations = np.array(self.generations)
        generations = generations.astype(np.uint8) * 255    # 0 - black, 255 - white
        self.image = np.zeros([pixels*self.numGenerations, pixels*self.n])
        for i, row in enumerate(self.image):
            for j in range(len(row)):
                self.image[i][j] = generations[int(np.floor(i/pixels))][int(np.floor(j/pixels))]

    # Display image of full generations
    def display(self):
        if not(hasattr(self, "image")):
            self.generateImage()
        windowName = 'Elemental Cellular Automata'
        cv2.imshow(windowName, self.image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    # Display simulation
    def runSimulation(self):
        if not(hasattr(self, "image")):
            self.generateImage()
        sim = np.zeros_like(self.image)
        windowName = 'Elemental Cellular Automata'
        for i in range(10, len(sim), 10):
            sim[-i:] = self.image[:i]
            cv2.imshow(windowName, sim)
            key = cv2.waitKey(500)
            if key == 27: #if ESC is pressed, the simulation ends
                break
        cv2.waitKey(0)
        cv2.destroyAllWindows()


# Set inputs from command arguments, or set default if any argument is defined
def getInputArguments(inputs):
    if len(inputs) == 0:
        return 100, 50, 30
    elif len(inputs) < 3:
        print('Missing arguments. Input arguments to define the amount of cells and generations and rule number are expected.')
    elif len(inputs) > 3:
        print('More arguments than expected. Only expected values for amount of cells, generations and  rule number.')
    else:
        try:
            [n, numGenerations, rule] = [int(x) for x in inputs]
            return n, numGenerations, rule
        except:
            print('Something went wrong. Verify all input arguments are integers.')
    return -1, -1, -1


if __name__ == "__main__":

    [n, numGenerations, rule] = getInputArguments(sys.argv[1:])

    if n != -1:
        print('Number of cells: ' + str(n))
        print('Number of generations: ' + str(numGenerations))
        print('Rule : ' + str(rule))

        CA = ElementaryCellularAutomata(n, rule, numGenerations)
        CA.generate()
        CA.runSimulation()