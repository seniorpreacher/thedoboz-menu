import pygame
import sys
from teams import Team
import teamdata

pygame.init()
size = (1280,1024)
screen = pygame.display.set_mode(size)

obj1 = pygame.image.load("player1.png")
obj1_rect = obj1.get_rect()
obj1_rect.x = 200
obj2 = pygame.image.load("player2.png")
obj2_rect = obj2.get_rect()
obj2_rect.x = 500

#creating teams
game_list = pygame.sprite.Group()

for team in teamdata.teams:
    game_list.add(Team(team["filename"], team["position"], team["command"]))
clock = pygame.time.Clock()
done = False
pygame.key.set_repeat(1, 40)
pygame.joystick.init()
joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
for joy in joysticks:
    joy.init()
joy1 = joysticks[0]
# joy2 = joysticks[1]



while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.JOYAXISMOTION:
            if joy1.get_axis(0) < 0:
                obj1_rect = obj1_rect.move([-4,0])
            if joy1.get_axis(0) > 0:
                obj1_rect = obj1_rect.move([4, 0])
            if joy1.get_axis(1) < 0:
                obj1_rect = obj1_rect.move([0, -4])
            if joy1.get_axis(1) > 0:
                obj1_rect = obj1_rect.move([0, 4])
            # if joy2.get_axis(0) < 0:
            #     obj2_rect = obj2_rect.move([-4, 0])
            # if joy2.get_axis(0) > 0:
            #     obj2_rect = obj2_rect.move([4, 0])
            # if joy2.get_axis(1) < 0:
            #     obj2_rect = obj2_rect.move([0, -4])
            # if joy2.get_axis(1) > 0:
            #     obj2_rect = obj2_rect.move([0, 4])
        if event.type == pygame.JOYBUTTONDOWN:
            if joy1.get_button(0) == 1:
                for game in game_list:
                    gamerect = game.get_rect()
                    if gamerect.contains(obj1_rect) and gamerect.contains(obj2_rect):
                        game.run_game()
            elif joy1.get_button(11) == 1:
                sys.exit()



    screen.fill((241, 196, 15))
    game_list.update()
    game_list.draw(screen)

    screen.blit(obj1, obj1_rect)
    screen.blit(obj2, obj2_rect)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()