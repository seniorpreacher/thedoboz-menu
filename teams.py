import pygame
from subprocess import call


class Team(pygame.sprite.Sprite):

    def __init__(self, name, pos, command):
        self.name = name
        self.image = pygame.image.load("team_"+name+".png")
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.command = command

        super().__init__()


    def run_game(self):
        call(self.command)