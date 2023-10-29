import pygame
import random

class Gold:

    def __init__(self, width: int, height: int, surface: pygame.Surface, color: str, area: list[int]) -> None:
        self.width = width
        self.height = height
        self.surface = surface
        self.area = area
        self.position_x = random.randint(0, area[0] - self.width)
        self.position_y = random.randint(0, area[1] - self.height)
        self.color = color

        self.gold = pygame.Surface((self.width, self.height))
        self.gold.fill(color)



    def get_gold(self):
        return self.gold.get_rect(topleft=(self.position_x, self.position_y))

    

    def spawn_gold(self):
        self.position_x = random.randint(0, self.area[0] - self.width)
        self.position_y = random.randint(0, self.area[1] - self.height)

        return self.surface.blit(self.gold, (self.position_x, self.position_y))



    def draw(self):
        rect = self.get_gold()
        return self.surface.blit(self.gold, rect)