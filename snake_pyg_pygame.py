import random
from enum import Enum
from collections import deque
from itertools import islice
import pygame
from pygame.transform import flip, rotate
from pygame import Rect
import sys

pygame.init()

TILE_SIZE = 24
TILES_W = 20
TILES_H = 15
WIDTH = TILE_SIZE * TILES_W
HEIGHT = TILE_SIZE * TILES_H
FPS = 15

# Load images (replace with your own image paths or use colored rectangles)


def load_image(name):
    try:
        return pygame.image.load(name).convert_alpha()
    except Exception:
        # fallback: colored surface
        surf = pygame.Surface((TILE_SIZE, TILE_SIZE), pygame.SRCALPHA)
        if name == 'apple.png':
            pygame.draw.ellipse(surf, (255, 0, 0), surf.get_rect())
        elif name == 'snake_head.png':
            pygame.draw.rect(surf, (0, 255, 0), surf.get_rect())
        elif name == 'snake_tail.png':
            pygame.draw.rect(surf, (0, 200, 0), surf.get_rect())
        elif name == 'snake_straight.png':
            pygame.draw.rect(surf, (0, 180, 0), surf.get_rect())
        elif name == 'snake_corner.png':
            pygame.draw.rect(surf, (0, 150, 0), surf.get_rect())
        return surf


images = type('images', (), {
    'apple': load_image('apple.png'),
    'snake_head': load_image('snake_head.png'),
    'snake_tail': load_image('snake_tail.png'),
    'snake_straight': load_image('snake_straight.png'),
    'snake_corner': load_image('snake_corner.png'),
})

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake')
font = pygame.font.SysFont(None, 32)


def screen_rect(tile_pos):
    x, y = tile_pos
    return Rect(TILE_SIZE * x, TILE_SIZE * y, TILE_SIZE, TILE_SIZE)


class Direction(Enum):
    RIGHT = (1, 0)
    UP = (0, -1)
    LEFT = (-1, 0)
    DOWN = (0, 1)

    def opposite(self):
        x, y = self.value
        return Direction((-x, -y))


class Crashed(Exception):
    pass


class Snake:
    def __init__(self, pos=(TILES_W // 2, TILES_H // 2)):
        self.pos = pos
        self.dir = Direction.LEFT
        self.length = 4
        self.tail = deque(maxlen=self.length)
        x, y = pos
        for i in range(self.length):
            p = (x + i, y)
            segment = p, self.dir
            self.tail.append(segment)
        self.alive = True

    @property
    def lastdir(self):
        return self.tail[0][1]

    def move(self):
        dx, dy = self.dir.value
        px, py = self.pos
        px = px + dx
        py = py + dy
        # Border check
        if px < 0 or px >= TILES_W or py < 0 or py >= TILES_H:
            raise Crashed((px, py))
        self.pos = px, py
        segment = self.pos, self.dir
        self.tail.appendleft(segment)
        for t, d in islice(self.tail, 1, None):
            if t == self.pos:
                raise Crashed(t)

    def __len__(self):
        return self.length

    def __contains__(self, pos):
        return any(p == pos for p, d in self.tail)

    def grow(self):
        self.length += 1
        self.tail = deque(self.tail, maxlen=self.length)


class SnakePainter:
    def __init__(self):
        right, up, left, down = (d.value for d in Direction)
        straight = images.snake_straight
        corner = images.snake_corner
        corner2 = flip(corner, True, False)
        self.tiles = {
            (right, right): straight,
            (up, up): rotate(straight, 90),
            (left, left): rotate(straight, 180),
            (down, down): rotate(straight, 270),
            (right, up): corner,
            (up, left): rotate(corner, 90),
            (left, down): rotate(corner, 180),
            (down, right): rotate(corner, 270),
            (left, up): corner2,
            (up, right): rotate(corner2, -90),
            (right, down): rotate(corner2, -180),
            (down, left): rotate(corner2, -270),
        }
        head = images.snake_head
        self.heads = {
            right: head,
            up: rotate(head, 90),
            left: rotate(head, 180),
            down: rotate(head, 270),
        }
        tail = images.snake_tail
        self.tails = {
            right: tail,
            up: rotate(tail, 90),
            left: rotate(tail, 180),
            down: rotate(tail, 270),
        }

    def draw(self, snake):
        for i, (pos, dir) in enumerate(snake.tail):
            if not i:
                tile = self.heads[snake.dir.value]
            elif i >= len(snake.tail) - 1:
                nextdir = snake.tail[i - 1][1]
                tile = self.tails[nextdir.value]
            else:
                nextdir = snake.tail[i - 1][1]
                key = dir.value, nextdir.value
                tile = self.tiles.get(key, self.tiles[dir.value, dir.value])
            r = screen_rect(pos)
            screen.blit(tile, r)


class Apple:
    def __init__(self):
        self.pos = 0, 0

    def draw(self):
        screen.blit(images.apple, screen_rect(self.pos))


KEYBINDINGS = {
    pygame.K_LEFT: Direction.LEFT,
    pygame.K_RIGHT: Direction.RIGHT,
    pygame.K_UP: Direction.UP,
    pygame.K_DOWN: Direction.DOWN,
}

snake = Snake()
snake_painter = SnakePainter()
apple = Apple()


def place_apple():
    if len(snake) == TILES_W * TILES_H:
        raise ValueError("No empty spaces!")
    while True:
        pos = (
            random.randrange(TILES_W),
            random.randrange(TILES_H)
        )
        if pos not in snake:
            apple.pos = pos
            return


def draw():
    screen.fill((0, 0, 0))
    snake_painter.draw(snake)
    apple.draw()
    score_surf = font.render(f'Score: {len(snake)}', True, (255, 255, 255))
    screen.blit(score_surf, (WIDTH - score_surf.get_width() - 5, 5))
    if not snake.alive:
        msg = font.render('You died!', True, (255, 255, 255))
        screen.blit(msg, (WIDTH//2 - msg.get_width() //
                    2, HEIGHT//2 - msg.get_height()//2))
    pygame.display.flip()


def main():
    clock = pygame.time.Clock()
    running = True
    move_event = pygame.USEREVENT + 1
    interval = 400
    pygame.time.set_timer(move_event, interval)
    place_apple()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if not snake.alive:
                    continue
                dir = KEYBINDINGS.get(event.key)
                if dir and dir != snake.lastdir.opposite():
                    snake.dir = dir
            elif event.type == move_event:
                if not snake.alive:
                    continue
                try:
                    snake.move()
                except Crashed:
                    snake.alive = False
                else:
                    if snake.pos == apple.pos:
                        snake.grow()
                        place_apple()
                        interval = max(100, 400 - 30 * (len(snake) - 3))
                        pygame.time.set_timer(move_event, interval)
        draw()
        clock.tick(FPS)
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    main()
