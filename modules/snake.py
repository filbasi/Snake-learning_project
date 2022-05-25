from modules.settings import *
import os


class Snake:
    def __init__(self, main_background, length):
        self.screen = main_background
        # self.head = pygame.image.load("snake//resources//block.jpg")
        # self.body = pygame.image.load("snake//resources//block111.jpg")
        self.head = pygame.image.load(
            os.path.abspath("snake_game//resources//block.jpg")
        )
        self.body = pygame.image.load(
            os.path.abspath("snake_game//resources//block111.jpg")
        )
        self.length = length
        self.x = [WIDTH / 2] * self.length
        self.y = [HEIGHT / 2] * self.length
        self.direction = "down"

    def draw_head(self):
        self.screen.blit(self.head, (self.x[0], self.y[0]))

    def draw_body(self):
        for i in range(self.length - 1):
            self.screen.blit(self.body, (self.x[i + 1], self.y[i + 1]))

    def move_body(self):
        for i in reversed(range(self.length - 1)):
            self.x[i + 1] = self.x[i]
            self.y[i + 1] = self.y[i]

    def move_up(self):
        # self.move_body()
        # self.y[0] -= snake_cell_size
        if not (self.direction == "down"):
            self.direction = "up"

    def move_down(self):
        # self.move_body()
        # self.y[0] += snake_cell_size
        if not (self.direction == "up"):
            self.direction = "down"

    def move_right(self):
        # self.move_body()
        # self.x[0] += snake_cell_size
        if not (self.direction == "left"):
            self.direction = "right"

    def move_left(self):
        # self.move_body()
        # self.x[0] -= snake_cell_size
        if not (self.direction == "right"):
            self.direction = "left"

    def snake_movement(self):

        if self.direction == "up":
            # self.move_body
            self.y[0] -= snake_cell_size

        if self.direction == "down":
            # self.move_body
            self.y[0] += snake_cell_size

        if self.direction == "right":
            # self.move_body
            self.x[0] += snake_cell_size

        if self.direction == "left":
            # self.move_body
            self.x[0] -= snake_cell_size

    def snake_speed(time_value):
        clock.tick(time_value)
