from pygame import *
from random import randint

window = display.set_mode((1080,720))
display.set_caption("Пингпонг")
background = transform.scale(image.load("background_material.jpg"), (1080,720))
keys_pressed = key.get_pressed()
clock = time.Clock()
FPS = 60
font.init()
font = font.SysFont('Arial', 40)
text = font.render("Ты проиграл!", True, (255,255,255))

speed_x = 3
speed_y = 3

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
ball = Gamesprite("circle_PNG71.png", 500, 500, 10, 70, 70)

class Player(Gamesprite):
    def update(self):

        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed

        if keys_pressed[K_s] and self.rect.y < 570:
            self.rect.y += self.speed
plr1 = Player("pngwing.com.png", 25, 300, 10, 75, 150)

finish = False
game = True
while game:

    for e in event.get():
        if e.type == QUIT:
            game = False
            
    if finish != True:
        window.blit(background,(0,0))
        window.blit(ball,(500,500))
        keys_pressed = key.get_pressed()
        plr1.update()
        plr1.reset()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        clock.tick(FPS)

        display.update() 
