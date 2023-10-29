import pygame
import tkinter
from tkinter import messagebox
from sys import exit
import datetime 

import settings
from player import Player
from gold import Gold

class Game_start:

    def __init__(self) -> None:

        pygame.init()
        pygame.display.set_caption(settings.WINDOW_TITLE)

        self.set_soundtracks()

        self.screen = pygame.display.set_mode((settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT), pygame.NOFRAME)
        pygame.display.set_icon(pygame.image.load(settings.PATH_ICON))
        self.screen.fill(settings.WINDOW_BACKGROUND_COLOR)

        self.points = 0
        self.speed = settings.PLAYER_SPEED
        self.time = settings.PLAYER_TIME

        self.font = pygame.font.Font(settings.FONT_FAMILY_PATH, settings.FONT_SIZE)
        self.points_text = self.font.render(f'points  {self.points}', True, settings.FONT_COLOR)
        self.time_text = self.font.render(f'Time {self.time}', True, settings.FONT_COLOR)

        self.start_time = datetime.datetime.now().second

        self.player = Player(settings.PLAYER_WIDTH, settings.PLAYER_HEIGHT, self.screen, settings.WINDOW_WIDTH // 2 - 30, settings.WINDOW_HEIGHT // 2 - 30, settings.PLAYER_COLOR, self.speed, [settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT])
        self.gold = Gold(settings.GOLDEN_WIDTH, settings.GOLDEN_HEIGHT, self.screen, settings.GOLDEN_COLOR, [settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT])
        self.clock = pygame.time.Clock()



        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit_the_game()


            self.screen.fill(settings.WINDOW_BACKGROUND_COLOR)
            self.player.draw()
            self.gold.draw()

            self.screen.blit(self.points_text, (10, 0))
            self.screen.blit(self.time_text, (settings.WINDOW_WIDTH // 1.2, 0))

            self.event_collection_gold()
            self.update_time()

            pygame.display.update()
            self.clock.tick(settings.FPS)




    def quit_the_game(self):
        pygame.quit()
        exit()



    def show_message(self):
        root = tkinter.Tk()
        root.withdraw()

        messagebox.showinfo("Game over",f'you scored {self.points} points')


    def show_points(self):
        self.points_text = self.font.render(f'points  {self.points}', True, settings.FONT_COLOR)



    def set_soundtracks(self):
        pygame.mixer.music.load(settings.PATH_SOUND_2)
        pygame.mixer.music.play(-1, 0, 0)

        self.sound1 = pygame.mixer.Sound(settings.PATH_SOUND_1)
        self.sound2 = pygame.mixer.Sound(settings.PATH_SOUND_3)



    def update_time(self):

        second = datetime.datetime.now().second

        self.time = second - self.start_time

        if self.time > settings.PLAYER_TIME:
            self.time = settings.PLAYER_TIME

        if self.time < 0:
            self.time = 60 - abs(second - self.start_time)


        self.time_text = self.font.render(f'Time { 3 - (self.time)}', True, settings.FONT_COLOR)


        if self.time == settings.PLAYER_TIME:
            pygame.mixer.music.pause()
            self.show_message()
            self.quit_the_game()



    def speed_up(self, speed):
        self.speed += speed
        position = self.player.get_position()
        self.player = Player(settings.PLAYER_WIDTH, settings.PLAYER_HEIGHT, self.screen, position[0], position[1], settings.PLAYER_COLOR, self.speed, [settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT])



    def event_collection_gold(self):
        player_rect = self.player.get_player()
        gold_rect = self.gold.get_gold()

        if player_rect.colliderect(gold_rect):
            self.gold.spawn_gold()
                
            self.points += 10
            self.show_points()

            self.start_time = datetime.datetime.now().second

            if self.points % 100 == 0:
                self.sound2.play()
                self.speed_up(0.5)

            else: self.sound1.play()


if __name__ == '__main__':
    Game_start()