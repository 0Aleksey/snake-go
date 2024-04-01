import os
import sys

import pygame
import random

pygame.init()
screen_width = 600
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Змейка")
green = (0, 255, 0)
red = (255, 0, 0)
font = pygame.font.SysFont("Arial", 20)
clock = pygame.time.Clock()

cell_size = 20
snake_speed = 5
snake_length = 3
snake_count = 0
snake_body = []

FPS = 50


def terminate():
    pygame.quit()
    sys.exit()


def load_outro_win(name, colorkey=None):
    fullname = os.path.join('', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


def win_screen():
    intro_text = []
    fon = pygame.transform.scale(load_outro('you-win.png'), (screen_width, screen_height))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('black'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                return
        pygame.display.flip()
        clock.tick(FPS)


def load_outro(name, colorkey=None):
    fullname = os.path.join('', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


def game_over_screen():
    intro_text = []
    fon = pygame.transform.scale(load_outro('backfon.png'), (screen_width, screen_height))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('black'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                return
        pygame.display.flip()
        clock.tick(FPS)


def load_image(name, colorkey=None):
    fullname = os.path.join('', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


def start_screen():
    intro_text = ["Играть"]
    fon = pygame.transform.scale(load_image('fon.png'), (screen_width, screen_height))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('black'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                return  # начинаем игру
        pygame.display.flip()
        clock.tick(FPS)


for i in range(snake_length):
    snake_body.append(pygame.Rect((screen_width / 2) - (cell_size * i), screen_height / 2, cell_size, cell_size))
snake_direction = "right"
new_direction = "right"

apple_position = pygame.Rect(random.randint(0, screen_width - cell_size),
                             random.randint(0, screen_height - cell_size), cell_size, cell_size)

apple_position_gold = pygame.Rect(random.randint(0, screen_width - cell_size),
                                  random.randint(0, screen_height - cell_size), cell_size, cell_size)

apple_position_black = pygame.Rect(random.randint(0, screen_width - cell_size),
                                   random.randint(0, screen_height - cell_size), cell_size, cell_size)

apple_position_fire = pygame.Rect(random.randint(0, screen_width - cell_size),
                                  random.randint(0, screen_height - cell_size), cell_size, cell_size)

apple_position_pyrpyr = pygame.Rect(random.randint(0, screen_width - cell_size),
                                    random.randint(0, screen_height - cell_size), cell_size, cell_size)

game_over = False
start_screen()
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_direction != "down":
                new_direction = "up"
            elif event.key == pygame.K_DOWN and snake_direction != "up":
                new_direction = "down"
            elif event.key == pygame.K_LEFT and snake_direction != "right":
                new_direction = "left"
            elif event.key == pygame.K_RIGHT and snake_direction != "left":
                new_direction = "right"

    if snake_count >= 25:
        snake_speed = 7
    if snake_count >= 50:
        snake_speed = 9
    if snake_count >= 75:
        snake_speed = 12
    if snake_count >= 125:
        snake_speed = 15
    if snake_count > 180:
        snake_speed = 20
    if snake_count > 250:
        snake_speed = 25

    if snake_count == 300:
        game_over = True
        win_screen()

    snake_direction = new_direction
    if snake_direction == "up":
        snake_body.insert(0, pygame.Rect(snake_body[0].left, snake_body[0].top - cell_size, cell_size, cell_size))
    elif snake_direction == "down":
        snake_body.insert(0, pygame.Rect(snake_body[0].left, snake_body[0].top + cell_size, cell_size, cell_size))
    elif snake_direction == "left":
        snake_body.insert(0, pygame.Rect(snake_body[0].left - cell_size, snake_body[0].top, cell_size, cell_size))
    elif snake_direction == "right":
        snake_body.insert(0, pygame.Rect(snake_body[0].left + cell_size, snake_body[0].top, cell_size, cell_size))

    if snake_body[0].colliderect(apple_position):
        snake_length += 2
        snake_count += 1
        apple_position = pygame.Rect(random.randint(0, screen_width - cell_size),
                                     random.randint(0, screen_height-cell_size), cell_size, cell_size)
        apple_position_gold = pygame.Rect(random.randint(0, screen_width - cell_size),
                                          random.randint(0, screen_height-cell_size), cell_size, cell_size)
        apple_position_fire = pygame.Rect(random.randint(0, screen_width - cell_size),
                                          random.randint(0, screen_height-cell_size), cell_size, cell_size)
        apple_position_black = pygame.Rect(random.randint(0, screen_width - cell_size),
                                           random.randint(0, screen_height - cell_size), cell_size, cell_size)
        apple_position_pyrpyr = pygame.Rect(random.randint(0, screen_width - cell_size),
                                            random.randint(0, screen_height - cell_size), cell_size, cell_size)
        if snake_count < 25:
            snake_speed = 5
        if snake_count >= 25:
            snake_speed = 7
        if snake_count >= 50:
            snake_speed = 9
        if snake_count >= 75:
            snake_speed = 11
        if snake_count >= 125:
            snake_speed = 12
        if snake_count > 180:
            snake_speed = 14
        if snake_count > 250:
            snake_speed = 16

    if snake_body[0].colliderect(apple_position_gold):
        apple_position = pygame.Rect(random.randint(0, screen_width - cell_size),
                                     random.randint(0, screen_height-cell_size), cell_size, cell_size)
        apple_position_gold = pygame.Rect(random.randint(0, screen_width - cell_size),
                                          random.randint(0, screen_height-cell_size), cell_size, cell_size)
        apple_position_fire = pygame.Rect(random.randint(0, screen_width - cell_size),
                                          random.randint(0, screen_height-cell_size), cell_size, cell_size)
        apple_position_black = pygame.Rect(random.randint(0, screen_width - cell_size),
                                           random.randint(0, screen_height - cell_size), cell_size, cell_size)
        apple_position_pyrpyr = pygame.Rect(random.randint(0, screen_width - cell_size),
                                            random.randint(0, screen_height - cell_size), cell_size, cell_size)
        snake_length += 3
        snake_count += 1
        if snake_count < 50:
            snake_speed = 8
        if (snake_count > 50) and (snake_count < 1000):
            snake_speed += 1

    if snake_body[0].colliderect(apple_position_pyrpyr):
        apple_position = pygame.Rect(random.randint(0, screen_width - cell_size),
                                     random.randint(0, screen_height-cell_size), cell_size, cell_size)
        apple_position_gold = pygame.Rect(random.randint(0, screen_width - cell_size),
                                          random.randint(0, screen_height-cell_size), cell_size, cell_size)
        apple_position_fire = pygame.Rect(random.randint(0, screen_width - cell_size),
                                          random.randint(0, screen_height-cell_size), cell_size, cell_size)
        apple_position_black = pygame.Rect(random.randint(0, screen_width - cell_size),
                                           random.randint(0, screen_height - cell_size), cell_size, cell_size)
        apple_position_pyrpyr = pygame.Rect(random.randint(0, screen_width - cell_size),
                                            random.randint(0, screen_height - cell_size), cell_size, cell_size)
        if snake_count < 25:
            snake_speed = 3
        if (snake_count > 25) and (snake_count < 1000):
            snake_speed -= 1

    if snake_body[0].colliderect(apple_position_fire):
        apple_position = pygame.Rect(random.randint(0, screen_width - cell_size),
                                     random.randint(0, screen_height-cell_size), cell_size, cell_size)
        apple_position_gold = pygame.Rect(random.randint(0, screen_width - cell_size),
                                          random.randint(0, screen_height-cell_size), cell_size, cell_size)
        apple_position_fire = pygame.Rect(random.randint(0, screen_width - cell_size),
                                          random.randint(0, screen_height-cell_size), cell_size, cell_size)
        apple_position_black = pygame.Rect(random.randint(0, screen_width - cell_size),
                                           random.randint(0, screen_height - cell_size), cell_size, cell_size)
        apple_position_pyrpyr = pygame.Rect(random.randint(0, screen_width - cell_size),
                                            random.randint(0, screen_height - cell_size), cell_size, cell_size)
        snake_length += 5
        snake_count += 1
        if snake_count < 125:
            snake_speed = 11
        if (snake_count > 125) and (snake_count < 1000):
            snake_speed += 1

    if snake_body[0].colliderect(apple_position_black):
        game_over = True

    if len(snake_body) > snake_length:
        snake_body.pop()

    if snake_body[0].left < 0 or snake_body[0].right > screen_width or snake_body[0].top < 0 or \
            snake_body[0].bottom > screen_height:
        game_over = True

    for i in range(1, len(snake_body)):
        if snake_body[0].colliderect(snake_body[i]):
            game_over = True

    screen.fill((120, 170, 255))
    for i in range(len(snake_body)):
        if i == 0:
            pygame.draw.circle(screen, green, snake_body[i].center, cell_size / 2)
        else:
            pygame.draw.circle(screen, green, snake_body[i].center, cell_size / 2)
            pygame.draw.circle(screen, (0, 200, 0), snake_body[i].center, cell_size / 4)

    pygame.draw.circle(screen, red, apple_position.center, cell_size / 2)
    pygame.draw.circle(screen, (255, 223, 0), apple_position_gold.center, cell_size / 2)
    pygame.draw.circle(screen, (10, 10, 10), apple_position_black.center, cell_size / 2)
    pygame.draw.circle(screen, (230, 86, 30), apple_position_fire.center, cell_size / 2)
    pygame.draw.circle(screen, (148, 0, 211), apple_position_pyrpyr.center, cell_size / 2)

    score_text = font.render(f"Съедено яблок: {snake_count}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))
    pygame.display.update()

    clock.tick(snake_speed)
if snake_count < 300:
    game_over_screen()
pygame.quit()
