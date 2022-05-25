from modules.settings import *
import os


class Food:
    def __init__(self, main_background):
        self.screen = main_background
        self.food = pygame.image.load(os.path.abspath("snake_game//resources/krem.jpg"))
        self.x = random.randint(0, (WIDTH / snake_cell_size) - 1) * snake_cell_size
        self.y = random.randint(0, (HEIGHT / snake_cell_size) - 1) * snake_cell_size

    def draw_food(self):
        self.screen.blit(self.food, (self.x, self.y))

    def move_food(self):
        self.x = random.randint(0, (WIDTH / snake_cell_size) - 1) * snake_cell_size
        self.y = random.randint(0, (HEIGHT / snake_cell_size) - 1) * snake_cell_size
