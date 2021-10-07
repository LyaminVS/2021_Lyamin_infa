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


def legs(x, y, color, size):
    """
    :param x: координата x центральной точки ног
    :param y: координата y верхней точки ног
    :param color: цвет ног
    :param size: длина ног
    :return: none

    чертит ноги по координатам верхней (по y) центральной (по x) точки указанного цвета указанной длины
    """
    d_leg, d_foot = 0.8, 1.6     # расстояние между ногами, стопами
    wid_leg, wid_foot = 1.2, 0.6   # ширина ноги, стопы
    len_leg, len_foot = 0.8, 1.2  # длина ноги (без стопы), стопы

    left_leg_rect = pygame.Rect(x + (-d_leg * 0.5 - wid_leg) * size, y - len_leg * size,
                                wid_leg * size, len_leg * 2 * size)
    pygame.draw.ellipse(screen, color, left_leg_rect)

    right_leg_rect = pygame.Rect(x + (d_leg * 0.5) * size, y - len_leg * size,
                                 wid_leg * size, len_leg * 2 * size)
    pygame.draw.ellipse(screen, color, right_leg_rect)

    left_foot_rect = pygame.Rect(x - 2 * size, y + (1 - wid_foot) * size,
                                 len_foot * size, wid_foot * size)
    pygame.draw.ellipse(screen, color, left_foot_rect)

    right_foot_rect = pygame.Rect(x + (d_foot + len_foot - 2) * size, y + (1 - wid_foot) * size,
                                  len_foot * size, wid_foot * size)
    pygame.draw.ellipse(screen, color, right_foot_rect)


def face(x, y, size):
    """
    :param x: координата x центра лица
    :param y: координата y верхней точки лица
    :param size: численно равно расстоянию между глазами, задаёт размер всего лица
    :return: none

    чертит лицо человека по координатам верхней (по y) центральной (по x) точки и расстоянию между глазами
    """
    smile_y = 1     # координата y верхней точки рта
    eye_x, eye_y = 1, 0.5   # размеры глаза по x и y соответственно
    color = (0, 0, 0)   # цвет линий (чёрный)
    radius, angle = 5, np.pi / 6    # задают рот через радиус и угловую длину дуги окружности
    pygame.draw.line(screen, color, (x - (eye_x + 0.5) * size, y + 0 * size), (x - 0.5 * size, y + eye_y * size))

    pygame.draw.line(screen, color, (x + (eye_x + 0.5) * size, y + 0 * size), (x + 0.5 * size, y + eye_y * size))

    smile_rect = pygame.Rect(x - radius * size, y + smile_y * size, radius * 2 * size, radius * 2 * size)
    pygame.draw.arc(screen, color, smile_rect, (np.pi - angle) * 0.5, (np.pi + angle) * 0.5)


def hands(x, y, color, size):
    """
    :param color: цвет рук
    :param x: координата x центра рук
    :param y: координата y верхней точки рук
    :param size: численно равно расстоянию ширине рук, задаёт размер рук
    :return: none

    чертит руки человека указанного цвета по координатам верхней (по y) центральной (по x) точки и их ширине
    """
    hand_1_rect = pygame.Rect(x - 3 * size, y - 0 * size, 2.4 * size, 1 * size)
    pygame.draw.ellipse(screen, color, hand_1_rect)

    hand_1_rect = pygame.Rect(x + 0.6 * size, y - 0 * size, 2.4 * size, 1 * size)
    pygame.draw.ellipse(screen, color, hand_1_rect)


def head_and_body(x, y, size, color):
    """
    :param color: массив с цветом
        [0] - основной цвет
        [1] - дополнительный цвет
        [2] - цвет внутри капюшона
        [3] - цвет головы и меха на капюшоне
    :param x: координата x центра тела
    :param y: координата y центра тела
    :param size: численно равно расстоянию ширине тела, задаёт размер головы и тела
    :return: none

    чертит голову и тело человека указанного цвета по центральной точки тела и его ширине
    """
    # прямоугольники, в которые будут вписываться эллипсы для капюшона и головы
    head_1_rect = pygame.Rect(x - 0.4 * size, y - 0.75 * size, 0.8 * size, 0.5 * size)
    head_2_rect = pygame.Rect(x - 0.3 * size, y - 0.68 * size, 0.6 * size, 0.35 * size)
    head_3_rect = pygame.Rect(x - 0.2 * size, y - 0.6 * size, 0.4 * size, 0.25 * size)

    pygame.draw.ellipse(screen, color[3], head_1_rect)

    body_rect = pygame.Rect(x - 0.5 * size, y - 0.5 * size, 1 * size, 1 * size)
    shape = pygame.Surface(body_rect.size, pygame.SRCALPHA)
    pygame.draw.ellipse(shape, color[0], (0, 0, body_rect[2], body_rect[3] * 2))
    screen.blit(shape, shape.get_rect(center=body_rect.center))
    # горизонтальная и вертикальная тёмная линия на одежде соответственно
    pygame.draw.rect(screen, color[1], pygame.Rect(x - 0.5 * size, y + 0.35 * size, 1 * size, 0.15 * size))
    pygame.draw.rect(screen, color[1], pygame.Rect(x - 0.1 * size, y - 0.35 * size, 0.2 * size, 0.7 * size))

    pygame.draw.ellipse(screen, color[2], head_2_rect)

    pygame.draw.ellipse(screen, color[3], head_3_rect)


