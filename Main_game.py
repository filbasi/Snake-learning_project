from modules.settings import *
from pygame.locals import *
from modules.food import *
from modules.snake import *


class Main_game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.snake = Snake(self.screen, length)
        # self.Snake.draw_head()
        # self.Snake.draw_body()
        self.food = Food(self.screen)
        # self.Food.draw_food()
        # self.Food.move_food()

    def play(self):
        self.background()
        self.snake.snake_movement()
        self.food.draw_food()
        self.snake.draw_body()
        self.snake.draw_head()
        self.collision_with_food()
        self.snake.move_body()
        self.print_score()
        self.collision_with_body()
        self.collision_with_border()
        pygame.display.flip()

    def collision(self, x0, y0, xi, yi):
        if x0 >= xi and x0 < xi + snake_cell_size:
            if y0 >= yi and y0 < yi + snake_cell_size:
                return True
        return False

    def collision_with_food(self):
        # if (
        #     abs(self.snake.x[0] - self.food.x) < snake_cell_size
        #     and abs(self.snake.y[0] - self.food.y) < snake_cell_size
        # ):
        if self.collision(self.snake.x[0], self.snake.y[0], self.food.x, self.food.y):
            self.food.move_food()
            self.snake.length += 1
            # Snake.snake_speed.time_value += 1
            self.snake.x.append(self.snake.x[0])
            self.snake.y.append(self.snake.y[0])

    def collision_with_body(self):
        # for i in range(3, self.snake.length):
        #     if (
        #         abs(self.snake.x[0] - self.food.x[i]) < snake_cell_size
        #         and abs(self.snake.y[0] - self.food.y[i]) < snake_cell_size
        #     ):
        #         raise "You lost"
        for i in range(3, self.snake.length):
            if self.collision(
                self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]
            ):
                raise "You lost"

    def collision_with_border(self):
        if not (0 <= self.snake.x[0] <= WIDTH and 0 <= self.snake.y[0] <= HEIGHT):
            raise "You hit the border. Game Over"

    def print_score(self):
        font = pygame.font.SysFont("arial", 30)
        score = font.render(f"Score is: {self.snake.length}", True, (255, 255, 255))
        self.screen.blit(score, (1000, 10))

    def print_game_over(self):
        self.background()
        font = pygame.font.SysFont("arial", 40)
        game_over = font.render(
            f"Game Over. Your score is: {self.snake.length}", True, (255, 255, 255)
        )
        self.screen.blit(game_over, (400, 200))
        game_continue = font.render(
            "Press Enter if you want to continue. Otherwise press ESC",
            True,
            (255, 255, 255),
        )
        self.screen.blit(game_continue, (250, 400))
        pygame.display.flip()

    def reset(self):
        self.snake = Snake(self.screen, 1)
        self.food = Food(self.screen)

    def background(self):
        self.theme = pygame.image.load("programming_material/resources//background.jpg")
        self.screen.blit(self.theme, (0, 0))

    def game(self):
        continue_game = True
        running_game = True
        while running_game:

            k = pygame.key.get_pressed()
            if k[pygame.K_x]:
                t = 15
            else:
                t = 5

            for event in pygame.event.get():

                if event.type == KEYDOWN:

                    if event.key == K_RETURN:
                        continue_game = True
                    if event.key == K_ESCAPE:
                        running_game = False

                    if event.key == K_UP:
                        self.snake.move_up()
                    if event.key == K_DOWN:
                        self.snake.move_down()
                    if event.key == K_RIGHT:
                        self.snake.move_right()
                    if event.key == K_LEFT:
                        self.snake.move_left()

            # self.Snake.snake_movement()
            try:
                if continue_game:
                    self.play()
            except:
                self.print_game_over()
                continue_game = False
                self.reset()
            # clock.tick(t)
            Snake.snake_speed(t)


if __name__ == "__main__":
    game = Main_game()
    game.game()
