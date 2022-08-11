import pygame
import time
pygame.init()
board = [1500, 780]
pos = [0, 0]
pos2 = [board[0], 0]
velocity = [1, 0.5]
velocity2 = [1, 0.5]
back = pygame.display.set_mode((board[0], board[1]))
pygame.display.set_caption("Abhay Gaming")
backColor = 'black'
exit_loop = False
while not exit_loop:
    back.fill(backColor)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_loop = True
    pygame.draw.circle(back, 'green', (pos[0], pos[1]), 50)
    pygame.draw.circle(back, 'blue', (pos2[0], pos2[1]), 50)
    for i in (0, 1):
        if pos[0] < 0 or pos[0] > board[0]:
            velocity[0] *= -1
        if pos[1] < 0 or pos[1] > board[1]:
            velocity[1] *= -1
        if pos2[0] < 0 or pos2[0] > board[0]:
            velocity2[0] *= -1
        if pos2[1] < 0 or pos2[1] > board[1]:
            velocity2[1] *= -1
        if pos[0] == pos2[0] and pos[1] == pos2[1]:
            velocity[0] *= -1.1
            velocity2[0] *= -1.1
            velocity[1] *= -1.1
            velocity2[1] *= -1.1
        pos2[0] += velocity2[0]
        pos2[1] += velocity2[1]
        pos[0] += velocity[0]
        pos[1] += velocity[1]
    pygame.display.flip()
