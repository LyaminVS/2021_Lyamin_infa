import pygame

pygame.init()

FPS = 30
screen = pygame.display.set_mode((600, 600))
screen.fill("white")

pygame.draw.circle(screen, "yellow", (300, 300), 150)
pygame.draw.circle(screen, "black", (300, 300), 150, 1)

pygame.draw.circle(screen, "red", (235, 255), 30)
pygame.draw.circle(screen, "black", (235, 255), 15)

pygame.draw.circle(screen, "red", (365, 255), 20)
pygame.draw.circle(screen, "black", (365, 255), 10)

pygame.draw.polygon(screen, "black", ([235, 360], [365, 360], [365, 385], [235, 385]))

pygame.draw.polygon(screen, "black", ([285, 240], [275, 250], [150, 145], [160, 135]))
pygame.draw.polygon(screen, "black", ([320, 230], [325, 245], [475, 215], [470, 200]))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
