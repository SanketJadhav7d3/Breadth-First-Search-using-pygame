
from PathPlanning.window import Window
import pygame
import sys

if __name__ == "__main__":

    pygame.init()

    win = Window(1400, 900, "dijkstra")

    win.run()
