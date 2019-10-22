# 贪吃蛇游戏

import pygame
import sys

pygame.init()
pygame.display.set_caption('Good Me')
pygame.display.set_mode((500, 500))

white = (255, 255, 255)

pygame.draw.rect(caption, white, pygame.Rect(250, 250, 10, 10))
pygame.draw.rect(caption, white, pygame.Rect(240, 250, 10, 10))
pygame.draw.rect(caption, white, pygame.Rect(230, 250, 10, 10))
pygame.draw.rect(caption, white, pygame.Rect(220, 250, 10, 10))
pygame.display.update()
