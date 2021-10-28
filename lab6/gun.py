import math
import random as rnd

import pygame

FPS = 30

RED = 0xFF0000
BLUE = 0x0000FF
YELLOW = 0xFFC91F
GREEN = 0x00FF00
MAGENTA = 0xFF03B8
CYAN = 0x00FFCC
BLACK = (0, 0, 0)
WHITE = 0xFFFFFF
GREY = (125, 125, 125)
GAME_COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

WIDTH = 800
HEIGHT = 600

score = 0


class Ball:
    def __init__(self, screen: pygame.Surface, x=40, y=450):
        """ Конструктор класса ball

        Args:
        screen - экран для рисования
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.screen = screen
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.g = 1
        self.color = rnd.choice(GAME_COLORS)
        self.live = 30

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        self.x += self.vx
        self.y += self.vy
        self.vy += self.g

        if self.y + self.r > 600 - 40:
            if math.fabs(self.vy) < 5:
                self.y = 600 - 40
                self.vy = 0
            self.vy = -math.fabs(self.vy * 0.75)
            self.vx = 0.75 * self.vx

        if self.x + self.r > 800:
            self.vx = -math.fabs(self.vx)

        if self.x - self.r < 0:
            self.vx = math.fabs(self.vx)

        if self.vy == 0:
            self.live -= 1

    def draw(self):
        """
        метод отрисовывает мяч в данный момент времени

        :return:
        """
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r
        )

    def hit_test(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        if ((self.x - obj.x) ** 2 + (self.y - obj.y) ** 2) ** 0.5 < self.r + obj.r:
            return True
        return False


class Gun:
    def __init__(self, screen):
        """
        Конструктор класса Gun
        :param screen:
        """
        self.screen = screen
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.color = GREY
        self.length = 30

    def fire2_start(self):
        """
        начинает процесс выстрела, происходит при нажатии на мышь
        :return:
        """
        self.f2_on = 1

    def fire2_end(self, all_balls):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        :param all_balls: массим содержащий все мячи
        """
        new_ball = Ball(self.screen)
        new_ball.r += 5
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = -self.f2_power * math.sin(self.an)
        all_balls.append(new_ball)
        self.f2_on = 0
        self.f2_power = 10
        return all_balls

    def targeting(self, click):
        """
        Прицеливание. Зависит от положения мыши.
        :param click: объект содержащий информацию о нажатии на кнопку мыши
        """
        if click:
            self.an = -math.atan((click.pos[1] - 450) / (click.pos[0] - 20))
        if self.f2_on:
            self.color = RED
        else:
            self.color = GREY

    def draw(self):
        """
        рисует пушку в данный момент времени
        :return:
        """
        x1 = 40
        y1 = 450
        x2 = x1 + self.f2_power * math.cos(self.an)
        y2 = y1 - self.f2_power * math.sin(self.an)
        width = 5
        point1 = (x1 + width * math.sin(self.an), y1 + width * math.cos(self.an))
        point2 = (x1 - width * math.sin(self.an), y1 - width * math.cos(self.an))
        point3 = (x2 - width * math.sin(self.an), y2 - width * math.cos(self.an))
        point4 = (x2 + width * math.sin(self.an), y2 + width * math.cos(self.an))

        points = (point1, point2, point3, point4)

        pygame.draw.polygon(self.screen, self.color, points)

    def power_up(self):
        """
        увеличивает мощность выстрела
        :return:
        """
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            self.color = RED
        else:
            self.color = GREY


class Target:
    def __init__(self):
        """
        конструктор класса Target
        """
        self.points = 0
        self.live = 1
        self.x = rnd.randint(600, 780)
        self.y = rnd.randint(300, 550)
        self.r = rnd.randint(2, 50)
        self.vx = rnd.randint(-5, 5)
        self.vy = rnd.randint(-5, 5)
        self.color = RED

    def draw(self):
        """
        функция рисует цель в данный момент времени
        :return:
        """
        pygame.draw.circle(display, self.color, (self.x, self.y), self.r)

    def move(self):
        """
        функция изменяет координат self.x и self.y
        :return:
        """
        self.x += self.vx
        self.y += self.vy

        if self.x + self.r > 800:
            self.vx = -math.fabs(self.vx)

        if self.x - self.r < 0:
            self.vx = math.fabs(self.vx)

        if self.y + self.r > 600 - 40:
            self.vy = -math.fabs(self.vy)

        if self.y - self.r < 0:
            self.vy = math.fabs(self.vy)


class Player:
    def __init__(self):
        """
        конструктор класса Player
        """
        self.score = 0
        self.shots = 0
        self.reset_time = 0
        self.saved_shots = 0

    def score_up(self):
        """
        повышает счет игрока га 1
        :return:
        """
        self.score += 1
        return self.score

    def end_round(self):
        """
        запускает перезагрузку раунда
        :return:
        """
        self.reset_time = 150
        self.saved_shots = self.shots

    def shot_up(self):
        """
        увеличивает число сделанных высрелов на 1
        :return:
        """
        self.shots += 1

    def show_message(self, screen):
        """
        показывает сообщение об окончании раунда
        :param screen: экран для рисования
        :return:
        """
        if self.reset_time > 0:
            font1 = pygame.font.Font(None, 36)
            message = "Вы уничтожили цели за " + str(self.saved_shots) + " раза"
            text1 = font1.render(message, False, BLACK)
            screen.blit(text1, (230, 300))

    def update_time(self):
        """
        изменяет время перезапуска раунда
        :return:
        """
        if self.reset_time > 0:
            self.reset_time -= 1


pygame.init()
display = pygame.display.set_mode((WIDTH, HEIGHT))
balls = []
targets = []
player = Player()
clock = pygame.time.Clock()
gun = Gun(display)
for count in range(2):
    targets.append(Target())
finished = False

while not finished:
    display.fill(WHITE)
    gun.draw()
    round_finished = 1
    for target in targets:
        if target.live == 1:
            target.move()
            target.draw()
            round_finished = 0
    if player.reset_time == 0 and round_finished == 1:
        player.end_round()
        player.shots = 0
        for count in range(2):
            targets.append(Target())
    for b in balls:
        b.draw()

    font = pygame.font.Font(None, 36)
    text = font.render(str(score), False, BLACK)
    display.blit(text, (50, 50))
    player.show_message(display)
    player.update_time()
    pygame.display.update()

    clock.tick(FPS)
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            gun.fire2_start()
        elif event.type == pygame.MOUSEBUTTONUP:
            balls = gun.fire2_end(balls)
            player.shot_up()
        elif event.type == pygame.MOUSEMOTION:
            gun.targeting(event)

    for b in balls:
        b.move()
        for target in targets:
            if b.hit_test(target) and target.live and player.reset_time == 0:
                target.live = 0
                score = player.score_up()
        if b.live == 0:
            balls.remove(b)

    gun.power_up()

pygame.quit()
