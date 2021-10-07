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


def gray(a):
    """
    :param a: отвечает за тон серого цвета (0 - чёрный, 255 - белый)
    :return: серый цвет в RGB

    возвращает серый цвет
    """
    return a, a, a


def half_circle_for_igloo(x, y, size):
    """
    :param x: x координата центра полукруга
    :param y: y координата центра полукруга
    :param size: радиус полукруга
    :return: none

    чертит полуокружность для иглу
    """
    igloo_color = (180, 180, 180), (0, 0, 0)    # цвет иглу [0] - основной, [1] - цвет границ (чёрный)
    target_rect = pygame.Rect(x - size, y - size, 2 * size, size)
    shape = pygame.Surface(target_rect.size, pygame.SRCALPHA)
    pygame.draw.circle(shape, igloo_color[0], (size, size), 1 * size)
    pygame.draw.circle(shape, igloo_color[1], (size, size), 1 * size, 1)
    screen.blit(shape, shape.get_rect(center=target_rect.center))


def horizontal_lines_for_igloo(x, y, size):
    """
    :param x: x координата центра полукруга
    :param y: y координата центра полукруга
    :param size: полукруга
    :return: none

    чертит горизонтальные отрезки для иглу
    """
    x_1, y_1 = 0.94, 0.33  # x_1 ** 2 + y_1 ** 2 = 1, координаты конца отрезка относительно середины полуокружности
    x_2, y_2 = 0.73, 0.67  # x_2 ** 2 + y_2 ** 2 = 1, координаты конца отрезка относительно середины полуокружности
    color = (0, 0, 0)  # цвет линий (чёрный)
    pygame.draw.line(screen, color, (x - 1 * size, y - 0 * size), (x + 1 * size, y - 0 * size))
    pygame.draw.line(screen, color, (x - x_1 * size, y - y_1 * size), (x + x_1 * size, y - y_1 * size))
    pygame.draw.line(screen, color, (x - x_2 * size, y - y_2 * size), (x + x_2 * size, y - y_2 * size))


def vertical_lines_for_igloo(x, y, size):
    """
    :param x: x координата центра полукруга
    :param y: y координата центра полукруга
    :param size: радиус полукруга
    :return: none

    чертит вертикальные отрезки для иглу
    """
    l_1, l_2, l_3 = 0.46, 0.47, 0.4   # расстояния между вертикальными линиями сверху, посередине и снизу соответственно
    h_3 = 0.97   # верхние отрезки должны упиратся в дугу окружности, от сюда и эта величина (0.97 ** 2 + 0.23 ** 2 = 1)
    h_0, h_1, h_2 = 0, 0.33, 0.67   # высота горизонтальных линий
    color = (0, 0, 0)   # цвет линий (чёрный)
    # верхние отрезки
    pygame.draw.line(screen, color, (x - l_1 * 0.5 * size, y - h_3 * size), (x - l_1 * 0.5 * size, y - h_2 * size))
    pygame.draw.line(screen, color, (x + l_1 * 0.5 * size, y - h_3 * size), (x + l_1 * 0.5 * size, y - h_2 * size))
    # средние отрезки
    pygame.draw.line(screen, color, (x - l_2 * size, y - h_2 * size), (x - l_2 * size, y - h_1 * size))
    pygame.draw.line(screen, color, (x - 0 * size, y - h_2 * size), (x - 0 * size, y - h_1 * size))
    pygame.draw.line(screen, color, (x + l_2 * size, y - h_2 * size), (x + l_2 * size, y - h_1 * size))
    # нижние отрезки
    pygame.draw.line(screen, color, (x - l_3 * 1.5 * size, y - h_1 * size), (x - l_3 * 1.5 * size, y - h_0 * size))
    pygame.draw.line(screen, color, (x - l_3 * 0.5 * size, y - h_1 * size), (x - l_3 * 0.5 * size, y - h_0 * size))
    pygame.draw.line(screen, color, (x + l_3 * 0.5 * size, y - h_1 * size), (x + l_3 * 0.5 * size, y - h_0 * size))
    pygame.draw.line(screen, color, (x + l_3 * 1.5 * size, y - h_1 * size), (x + l_3 * 1.5 * size, y - h_0 * size))


