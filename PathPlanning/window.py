
import pygame
from pygame.locals import *
import numpy as np

	
class Window:
    def __init__(self, width, height, algo):
        self.width = width
        self.height = height
        self.win = pygame.display.set_mode((self.width, self.height))
        self.algo = algo
        self.node_size = 20
        self.rows = self.width // self.node_size
        self.cols = self.height // self.node_size
        self.nodes = np.zeros((self.rows, self.cols))
        # start node value
        self.start_flag = None
        # end node value
        self.end_flag = None

    def show(self):
        s = self.node_size
        for i in range(self.nodes.shape[0]):
            for j in range(self.nodes.shape[1]):
                node = pygame.Rect(i * s, j * s, s - 1, s - 1)
                if self.nodes[i][j] == 0:
                    pygame.draw.rect(self.win, (32,	37, 40), node, border_radius=4)
                if self.nodes[i][j] == 1:
                    pygame.draw.rect(self.win, (104, 127, 145), node, border_radius=4)

        # draw the start and end node
        if self.start_flag is not None:
            s_x, s_y = self.start_flag
            pygame.draw.rect(self.win, (227, 227, 225), pygame.Rect(s_x * s, s_y * s, s - 1, s - 1), 
                    border_radius=4) 

        # draw the start and end node
        if self.end_flag is not None:
            e_x, e_y = self.end_flag
            pygame.draw.rect(self.win, (164, 147, 146), pygame.Rect(e_x * s, e_y * s, s - 1, s - 1), 
                    border_radius=4) 

    def get_grid_pos(self):
        # get mouse pos
        x, y = pygame.mouse.get_pos()
        # get position by grid
        x //= self.node_size
        y //= self.node_size

        return x, y

    def run(self):
        running = True
        drawing = False
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.MOUSEMOTION:
                    if drawing:
                        x, y = self.get_grid_pos()
                        self.nodes[x][y] = 1

                if event.type == pygame.KEYDOWN:
                    if event.key == K_RETURN:
                        print(self.start_flag, self.end_flag)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.start_flag == None:
                        x, y = self.get_grid_pos()
                        self.start_flag = x, y
                        continue

                    if self.end_flag == None and self.start_flag != None:
                        x, y = self.get_grid_pos()
                        self.end_flag = x, y
                        continue

                    drawing = True

                if event.type == pygame.MOUSEBUTTONUP:
                    drawing = False
            
            self.show()

            pygame.display.update()
        pygame.quit()
