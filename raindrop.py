import pygame


class Raindrop:
    """Represents a raindrop on the glass with a ripple effect."""
    
    __slots__ = ['x', 'y', 'radius']
    
    def __init__(self, x, y):
        """Initialize a raindrop at position (x, y) with radius 1.
        
        Args:
            x: The x-coordinate of the raindrop center.
            y: The y-coordinate of the raindrop center.
        """
        self.x = x
        self.y = y
        self.radius = 1
    
    def draw(self, window):
        """Draw the raindrop as a blue circle on the window.
        
        Args:
            window: The pygame surface to draw on.
        """
        pygame.draw.circle(window, (100, 150, 255), (self.x, self.y), self.radius)
    
    def update(self):
        """Increase the radius of the raindrop by 1."""
        self.radius += 1