def igloo(x, y, size):
    """
    :param x: x координата центра полукруга
    :param y: y координата центра полукруга
    :param size: радиус полукруга
    :return: none

    чертит иглу в форме полукруга
    """
    half_circle_for_igloo(x, y, size)
    horizontal_lines_for_igloo(x, y, size)
    vertical_lines_for_igloo(x, y, size)


def fish(x, y):
    """
    :param x: координата x верхнего левого угла рыбы
    :param y: координата y верхнего левого угла рыбы
    :return: none

    чертит рыбу по координатам её верхнего левого угла
    """
    fish_color = (153, 171, 167), (197, 102, 99)  # основной цвет рыбы и цвет плавника соответственно
    pygame.draw.polygon(screen, fish_color[1], ((x + 10, y + 5), (x, y + 15), (x + 10, y + 25)))
    pygame.draw.polygon(screen, fish_color[0], ((x, y + 10), (x, y), (x + 10, y), (x + 30, y + 30)))
    pygame.draw.polygon(screen, fish_color[0], ((x + 30, y + 30), (x + 30, y + 40), (x + 40, y + 30)))
    pygame.draw.circle(screen, (0, 0, 255), (x + 5, y + 5), 3)
    pygame.draw.circle(screen, fish_color[0], (x + 5, y + 5), 1)


def man(x, y, size, direction):
    """
    :param x: координата x середины тела
    :param y: координата y середины тела
    :param size: высота основной фигуры тела
    :param direction: рука, в которой будет копьё ("left" / "right")
    :return: none

    чертит человека, по координатам середины и высоте основной фигуры тела, чертит копьё в указанной руке
    """
    man_color_clothes = (142, 125, 113), (107, 94, 84), (160, 150, 140)
    # цвет одежды [0] - основной, [1] - дополнительный, [2] - внутри капюшона
    head_1_rect = pygame.Rect(x - 0.4 * size, y - 0.75 * size, 0.8 * size, 0.5 * size)

    pygame.draw.ellipse(screen, gray(220), head_1_rect)

    body_rect = pygame.Rect(x - 0.5 * size, y - 0.5 * size, 1 * size, 1 * size)
    shape = pygame.Surface(body_rect.size, pygame.SRCALPHA)
    pygame.draw.ellipse(shape, man_color_clothes[0], (0, 0, body_rect[2], body_rect[3] * 2))
    screen.blit(shape, shape.get_rect(center=body_rect.center))

    leg_1_rect = pygame.Rect(x - 0.4 * size, y + 0.3 * size, 0.3 * size, 0.4 * size)
    pygame.draw.ellipse(screen, man_color_clothes[0], leg_1_rect)

    leg_2_rect = pygame.Rect(x + 0.1 * size, y + 0.3 * size, 0.3 * size, 0.4 * size)
    pygame.draw.ellipse(screen, man_color_clothes[0], leg_2_rect)

    leg_3_rect = pygame.Rect(x - 0.5 * size, y + 0.6 * size, 0.3 * size, 0.15 * size)
    pygame.draw.ellipse(screen, man_color_clothes[0], leg_3_rect)

    leg_4_rect = pygame.Rect(x + 0.2 * size, y + 0.6 * size, 0.3 * size, 0.15 * size)
    pygame.draw.ellipse(screen, man_color_clothes[0], leg_4_rect)

    pygame.draw.rect(screen, man_color_clothes[1], pygame.Rect(x - 0.5 * size, y + 0.35 * size, 1 * size, 0.15 * size))
    pygame.draw.rect(screen, man_color_clothes[1], pygame.Rect(x - 0.1 * size, y - 0.35 * size, 0.2 * size, 0.7 * size))

    head_2_rect = pygame.Rect(x - 0.3 * size, y - 0.68 * size, 0.6 * size, 0.35 * size)
    pygame.draw.ellipse(screen, man_color_clothes[2], head_2_rect)

    head_3_rect = pygame.Rect(x - 0.2 * size, y - 0.6 * size, 0.4 * size, 0.25 * size)
    pygame.draw.ellipse(screen, gray(220), head_3_rect)

    hand_1_rect = pygame.Rect(x - 0.75 * size, y - 0.25 * size, 0.6 * size, 0.25 * size)
    pygame.draw.ellipse(screen, man_color_clothes[0], hand_1_rect)

    hand_1_rect = pygame.Rect(x + 0.15 * size, y - 0.25 * size, 0.6 * size, 0.25 * size)
    pygame.draw.ellipse(screen, man_color_clothes[0], hand_1_rect)

    pygame.draw.line(screen, gray(0), (x + (1 - 2 * (direction == "left")) * 0.7 * size, y - 0.65 * size),
                     (x + (1 - 2 * (direction == "left")) * 0.7 * size, y + 0.65 * size))

    pygame.draw.line(screen, gray(0), (x - 0.15 * size, y - 0.55 * size), (x - 0.05 * size, y - 0.5 * size))

    pygame.draw.line(screen, gray(0), (x + 0.15 * size, y - 0.55 * size), (x + 0.05 * size, y - 0.5 * size))

    smile_1_rect = pygame.Rect(x - 0.5 * size, y - 0.45 * size, 1 * size, 1 * size)
    pygame.draw.arc(screen, gray(0), smile_1_rect, np.pi * 5 / 12, np.pi * 7 / 12)


