
import pygame
import numpy as np
	

class Window:
    def __init__(self, width, height, algo):
        pygame.init()
        self.width = width
        self.height = height
        self.win = pygame.display.set_mode((self.width, self.height))
        self.algo = algo
        self.node_size = 20
        self.rows = self.width // self.node_size
        self.cols = self.height // self.node_size
        self.nodes = np.zeros((self.rows, self.cols))
        print(self.nodes.shape)

    def show(self):
        s = self.node_size
        for i in range(self.nodes.shape[0]):
            for j in range(self.nodes.shape[1]):
                node = pygame.Rect(i * s, j * s, s - 1, s - 1)
                if self.nodes[i][j] == 0:
                    pygame.draw.rect(self.win, (32,	37, 40), node)

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            
            self.show()

            pygame.display.update()

        pygame.quit()
