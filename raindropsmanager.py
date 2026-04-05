import pygame
import sys
import random
import time
from raindrop import Raindrop


class RaindropsManager:
    """Manages the raindrop simulation window and handles the main loop."""
    
    RAIN_RATE = 0.1  # Time in seconds between new raindrops
    MAX_RADIUS = 100  # Maximum radius before raindrop is removed
    WINDOW_WIDTH = 800
    WINDOW_HEIGHT = 600
    FPS = 60
    
    def __init__(self):
        """Initialize the RaindropsManager."""
        pygame.init()
        self.screen = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        pygame.display.set_caption("Raindrops on Glass")
        self.clock = pygame.time.Clock()
        self.running = True
        self.raindrops = []
        self.last_raindrop_time = time.time()
    
    def handle_events(self):
        """Handle input events like window close."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
    
    def update(self):
        """Update the simulation state."""
        current_time = time.time()
        
        # Create a new raindrop if enough time has passed
        if current_time - self.last_raindrop_time >= self.RAIN_RATE:
            x = random.randint(0, self.WINDOW_WIDTH - 1)
            y = random.randint(0, self.WINDOW_HEIGHT - 1)
            self.raindrops.append(Raindrop(x, y))
            self.last_raindrop_time = current_time
        
        # Update all raindrops and remove those that exceed MAX_RADIUS
        self.raindrops = [raindrop for raindrop in self.raindrops if raindrop.radius <= self.MAX_RADIUS]
        for raindrop in self.raindrops:
            raindrop.update()
    
    def draw(self):
        """Draw the window and all raindrops."""
        self.screen.fill((200, 220, 240))  # Light blue background (sky)
        
        # Draw all raindrops
        for raindrop in self.raindrops:
            raindrop.draw(self.screen)
        
        pygame.display.flip()
    
    def run(self):
        """Main loop that handles events, updates, and drawing."""
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(self.FPS)
        
        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    manager = RaindropsManager()
    manager.run()
