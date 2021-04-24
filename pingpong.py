from pygame import *
from random import randint

'''window = display.set_mode((1080,720))
display.set_caption("Пингпонг")

background = transform.scale(image.load("castle.png"), (1080,720))

keys_pressed = key.get_pressed()

clock = time.Clock()
FPS = 60

font.init()
font = font.SysFont('Times New Roman', 40)
text = font.render("Ты проиграл!", True, (255,255,255))'''
   
class Gamesprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, player_width, player_hight):
        super().__init__()
        self.width = player_width
        self.hight = player_hight
        self.image = transform.scale(image.load(player_image), (player_width, player_hight))

        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(Gamesprite):
    def update(self):

        if keys_pressed[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed

        if keys_pressed[K_d] and self.rect.x < 1030:
            self.rect.x += self.speed


class Enemy(Gamesprite):
    def update(self):
        global lost
        if self.rect.y <= 700:
            self.rect.y += self.speed
        else:
            self.rect.y = randint(-500,0)
            self.rect.x = randint(0,1000)
            lost += 1




finish = False
game = True
while game:

    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        display.update()