
import pygame
from queue import Queue
from pygame.locals import *
import numpy as np

class BFS:

    def __init__(self):
        pygame.init()
        self.height = 800
        self.width = 800
        self.tile = 10
        self.graph = np.zeros((self.width // self.tile, self.height // self.tile))
        self.window = pygame.display.set_mode((self.width, self.height))
        self.start_node = None
        self.target_node = None
        self.visited = {}       # to keep track of visited elements
        self.queue = Queue()    # will keep adjacent elements 

    def draw_node(self, x, y, color):
        '''
            Draws node given mouse x and y coordinates
        '''
        s = self.tile
        node = pygame.Rect(x*s, y*s, s-1, s-1);
        pygame.draw.rect(self.window, color, node, border_radius=3)

    def get_grid_pos(self):
        x, y = pygame.mouse.get_pos()

        x //= self.tile
        y //= self.tile

        return x, y

    def draw_graph(self):

        for i in range(self.graph.shape[0]):
            for j in range(self.graph.shape[1]):
                if self.graph[i][j] == 1:
                    self.draw_node(i, j, (255, 0, 0))

                if self.graph[i][j] == 2:
                    self.draw_node(i, j, (255, 255, 0))

    def get_neighbours(self, node):
        
        neighbours = []
        x, y = node

        if x + 1 < self.graph.shape[0]: neighbours.append((x+1, y))
        if x - 1 >= 0: neighbours.append((x-1, y))

        if y + 1 < self.graph.shape[1]: neighbours.append((x, y+1))
        if y - 1 >= 0: neighbours.append((x, y-1))

        return neighbours

    def flood(self):
        self.queue.put(self.start_node)
        self.visited[self.start_node] = None
        
        while not self.queue.empty():
            current = self.queue.get()

            x, y = current

            if self.graph[x][y] == 1:
                continue

            for n in self.get_neighbours(current):

                if n not in self.visited:
                    self.queue.put(n)
                    self.visited[n] = current

        current = self.target_node
        path = []

        while current != self.start_node:
            path.append(current)
            current = self.visited[current]

        path.append(self.start_node)

        for p in path:
            x, y = p
            self.graph[x][y] = 2


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
                        self.graph[x][y] = 1

                if event.type == pygame.KEYDOWN:

                    if event.key == K_f:
                        self.flood()
                
                if event.type == pygame.MOUSEBUTTONDOWN:

                    if self.start_node == None:
                        self.start_node = self.get_grid_pos()
                        x, y = self.start_node
                        self.graph[x][y] = 2
                        continue

                    if self.target_node == None and self.start_node is not None:
                        self.target_node = self.get_grid_pos()
                        x, y = self.target_node
                        self.graph[x][y] = 2
                        continue

                    drawing = True

                if event.type == pygame.MOUSEBUTTONUP:
                    drawing = False

            for node in self.visited:
                self.draw_node(node[0], node[1], (0, 0, 255))

            self.draw_graph()
            pygame.display.update()

        pygame.quit()


if __name__ == "__main__":
    b = BFS()
    b.run()
