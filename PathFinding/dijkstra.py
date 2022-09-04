
from PathFinding.window import Window
import pygame
from pygame.locals import *
from queue import Queue


class Dijkstra(Window):

    def __init__(self):
        super().__init__()
        self.frontier = Queue()
        self.reached = set()

    def flood(self):
        if self.start_flag == None or self.end_flag == None:
            return

        self.frontier.put(self.start_flag)
        self.reached.add(self.start_flag)
        
        while not self.frontier.empty():
            x, y = self.frontier.get()
            self.nodes[x][y] = 1
            for n in self.get_neighbours((x, y)):
                if n not in self.reached:
                    self.frontier.put(n)
                    self.reached.add(n)

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
                        self.nodes = np.zeros((self.rows, self.cols))
                        self.start_flag = None
                        self.end_flag = None

                    if event.key == K_s:
                        self.flood()

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
