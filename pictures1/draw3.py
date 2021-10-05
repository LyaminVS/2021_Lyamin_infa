import numpy as np
import pygame


def draw_ellipse_angle(surface, color, rect, angle):
    """
    :param surface: плоскость, на которой будет начерчен повёрнутый овал (например screen).
    :param color: цвет овала в RGB.
    :param rect: прямоугольник, в который будет вписан овал,
                первые 2 числа - координаты левого верхнего угла до поворота,
                вторые 2 числа - стороны прямоугольника.
    :param angle: угол поворота по часовой стрелке в градусах, поворот производится относительно центра овала.
    :return: none.

    чертит повёрнутый овал.
    """
    target_rect = pygame.Rect(rect)
    shape_surf = pygame.Surface(target_rect.size, pygame.SRCALPHA)
    pygame.draw.ellipse(shape_surf, color, [0, 0, *target_rect.size])
    rotated_surf = pygame.transform.rotate(shape_surf, angle)
    surface.blit(rotated_surf, rotated_surf.get_rect(center=target_rect.center))


def igloo(x, y, size):
    pygame.draw.circle(screen, (180, 180, 180), (x, y), 1 * size)
    pygame.draw.circle(screen, (0, 0, 0), (x, y), 1 * size, 1)
    pygame.draw.rect(screen, (255, 255, 255), (x - 1.07 * size, y, 2.13 * size, 1.07 * size))

    pygame.draw.line(screen, (0, 0, 0), (x - 1 * size, y), (x + 1 * size, y))
    pygame.draw.line(screen, (0, 0, 0), (x - 0.93 * size, y - 0.33 * size), (x + 0.93 * size, y - 0.33 * size))
    pygame.draw.line(screen, (0, 0, 0), (x - 0.73 * size, y - 0.67 * size), (x + 0.73 * size, y - 0.67 * size))

    pygame.draw.line(screen, (0, 0, 0), (x - 0.47 * size, y - 0.67 * size), (x - 0.47 * size, y - 0.33 * size))
    pygame.draw.line(screen, (0, 0, 0), (x - 0 * size, y - 0.66 * size), (x - 0 * size, y - 0.33 * size))
    pygame.draw.line(screen, (0, 0, 0), (x + 0.47 * size, y - 0.67 * size), (x + 0.47 * size, y - 0.33 * size))

    pygame.draw.line(screen, (0, 0, 0), (x - 0.6 * size, y - 0.33 * size), (x - 0.6 * size, y - 0 * size))
    pygame.draw.line(screen, (0, 0, 0), (x - 0.2 * size, y - 0.33 * size), (x - 0.2 * size, y - 0 * size))
    pygame.draw.line(screen, (0, 0, 0), (x + 0.2 * size, y - 0.33 * size), (x + 0.2 * size, y - 0 * size))
    pygame.draw.line(screen, (0, 0, 0), (x + 0.6 * size, y - 0.33 * size), (x + 0.6 * size, y - 0 * size))

    pygame.draw.line(screen, (0, 0, 0), (x - 0.23 * size, y - 0.97 * size), (x - 0.23 * size, y - 0.67 * size))
    pygame.draw.line(screen, (0, 0, 0), (x + 0.23 * size, y - 0.97 * size), (x + 0.23 * size, y - 0.67 * size))


def fish(x, y):
    pygame.draw.polygon(screen, (197, 102, 99), ((x, y - 60), (x - 10, y - 50), (x, y - 40)))
    pygame.draw.polygon(screen, (153, 171, 167), ((x - 10, y - 55), (x - 10, y - 65), (x, y - 65), (x + 20, y - 35)))
    pygame.draw.polygon(screen, (153, 171, 167), ((x + 20, y - 35), (x + 20, y - 25), (x + 30, y - 35)))
    pygame.draw.circle(screen, "blue", (x - 5, y - 60), 3)
    pygame.draw.circle(screen, (153, 171, 167), (x - 5, y - 60), 1)


