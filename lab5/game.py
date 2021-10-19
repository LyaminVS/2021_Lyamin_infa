import pygame
from random import randint
import numpy as np

pygame.init()

FPS = 30
screen = pygame.display.set_mode((1200, 800))

game_over = True
time = 60
score = 0
balls = []
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (100, 100, 100)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]


def new_game(user_score):
    """
    начинает новую игру при нажатии на кнопку

    :param user_score: счет игрока в данный момент
    :return:
    """
    pygame.draw.polygon(screen, GREY, ((450, 350), (450, 450), (750, 450), (750, 350)))
    font_1 = pygame.font.Font(None, 36)
    text_1 = font_1.render("Начать игру", True, WHITE)
    screen.blit(text_1, (530, 385))
    font_2 = pygame.font.Font(None, 50)
    text_2 = font_2.render("Ваш счет:", True, WHITE)
    screen.blit(text_2, (510, 200))
    text_3 = font_2.render(str(int(user_score)), True, WHITE)
    screen.blit(text_3, (580, 270))


def new_ball(all_balls):
    """
    рисует новый шарик в рандомном месте и с рандомным радиусом
    :return:
    """
    x = randint(100, 700)
    y = randint(100, 500)
    r = randint(30, 50)
    v_x = randint(-10, 10)
    v_y = randint(-10, 10)
    color = COLORS[randint(0, 5)]
    special = False

    if randint(1, 101) in range(1, 21):
        special = True
        v_x = 10
        v_y = 10
        r = 80

    pygame.draw.circle(screen, color, (x, y), r)
    all_balls.append({
        "x": x,
        "y": y,
        "r": r,
        "v_x": v_x,
        "v_y": v_y,
        "color": color,
        "special": special,
    })


def new_color(color):
    """
    изменяет цвет специального шара

    :param color: цвет шара в данный момент
    :return:
    """
    changed_color = []
    for col in color:
        col += randint(-20, 20)
        if col > 255:
            col = 255
        if col < 0:
            col = 0
        changed_color.append(col)
    return tuple(changed_color)


def ball_update(one_ball):
    """
    рисует новое положение шарика

    :param one_ball: словарь шарика
    :return: нужно ли уничтожить шар
    """

    one_ball["x"] += one_ball["v_x"]
    one_ball["y"] += one_ball["v_y"]
    pygame.draw.circle(screen, one_ball["color"], (one_ball["x"], one_ball["y"]), one_ball["r"])

    if one_ball["x"] < one_ball["r"]:
        one_ball["v_x"] = randint(1, 10)
        one_ball["v_y"] = randint(-10, 10)
    if one_ball["y"] < one_ball["r"]:
        one_ball["v_x"] = randint(-10, 10)
        one_ball["v_y"] = randint(1, 10)
    if one_ball["x"] > 1200 - one_ball["r"]:
        one_ball["v_x"] = -randint(1, 10)
        one_ball["v_y"] = randint(-10, 10)
    if one_ball["y"] > 800 - one_ball["r"]:
        one_ball["v_x"] = randint(-10, 10)
        one_ball["v_y"] = -randint(1, 10)

    if one_ball["special"]:
        one_ball["color"] = new_color(one_ball["color"])

    if one_ball["r"] < 7:
        return True
    return False


def special_div(one_ball, all_balls):
    """
     разделяет специальный шар при нажатии на него

    :param one_ball: шар, на который нажали
    :param all_balls: массив со всеми шарами
    :return:
    """
    all_balls.append({
        "x": one_ball["x"],
        "y": one_ball["y"],
        "r": one_ball["r"] / 2,
        "v_x": one_ball["v_x"],
        "v_y": one_ball["v_y"],
        "color": one_ball["color"],
        "special": bool(randint(0, 5))
    })
    all_balls.append({
        "x": one_ball["x"],
        "y": one_ball["y"],
        "r": one_ball["r"] / 2,
        "v_x": -one_ball["v_x"],
        "v_y": -one_ball["v_y"],
        "color": one_ball["color"],
        "special": bool(randint(0, 5))
    })


def score_up(one_ball, user_score, all_balls):
    """
    увеличивает счет игрока

    :param all_balls:
    :param one_ball: шарик, на который нажал игрок
    :param user_score: счет игрока
    :return: новый счет, новый массив в шарами
    """
    if one_ball["special"]:
        special_div(one_ball, all_balls)
        user_score += (np.log2(80 / one_ball["r"]))
    else:
        user_score += 1
    return user_score, all_balls


def store_update(user_score):
    """
    отрисовывает на экране счетчик очков

    :param user_score: количество очков в данный момент времени
    :return:
    """
    font = pygame.font.Font(None, 36)
    text = font.render(user_score, True, (180, 0, 0))
    screen.blit(text, (50, 50))


def time_update(user_time):
    """
    обновляет время, выводимое на экран

    :param user_time: оставшееся время игры
    :return: закончилась ли игра
    """
    font = pygame.font.Font(None, 36)
    text = font.render(user_time, True, (180, 0, 0))
    screen.blit(text, (1050, 50))
    if int(user_time) <= 0:
        return True
    return False


pygame.display.update()
clock = pygame.time.Clock()
finished = False
for i in range(4):
    new_ball(balls)

while not finished:
    if game_over:
        new_game(score)
    if not game_over:
        time -= (1 / FPS)
        game_over = time_update(str(round(time)))
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            for ball in balls:
                if (event.pos[0] - ball["x"]) ** 2 + (event.pos[1] - ball["y"]) ** 2 <= ball["r"] ** 2:
                    score, balls = score_up(ball, score, balls)
                    balls.remove(ball)
        elif event.type == pygame.MOUSEBUTTONDOWN and 750 > event.pos[0] > 450 > event.pos[1] > 350:
            balls = []
            for i in range(4):
                new_ball(balls)
            game_over = False
            score = 0
    store_update(str(int(score)))

    for ball in balls:
        if ball_update(ball):
            balls.remove(ball)

    if len(balls) < 4:
        new_ball(balls)

    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()
