import sys
import pygame

class AlienInvasion:
    "General class for managing game resources and behavior"
    def __init__(self):
        pygame.init()
        self.clock= pygame.time.Clock()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")

        # Set the background color
        self.bg_color = (230, 230, 230)


    def run_game(self):
        "Start the main loop for the game"
        while True:
            # search for keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            # Redraws the screen at each step through the loop
            self.screen.fill(self.bg_color)
            # makes the last drawn screen visible
            pygame.display.flip()

            self.clock.tick(60) # limits the game to 60 frames per second
    
if __name__ == '__main__':
    # make a game instance and run the game
    ai = AlienInvasion()
    ai.run_game()