def man(x, y, size, direction):
    """
    :param x: координата x середины тела
    :param y: координата y середины тела
    :param size: высота основной фигуры тела
    :param direction: рука, в которой будет копьё ("left" / "right")
    :return: none

    чертит человека, по координатам середины и высоте основной фигуры тела, чертит копьё в указанной руке
    """
    # цвет [0] основной, [1] дополнительный, [2] внутри капюшона, [3] самого человека и меха на капюшоне, [4] копья
    man_color = (142, 125, 113), (107, 94, 84), (160, 150, 140), (220, 220, 220), (0, 0, 0)

    legs(x, y + 0.5 * size, man_color[0], size * 0.25)

    head_and_body(x, y, size, man_color)

    hands(x, y - 0.25 * size, man_color[0], size * 0.25)

    pygame.draw.line(screen, man_color[4], (x + (1 - 2 * (direction == "left")) * 0.7 * size, y - 0.65 * size),
                     (x + (1 - 2 * (direction == "left")) * 0.7 * size, y + 0.65 * size))

    face(x, y - 0.55 * size, size * 0.1)


def cat_paws(x, y_right, color):
    """
    :param x: координата x центра лап
    :param y_right: координата y центра правых (дальних) лап
    :param color: цвет лап
    :return: none

    чертит лапы по координатам центра правых (дальних) лап соответствующего цвета
    """
    wid_paw, len_paw = 13, 80   # ширина и длинна лап соответственно
    angle_left_paw, angle_right_paw = 60, 70    # угол поворота относительно вертикали правых и левых лап соответственно
    y_left = y_right + 10   # координата y центра левых (ближних) лап
    d_x_left, d_x_right = 150, 170    # расстояние между центрами левых и правых лап соответственно
    # задние лапы
    draw_ellipse_angle(screen, color, (x + (d_x_right - len_paw) * 0.5, y_right - wid_paw * 0.5, wid_paw, len_paw),
                       angle_right_paw)
    draw_ellipse_angle(screen, color, (x + (d_x_left - len_paw) * 0.5, y_left - wid_paw * 0.5, wid_paw, len_paw),
                       angle_left_paw)
    # передние лапы
    draw_ellipse_angle(screen, color, (x - (d_x_right - len_paw) * 0.5, y_right - wid_paw * 0.5, wid_paw, len_paw),
                       -angle_right_paw)
    draw_ellipse_angle(screen, color, (x - (d_x_left - len_paw) * 0.5, y_left - wid_paw * 0.5, wid_paw, len_paw),
                       -angle_left_paw)


def cat_eyes(x, y, color):
    """
    :param x: координата x точки между глаз
    :param y: координата y точки между глаз
    :param color: цвет глаз
        color[0] - белок
        color[1] - зрачёк
    :return: none

    чертит глаза по координате точки между ними соответствующего цвета
    """
    r_b, r_z = 4, 2     # радиус белка и зрачка соответственно
    d_x, d_y = 15, 2    # расстояние между центрами глаз по x и y соответственно
    pygame.draw.circle(screen, color[0], (x - d_x * 0.5, y - d_y * 0.5), r_b)
    pygame.draw.circle(screen, color[0], (x + d_x * 0.5, y + d_y * 0.5), r_b)

    pygame.draw.circle(screen, color[1], (x - d_x * 0.5 + r_b - r_z, y - d_y * 0.5), r_z)
    pygame.draw.circle(screen, color[1], (x + d_x * 0.5 + r_b - r_z, y + d_y * 0.5), r_z)


def cat(x, y):
    """
    :param x: координата x центра тела
    :param y: координата y центра тела
    :return: none

    чертит кота относительно центра его тела
    """
    # цвет [0] основной, [1] белки глаз и зубы (белый), [2] зрачки и нос (чёрный)
    cat_color = (140, 140, 140), (255, 255, 255), (0, 0, 0)
    body_1_rect = pygame.Rect(x - 50, y - 15, 100, 30)
    pygame.draw.ellipse(screen, cat_color[0], body_1_rect)

    cat_paws(x - 10, y - 28.5, cat_color[0])

    fish(x - 75, y - 30)

    pygame.draw.polygon(screen, cat_color[1], ((x - 55, y - 25), (x - 55, y - 6), (x - 50, y - 36)))
    pygame.draw.polygon(screen, cat_color[1], ((x - 45, y - 25), (x - 45, y - 0), (x - 40, y - 36)))

    draw_ellipse_angle(screen, cat_color[0], (x - 60, y - 35, 35, 30), 0)

    draw_ellipse_angle(screen, cat_color[0], (x + 55, y - 55, 13, 80), -60)

    cat_eyes(x - 42.5, y - 23, cat_color[1:3])

    pygame.draw.polygon(screen, cat_color[0], ((x - 35, y - 36), (x - 25, y - 40), (x - 30, y - 25)))
    pygame.draw.polygon(screen, cat_color[0], ((x - 55, y - 25), (x - 55, y - 40), (x - 50, y - 36)))

    pygame.draw.circle(screen, cat_color[2], (x - 47, y - 12), 2)


pygame.init()

FPS = 30
screen = pygame.display.set_mode((600, 800))
screen.fill((255, 255, 255))    # белая земля

pygame.draw.rect(screen, (192, 192, 192), (0, 0, 600, 400))     # светло серое небо

igloo(200, 500, 150)

igloo(180, 550, 120)

igloo(260, 600, 120)

man(550, 417.5, 50, 'right')

man(400, 387.5, 50, 'left')

man(450, 415, 100, 'right')

man(500, 475, 100, 'right')

man(500, 662.5, 150, 'right')

cat(265, 665)

cat(195, 715)

cat(315, 725)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
