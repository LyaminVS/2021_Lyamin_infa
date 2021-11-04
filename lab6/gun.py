import math
import random
import random as rnd

import numpy as np
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
    def __init__(self, screen: pygame.Surface, x, y):
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
        self.live = 100

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        self.x += self.vx
        self.y += self.vy
        if self.vy != 0:
            self.vy += self.g

        if self.y + self.r > 600 - 40:
            if math.fabs(self.vy) < 5:
                self.y = 600 - 60
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


class BombBall(Ball):
    def __init__(self, screen, x, y):
        """
        конструктор BombBall
        :param screen: экран, на котором рисуют
        :param x: координата центра x
        :param y: координата центра y
        """
        super().__init__(screen, x, y)
        self.explosion_time = 60
        self.live = 10

    def draw(self):
        """
        рисует мяч в данный момент
        :return:
        """
        if self.explosion_time != 0:
            pygame.draw.circle(
                self.screen,
                random.choice(GAME_COLORS),
                (self.x, self.y),
                self.r
            )
            self.explosion_time -= 1

        else:
            self.r += 10
            pygame.draw.circle(
                self.screen,
                random.choice(GAME_COLORS),
                (self.x, self.y),
                self.r
            )
            self.live -= 1

    def move(self):
        """
        изменяет координаты мяча
        :return:
        """
        if self.explosion_time == 0:
            pass
        else:
            super().move()


class TargetBall(Ball):
    def __init__(self, screen, x, y):
        super().__init__(screen, x, y)
        self.g = 1

    def hit_test(self, obj):
        return False


class Gun:
    def __init__(self, screen, x, y):
        """
        Конструктор класса Gun
        :param screen:
        """
        self.screen = screen
        self.f2_power = 20
        self.f2_on = 0
        self.an = 1
        self.color = GREY
        self.x1 = x
        self.y1 = y
        self.x2 = self.x1 + self.f2_power * math.cos(self.an)
        self.y2 = self.y1 - self.f2_power * math.sin(self.an)
        self.rad = 30
        self.center_x = self.x1 - self.rad * np.cos(self.an)
        self.center_y = self.y1 + self.rad * np.sin(self.an)

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

        if random.randint(1, 100) in range(1, 66):
            new_ball = Ball(self.screen, self.x2, self.y2)
        else:
            new_ball = BombBall(self.screen, self.x2, self.y2)
        new_ball.r += 5
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = -self.f2_power * math.sin(self.an)
        all_balls.append(new_ball)
        self.f2_on = 0
        self.f2_power = 30
        return all_balls

    def targeting(self, click):
        """
        Прицеливание. Зависит от положения мыши.
        :param click: объект содержащий информацию о нажатии на кнопку мыши
        """
        delta_y = click.pos[1] - self.y1
        delta_x = click.pos[0] - self.x1

        self.center_x = self.x1 - self.rad * np.cos(self.an)
        self.center_y = self.y1 + self.rad * np.sin(self.an)

        self.x2 = self.x1 + self.f2_power * math.cos(self.an)
        self.y2 = self.y1 - self.f2_power * math.sin(self.an)

        if click:
            if delta_x != 0:
                tan = delta_y / delta_x
                if delta_x > 0:
                    self.an = -math.atan(tan)
                else:
                    self.an = np.pi - math.atan(tan)
            else:
                if delta_y < 0:
                    self.an = np.pi / 2
                else:
                    self.an = 3 * np.pi / 2
        if self.f2_on:
            self.color = RED
        else:
            self.color = GREY

    def draw_tank(self):
        """
        рисует танк
        :return:
        """
        self.rad = 30
        pygame.draw.circle(self.screen, BLACK, (self.center_x, self.center_y), self.rad)

    def hit_test(self, ball):
        """
        проверяет столкнулся ли мяч с танком
        :param ball: мяч
        :return:
        """
        if ((self.center_x - ball.x) ** 2 + (self.center_y - ball.y) ** 2) ** 0.5 < self.rad + ball.r:
            return True
        return False

    def draw(self):
        """
        рисует пушку в данный момент времени
        :return:
        """

        self.draw_tank()
        self.x2 = self.x1 + self.f2_power * math.cos(self.an)
        self.y2 = self.y1 - self.f2_power * math.sin(self.an)
        width = 5
        point1 = (self.x1 + width * math.sin(self.an), self.y1 + width * math.cos(self.an))
        point2 = (self.x1 - width * math.sin(self.an), self.y1 - width * math.cos(self.an))
        point3 = (self.x2 - width * math.sin(self.an), self.y2 - width * math.cos(self.an))
        point4 = (self.x2 + width * math.sin(self.an), self.y2 + width * math.cos(self.an))

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

    def move(self, direction):
        self.x1 += direction
        self.center_x = self.x1 - self.rad * np.cos(self.an)
        self.center_y = self.y1 + self.rad * np.sin(self.an)
        self.x2 = self.x1 + self.f2_power * math.cos(self.an)
        self.y2 = self.y1 - self.f2_power * math.sin(self.an)


