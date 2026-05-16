import sys
import pygame

class AlienInvasion:
    "General class for managing game resources and behavior"
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        "Start the main loop for the game"
        while True:
            # search for keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            # makes the last drawn screen visible
            pygame.display.flip()
    
if __name__ == '__main__':
    # make a game instance and run the game
    ai = AlienInvasion()
    ai.run_game()