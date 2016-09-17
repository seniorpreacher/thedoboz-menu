import pygame
from subprocess import call


class Team(pygame.sprite.Sprite):



    def __init__(self, name, pos, command):
        self.name = name
        self.image = pygame.image.load("team_"+name+".png")
        self.imagerect = self.image.get_rect()
        self.imagerect.x = pos[0]
        self.imagerect.y = pos[1]
        self.command = command


    def run_game(self):
        call(self.command)