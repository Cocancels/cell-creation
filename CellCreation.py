import pygame
import numpy 

# On initie les cellules à l'aide d'un tableau, qui représente les cases : chaque entrée qui est 1 correspond à une cellule au début du jeu.
def init(x, y):
    cells = numpy.zeros((y, x))
    screen = numpy.array([[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,1,0,0,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0],
                        [1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,1,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]);
    pos = (3,3)
    cells[pos[0]:pos[0]+screen.shape[0], pos[1]:pos[1]+screen.shape[1]] = screen
    return cells

# Fonction de lancement du jeu, qui permet d'initier l'écran avec les cellules de bases
def main(x, y, cellsize):
    pygame.init()
    surface = pygame.display.set_mode((x * cellsize, y * cellsize))
    pygame.display.set_caption("Cell life")

    cells = init(x, y)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        surface.fill((30, 30, 60))
        cells = update(surface, cells, cellsize)
        pygame.display.update()

# Fonction qui permet de checker si les cellules voisines sont vivantes ou morts, et d'effectuer les bonnes actions après ça.
def update(surface, current, sz):
    updt = numpy.zeros((current.shape[0], current.shape[1]))

    for r, c in numpy.ndindex(current.shape):
        num_alive = numpy.sum(current[r-1:r+2, c-1:c+2]) - current[r, c]

        if current[r, c] == 1 and num_alive < 2 or num_alive > 3:
            col = (200, 200, 225)
        elif (current[r, c] == 1 and 2 <= num_alive <= 3) or (current[r, c] == 0 and num_alive == 3):
            updt[r, c] = 1
            col = (255, 255, 215)

        col = col if current[r, c] == 1 else (10, 10, 40)
        pygame.draw.rect(surface, col, (c*sz, r*sz, sz-1, sz-1))

    return updt

# Changer les valeurs dans main permet de changer la taille de l'écran
if __name__ == "__main__":
    main(120, 90, 8)