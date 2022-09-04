
from pygame.locals import *
import numpy as np
import pygame

	
class Window:
    '''
        Window to display a grid of nodes 
    '''
    pygame.font.init()
    def __init__(self):
        self.width = 1400
        self.height = 900
        self.font = pygame.font.Font("freesansbold.ttf", 18)
        self.win = pygame.display.set_mode((self.width + 250, self.height))
        self.node_size = 20
        self.rows = self.width // self.node_size
        self.cols = self.height // self.node_size
        self.nodes = np.zeros((self.rows, self.cols))
        # start node value
        self.start_flag = None
        # end node value
        self.end_flag = None

    def render_messages(self):
        '''
            Renders help messages
        '''
        clear_text = self.font.render("Press c to clear all nodes", True, (255, 255, 255))
        text_area = clear_text.get_rect()
        text_area.center = (self.width + 120, 20)
        self.win.blit(clear_text, text_area)

    def show(self):
        '''
            Displays all the nodes
        '''
        s = self.node_size
        for i in range(self.nodes.shape[0]):
            for j in range(self.nodes.shape[1]):
                node = pygame.Rect(i * s, j * s, s - 1, s - 1)
                if self.nodes[i][j] == 0:
                    self.draw_node(i, j, (207, 255, 220))
                if self.nodes[i][j] == 1:
                    self.draw_node(i, j, (104, 127, 145))

        # draw the start and end node
        if self.start_flag is not None:
            s_x, s_y = self.start_flag
            self.draw_node(s_x, s_y, (227, 225, 225))

        # draw the start and end node
        if self.end_flag is not None:
            e_x, e_y = self.end_flag
            self.draw_node(e_x, e_y, (164, 147, 146))

        # render help messages
        self.render_messages()

    def draw_node(self, x, y, color):
        '''
            Draws a node at specified x, y position in grid
        '''
        s = self.node_size
        node = pygame.Rect(x * s, y * s, s - 1, s - 1)
        pygame.draw.rect(self.win, color, node, border_radius=4)

    def get_grid_pos(self) -> tuple:
        # get mouse pos
        x, y = pygame.mouse.get_pos()
        # get position by grid
        x //= self.node_size
        y //= self.node_size

        return x, y

    def get_neighbours(self, node) -> list:
        '''
            Returns neigbouring node's coordinates as a list
        '''
        x, y = node[0], node[1]
        neighbours = []
        if x + 1 < self.nodes.shape[0]: neighbours.append((x+1, y))
        if x - 1 >= 0 : neighbours.append((x-1, y))
        if y + 1 < self.nodes.shape[1]: neighbours.append((x, y+1))
        if y -1 >= 0: neighbours.append((x, y-1))

        return neighbours

    def run(self) -> None:
        '''
            Main loop of the game
        '''
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

                    if event.key == K_p:
                        pass

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
