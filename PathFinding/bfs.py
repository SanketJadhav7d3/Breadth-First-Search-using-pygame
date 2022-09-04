
from PathFinding.window import Window
import pygame
from pygame.locals import *
from queue import Queue
import time 
import numpy as np


class BFS(Window):

    def __init__(self):
        super().__init__()
        self.frontier = Queue()
        self.came_from = dict()
        self.clock = pygame.time.Clock()

    def flood(self):
        if self.start_flag == None or self.end_flag == None:
            print("Start flag not initialized")
            return

        self.frontier.put(self.start_flag)
        self.came_from[self.start_flag] = None
        
        while not self.frontier.empty():
            current = self.frontier.get()

            x, y = current
            if self.nodes[x][y] == 1:
                continue
    
            for n in self.get_neighbours(current):
                if n not in self.came_from:
                    self.frontier.put(n)
                    self.came_from[n] = current

        current = self.end_flag
        path = []

        while current != self.start_flag:
            path.append(current)
            current = self.came_from[current]
            
        path.append(self.start_flag)
        for p in path:
            x, y = p
            self.nodes[x][y] = 2

    def show(self):
        '''
            Displays all the nodes
        '''
        s = self.node_size
        for i in range(self.nodes.shape[0]):
            for j in range(self.nodes.shape[1]):
                node = pygame.Rect(i * s, j * s, s - 1, s - 1)
                if self.nodes[i][j] == 0:
                    self.draw_node(i, j, (32, 37, 40))
                if self.nodes[i][j] == 1:
                    self.draw_node(i, j, (104, 127, 145))
                if self.nodes[i][j] == 2:
                    self.draw_node(i, j, (229, 229, 227))

        # draw the start and end node
        if self.start_flag is not None:
            s_x, s_y = self.start_flag
            self.draw_node(s_x, s_y, (0, 255, 255))

        # draw the start and end node
        if self.end_flag is not None:
            e_x, e_y = self.end_flag
            self.draw_node(e_x, e_y, (164, 147, 146))

        # render help messages
        self.render_messages()

    # override run method
    def run(self):
        drawing = False
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

                if event.type == pygame.MOUSEMOTION:

                    if drawing:
                        x, y = self.get_grid_pos()
                        self.nodes[x][y] = 1

                if event.type == pygame.KEYDOWN:

                    if event.key == K_RETURN:
                        print(self.start_flag, self.end_flag)

                    if event.key == K_c:
                        # clear the screen
                        self.nodes = np.zeros((self.rows, self.cols))
                        self.start_flag = None
                        self.end_flag = None
                        self.frontier = Queue()
                        self.came_from = dict()

                    if event.key == K_f:
                        self.flood()

                    if event.key == K_p:
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
