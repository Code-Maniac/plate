import pygame
import sys
from settings import WIDTH, HEIGHT, FPS
from debug import debug


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('_PROJECTNAME_')
        self.clock = pygame.time.Clock()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill('black')
            debug(f"{pygame.mouse.get_pos()}")
            pygame.display.update()
            self.clock.tick(FPS)


def main():
    g = Game()
    g.run()


if __name__ == "__main__":
    main()