def cat(x, y):
    body_1_rect = pygame.Rect(x + 15, y - 50, 100, 30)
    pygame.draw.ellipse(screen, gray(140), body_1_rect)

    draw_ellipse_angle(screen, gray(140), (x + 100, y - 70, 13, 80), 70)
    draw_ellipse_angle(screen, gray(140), (x + 90, y - 60, 13, 80), 60)

    draw_ellipse_angle(screen, gray(140), (x + 10, y - 70, 13, 80), -70)
    draw_ellipse_angle(screen, gray(140), (x + 20, y - 60, 13, 80), -60)

    fish(x - 10, y - 65)

    pygame.draw.polygon(screen, gray(255), ((x + 10, y - 60), (x + 10, y - 41), (x + 15, y - 71)))
    pygame.draw.polygon(screen, gray(255), ((x + 20, y - 60), (x + 20, y - 35), (x + 25, y - 71)))

    draw_ellipse_angle(screen, gray(140), (x + 5, y - 70, 35, 30), 0)

    draw_ellipse_angle(screen, gray(140), (x + 120, y - 90, 13, 80), -60)

    pygame.draw.circle(screen, gray(255), (x + 15, y - 59), 4)
    pygame.draw.circle(screen, gray(255), (x + 30, y - 57), 4)

    pygame.draw.circle(screen, gray(0), (x + 17, y - 59), 2)
    pygame.draw.circle(screen, gray(0), (x + 32, y - 57), 2)

    pygame.draw.polygon(screen, gray(140), ((x + 30, y - 71), (x + 40, y - 75), (x + 35, y - 60)))
    pygame.draw.polygon(screen, gray(140), ((x + 10, y - 60), (x + 10, y - 75), (x + 15, y - 71)))

    pygame.draw.circle(screen, gray(0), (x + 18, y - 47), 2)


pygame.init()

FPS = 30
screen = pygame.display.set_mode((600, 800))
screen.fill(gray(255))

pygame.draw.polygon(screen, gray(192), ([0, 0], [600, 0], [600, 400], [0, 400]))

igloo(200, 500, 150)

igloo(180, 550, 120)

igloo(260, 600, 120)

man(550, 417.5, 50, 'right')

man(400, 387.5, 50, 'left')

man(450, 415, 100, 'right')

man(500, 475, 100, 'right')

man(500, 662.5, 150, 'right')

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