def man(x, y, size, direction):
    head_1_rect = pygame.Rect(x - 40 * size, y - 100 * size, 80 * size, 50 * size)
    pygame.draw.ellipse(screen, (220, 220, 220), head_1_rect)

    body_1_rect = pygame.Rect(x - 50 * size, y - 75 * size, 100 * size, 200 * size)
    pygame.draw.ellipse(screen, (142, 125, 113), body_1_rect)

    pygame.draw.rect(screen, "white", pygame.Rect(x - 50 * size, y + 10 * size, 100 * size, 120 * size))

    leg_1_rect = pygame.Rect(x - 40 * size, y + 5 * size, 30 * size, 40 * size)
    pygame.draw.ellipse(screen, (142, 125, 113), leg_1_rect)

    leg_2_rect = pygame.Rect(x + 10 * size, y + 5 * size, 30 * size, 40 * size)
    pygame.draw.ellipse(screen, (142, 125, 113), leg_2_rect)

    leg_3_rect = pygame.Rect(x - 50 * size, y + 35 * size, 30 * size, 15 * size)
    pygame.draw.ellipse(screen, (142, 125, 113), leg_3_rect)

    leg_4_rect = pygame.Rect(x + 20 * size, y + 35 * size, 30 * size, 15 * size)
    pygame.draw.ellipse(screen, (142, 125, 113), leg_4_rect)

    pygame.draw.rect(screen, (107, 94, 84), pygame.Rect(x - 50 * size, y + 10 * size, 100 * size, 15 * size))
    pygame.draw.rect(screen, (107, 94, 84), pygame.Rect(x - 10 * size, y - 60 * size, 20 * size, 70 * size))

    head_2_rect = pygame.Rect(x - 30 * size, y - 93 * size, 60 * size, 35 * size)
    pygame.draw.ellipse(screen, (160, 150, 140), head_2_rect)

    head_3_rect = pygame.Rect(x - 20 * size, y - 85 * size, 40 * size, 25 * size)
    pygame.draw.ellipse(screen, (220, 220, 220), head_3_rect)

    head_3_rect = pygame.Rect(x - 20 * size, y - 85 * size, 40 * size, 25 * size)
    pygame.draw.ellipse(screen, (220, 220, 220), head_3_rect)

    hand_1_rect = pygame.Rect(x - 75 * size, y - 50 * size, 60 * size, 25 * size)
    pygame.draw.ellipse(screen, (142, 125, 113), hand_1_rect)

    hand_1_rect = pygame.Rect(x + 15 * size, y - 50 * size, 60 * size, 25 * size)
    pygame.draw.ellipse(screen, (142, 125, 113), hand_1_rect)

    if direction == "left":
        pygame.draw.line(screen, "black", (x - 70 * size, y - 90 * size), (x - 70 * size, y + 40 * size))
    if direction == "right":
        pygame.draw.line(screen, "black", (x + 70 * size, y - 90 * size), (x + 70 * size, y + 40 * size))

    pygame.draw.line(screen, "black", (x - 15 * size, y - 80 * size), (x - 5 * size, y - 75 * size))

    pygame.draw.line(screen, "black", (x + 15 * size, y - 80 * size), (x + 5 * size, y - 75 * size))

    smile_1_rect = pygame.Rect(x - 50 * size, y - 70 * size, 100 * size, 100 * size)
    pygame.draw.arc(screen, "black", smile_1_rect, np.pi * 5 / 12, np.pi * 7 / 12)


def cat(x, y):
    body_1_rect = pygame.Rect(x + 15, y - 50, 100, 30)
    pygame.draw.ellipse(screen, (140, 140, 140), body_1_rect)

    draw_ellipse_angle(screen, (140, 140, 140), (x + 100, y - 70, 13, 80), 70)
    draw_ellipse_angle(screen, (140, 140, 140), (x + 90, y - 60, 13, 80), 60)

    draw_ellipse_angle(screen, (140, 140, 140), (x + 10, y - 70, 13, 80), -70)
    draw_ellipse_angle(screen, (140, 140, 140), (x + 20, y - 60, 13, 80), -60)

    fish(x, y)

    pygame.draw.polygon(screen, "white", ((x + 10, y - 60), (x + 10, y - 41), (x + 15, y - 71)))
    pygame.draw.polygon(screen, "white", ((x + 20, y - 60), (x + 20, y - 35), (x + 25, y - 71)))

    draw_ellipse_angle(screen, (140, 140, 140), (x + 5, y - 70, 35, 30), 0)

    draw_ellipse_angle(screen, (140, 140, 140), (x + 120, y - 90, 13, 80), -60)

    pygame.draw.circle(screen, "white", (x + 15, y - 59), 4)
    pygame.draw.circle(screen, "white", (x + 30, y - 57), 4)

    pygame.draw.circle(screen, "black", (x + 17, y - 59), 2)
    pygame.draw.circle(screen, "black", (x + 32, y - 57), 2)

    pygame.draw.polygon(screen, (140, 140, 140), ((x + 30, y - 71), (x + 40, y - 75), (x + 35, y - 60)))
    pygame.draw.polygon(screen, (140, 140, 140), ((x + 10, y - 60), (x + 10, y - 75), (x + 15, y - 71)))

    pygame.draw.circle(screen, "black", (x + 18, y - 47), 2)


pygame.init()

FPS = 30
screen = pygame.display.set_mode((600, 800))
screen.fill("white")

pygame.draw.polygon(screen, (192, 192, 192), ([0, 0], [600, 0], [600, 400], [0, 400]))

igloo(200, 500, 150)

igloo(180, 550, 120)

igloo(260, 600, 120)

man(550, 430, 0.5, 'right')

man(400, 400, 0.5, 'left')

man(450, 440, 1, 'right')

man(500, 500, 1, 'right')

man(500, 700, 1.5, 'right')

cat(200, 700)

cat(130, 750)

cat(250, 760)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