class Target:
    def __init__(self, screen):
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
        self.screen = screen
        self.spawn_time = 60

    def draw(self):
        """
        функция рисует цель в данный момент времени
        :return:
        """
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.r)

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

    def spawn_bomb(self, all_balls):
        if self.spawn_time <= 0:
            new_ball = TargetBall(self.screen, self.x, self.y)
            new_ball.r += 5
            new_ball.vy = 0.1
            all_balls.append(new_ball)
            self.spawn_time = 60
            return all_balls
        else:
            self.spawn_time -= 1


class TeleportTarget(Target):
    def __init__(self, screen):
        """
        конструктор класса TeleportTarget
        """
        super(TeleportTarget, self).__init__(screen)
        self.teleport_time = 20

    def move(self):
        """
        изменяет координаты телепортирующейся цели
        :return:
        """
        self.teleport_time -= 1
        if self.teleport_time == 0:
            self.teleport_time = 10
            self.x = rnd.randint(600, 780)
            self.y = rnd.randint(300, 550)


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

    @staticmethod
    def fail_message(screen):
        """
        печатает сообщение о проигрыше
        :param screen:
        :return:
        """
        font1 = pygame.font.Font(None, 36)
        message = "Вы попали в свою пушку и проиграли"
        text1 = font1.render(message, False, BLACK)
        screen.blit(text1, (200, 300))

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
game_over = False
round_finished = 0
player = Player()
clock = pygame.time.Clock()
guns = [Gun(display, 100, 450), Gun(display, 700, 450)]
for count in range(2):
    targets.append(Target(display))
finished = False
k = 1
while not finished:
    display.fill(WHITE)
    if game_over and round_finished == 0:
        player.fail_message(display)
    for gun in guns:
        gun.draw()
    round_finished = 1
    for target in targets:
        if target.live == 1:
            target.move()
            target.draw()
            round_finished = 0
            target.spawn_bomb(balls)
    if player.reset_time == 0 and round_finished == 1:
        player.end_round()
        player.shots = 0
        for count in range(2):
            if rnd.randint(1, 100) in range(1, 33):
                targets.append(TeleportTarget(display))
            else:
                targets.append(Target(display))
    for b in balls:
        b.draw()

    font = pygame.font.Font(None, 36)
    text = font.render(str(score), False, BLACK)
    display.blit(text, (50, 50))
    if not game_over:
        player.show_message(display)
    player.update_time()

    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        if not game_over:
            if event.type == pygame.MOUSEBUTTONDOWN:
                for gun in guns:
                    gun.fire2_start()
            elif event.type == pygame.MOUSEBUTTONUP:
                for gun in guns:
                    balls = gun.fire2_end(balls)
                player.shot_up()
            elif event.type == pygame.MOUSEMOTION:
                for gun in guns:
                    gun.targeting(event)
            if keys[pygame.K_a]:
                guns[0].move(-3)
            elif keys[pygame.K_d]:
                guns[0].move(3)
            if keys[pygame.K_LEFT]:
                guns[1].move(-3)
            elif keys[pygame.K_RIGHT]:
                guns[1].move(3)

    for b in balls:
        b.move()
        for gun in guns:
            if gun.hit_test(b):
                game_over = True
        for target in targets:
            if b.hit_test(target) and target.live and player.reset_time == 0:
                target.live = 0
                score = player.score_up()
        if b.live <= 0:
            balls.remove(b)
    for gun in guns:
        gun.power_up()
    clock.tick(FPS)
    pygame.display.update()
if finished:
    pygame.quit()
