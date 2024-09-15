from Maze_Generator import WilsonsAlgorithm

w = WilsonsAlgorithm()

while True:
    path = w.loop_erased_random_walk()
    w.drawMaze()