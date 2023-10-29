import pygame

class Player:

    def __init__(self, width: int, height: int, surface: pygame.Surface, position_x: int, position_y: int, color: str, speed: int, area: list[int]) -> None:
        self.width = width
        self.height = height
        self.surface = surface
        self.position_x = position_x
        self.position_y = position_y
        self.area_x = area[0]
        self.area_y = area[1]
        self.speed = speed
        self.color = color

        self.player = pygame.Surface((self.width, self.height))
        self.player.fill(color)



    def get_player(self):
        return self.player.get_rect(topleft=(self.position_x, self.position_y))
    
    

    def get_position(self):
        return (self.position_x, self.position_y)
        


    def draw(self):
        self.moving()
        rect = self.get_player()
        return self.surface.blit(self.player, rect)
    


    def moving(self):

        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            if self.position_x + self.width < self.area_x:
                self.position_x += self.speed

        if keys[pygame.K_LEFT]:
            if self.position_x > 0:
                self.position_x -= self.speed

        if keys[pygame.K_UP]:
            if self.position_y > 0:
                self.position_y -= self.speed

        if keys[pygame.K_DOWN]:
            if self.position_y + self.height < self.area_y:
                self.position_y += self.speed