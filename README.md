# ElementaryCelularAutomata
This program generates a simulation of the evolution of a one dimensional celullar automata with binary states. It consists in rules of a neighborhood that contains 3 cells with which 256 (2^8) diferent rulesets can be made. It is based on the Elemenetary Cellular Automata designed by Wolfram in 1983.

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
March, 2021
