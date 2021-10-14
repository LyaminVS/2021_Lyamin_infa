import pygame
from random import randint

pygame.init()

FPS = 30
screen = pygame.display.set_mode((1200, 800))

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
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]


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
        color = WHITE
        v_x = 40
        v_y = 40
    pygame.draw.circle(screen, color, (x, y), r)
    all_balls.append({
        "x": x,
        "y": y,
        "r": r,
        "v_x": v_x,
        "v_y": v_y,
        "color": color,
        "special": special
    })


def ball_update(one_ball):
    """
    рисует новое положение шарика

    :param one_ball: словарь шарика
    :return:
    """

    one_ball["x"] += one_ball["v_x"]
    one_ball["y"] += one_ball["v_y"]
    pygame.draw.circle(screen, one_ball["color"], (one_ball["x"], one_ball["y"]), one_ball["r"])

    if not (one_ball["special"]):

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
        if one_ball["x"] < one_ball["r"] or one_ball["x"] > 1200 - one_ball["r"]:
            one_ball["v_x"] = -one_ball["v_x"]
        if one_ball["y"] < one_ball["r"] or one_ball["y"] > 800 - one_ball["r"]:
            one_ball["v_y"] = -one_ball["v_y"]


def score_up(one_ball, user_score):
    """
    увеличивает счет игрока

    :param one_ball: шарик, на который нажал игрок
    :param user_score: счет игрока
    :return:
    """
    if one_ball["special"]:
        user_score += 5
    else:
        user_score += 1
    return user_score


def store_update(user_score):
    """
    отрисовывает на экране счетчик очков

    :param user_score: количество очков в данный момент времени
    :return:
    """
    font = pygame.font.Font(None, 36)
    text = font.render(user_score, True, (180, 0, 0))
    screen.blit(text, (50, 50))


pygame.display.update()
clock = pygame.time.Clock()
finished = False
for i in range(4):
    new_ball(balls)

while not finished:

    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for ball in balls:
                if (event.pos[0] - ball["x"]) ** 2 + (event.pos[1] - ball["y"]) ** 2 <= ball["r"] ** 2:
                    score = score_up(ball, score)
                    balls.remove(ball)
                    new_ball(balls)
    store_update(str(score))
    for ball in balls:
        ball_update(ball)

    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()
