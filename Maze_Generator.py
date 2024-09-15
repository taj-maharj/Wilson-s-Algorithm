import pygame, random, sys

WIDTH, HEIGHT = 800, 800
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

pygame.init()

class WilsonsAlgorithm:

    def __init__(self) -> None:
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.rows = 20
        self.columns = 20
        self.boxLength = 30
        self.grid = [[0 for x in range(self.rows)] for y in range(self.columns)] 
        self.startingCell: tuple = (random.randint(0,self.columns-1), random.randint(0,self.rows-1))
        self.initGrid()

    def drawMaze(self):
        self.screen.fill(BLACK)
        for y in range(self.columns):
            for x in range(self.rows):
                print(f"{y} {x}")
                if self.grid[y][x] == 1:
                    screen_x,screen_y = self.get_cords_to_draw(x, y)
                    pygame.draw.rect(self.screen, WHITE, pygame.Rect(screen_x, screen_y,self.boxLength, self.boxLength))
        pygame.display.flip()
        self.wasClosed()
        
    def draw(self, path):
        self.screen.fill(BLACK)

        for cells in path:
            x,y = self.get_cords_to_draw(cells[0], cells[1])
            pygame.draw.rect(self.screen, WHITE, pygame.Rect(x, y,self.boxLength, self.boxLength))
        
        x,y = self.get_cords_to_draw(self.startingCell[0], self.startingCell[1])
        pygame.draw.rect(self.screen, (0,155,200), pygame.Rect(x, y,self.boxLength, self.boxLength))

        x,y = self.get_cords_to_draw(path[0][0], path[0][1])
        pygame.draw.rect(self.screen, (0,155,0), pygame.Rect(x, y,self.boxLength, self.boxLength))

        pygame.display.flip()
        self.wasClosed()
    
    def get_cords_to_draw(self,x,y):
        return x*40+5, y*40+5
    
    def loop_erased_random_walk(self):
        randomCell = (random.randint(0,self.columns-1), random.randint(0, self.rows-1))
        path = [randomCell]
        done = False

        while not done:
            options = self.getValidChoices(path[-1])
            nextCell = random.choice(options)
            x,y = nextCell
            #if that pos in grid is 0, never vistited; 1 = visited
            if self.grid[y][x] == 1:
                self.startingCell = (x,y)
                done = True
            elif nextCell not in path:
                path.append(nextCell)
            elif nextCell in path:
                path.clear()
                path.append(randomCell)
        
        self.updateGrid(path)
        return path

    def wasClosed(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("QUITTING")
                pygame.quit()
                sys.exit()
    
    def initGrid(self):
        self.grid[self.startingCell[1]][self.startingCell[0]] = 1
    
    def updateGrid(self, path):
        for cell in path:
             x, y = cell
             self.grid[y][x] = 1
    
    def getValidChoices(self, cell: tuple):
        x, y = cell
        choices = []
        # Ensure boundary checks before accessing the grid
        if x < 19 and self.grid[y][x + 1] <= 1:  # Check right
            choices.append((x + 1, y))
        if x > 0 and self.grid[y][x - 1] <= 1:  # Check left
            choices.append((x - 1, y))
        if y < 19 and self.grid[y + 1][x] <= 1:  # Check down
            choices.append((x, y + 1))
        if y > 0 and self.grid[y - 1][x] <= 1:  # Check up
            choices.append((x, y - 1))
        return choices
