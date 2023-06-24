from pygame import *
from random import *
window = display.set_mode((400,500))
display.set_caption("CS:GO TESAK EDITION")

mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()
mixer.music.set_volume(0.1)
fire_sound = mixer.Sound('fire.ogg')


class GameSprite(sprite.Sprite):
    def __init__(self, pl_image, pl_x, pl_y, size_x, size_y, pl_speed):
        super().__init__()
        self.image = transform.scale(image.load(pl_image),(size_x, size_y))
        self.speed = pl_speed
        self.rect = self.image.get_rect()
        self.rect.x = pl_x
        self.rect.y = pl_y
    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Bullet(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y < 0:
            self.kill()

class Player(GameSprite):
    def update (self):
        keys = key.get_pressed()
        if keys[K_RIGHT] and self.rect.x < 320:
            self.rect.x += self.speed
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed

        
    def fire(self):
        fire_sound.play()
        bullet = Bullet('bullet.png', self.rect.centerx, self.rect.top, 15, 20, -20)
        bullets.add(bullet)
        




class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y > 500:
            self.rect.x = randint(0, 400)
            self.rect.y = 0
            lost += 1
            
            


monsters = sprite.Group()
for i in range(1,6):
    monster = Enemy("ufo.png", randint(0, 450), -40, 50, 50, randint(1,5))
    monsters.add(monster)

bullets = sprite.Group()


finish = False

background = transform.scale(image.load("galaxy.jpg"),(400,500))

max_lost = 3

ship = Player("rocket.png", 100, 400, 80, 100, 10)
import sys

font.init()
score = 0
lost = 0
mainfont = font.SysFont(None, 30)
win = mainfont.render("YOU WIN", True, (0, 255, 0))
lose = mainfont.render("YOU LOSE", True, (255, 0, 0))
num_fire = 0
rel_time = False
from time import time as timer
while True:
    for e in event.get():
        if e.type == QUIT:
            sys.exit()
        if e.type == KEYDOWN:

            if e.key == K_SPACE:
                if num_fire < 5 and rel_time == False:
                    num_fire += 1
                    ship.fire()
                if num_fire >=5 and rel_time == False:
                    last_time = timer ()
                    rel_time = True


            if e.key == K_ESCAPE:
                sys.exit()
 
    if not finish: #КОЛИ ПЕРЕРВА
        window.blit(background, (0, 0))
        text_rah =mainfont.render("Score:" + str(score), True, (0,255,0))
        text_skip =mainfont.render("Mises:" + str(lost), True, (255,0,0))
        window.blit(text_rah, (10,10))
        window.blit(text_skip, (10,50))
        ship.update()
        ship.draw()
        bullets.draw(window)
        bullets.update()
        monsters.update()
        monsters.draw(window)


        if rel_time == True:
            now_time = timer()
            if now_time - last_time < 3:
                reloadfont = font.Font("minecraftruss.ttf", 20)
                reload = reloadfont.render("У НАС НЕХВАТКА БОЕПРИПАСОВ", True, (255,255,255))
                reload2 = reloadfont.render("70%", True, (255,0,0))
                window.blit(reload, (20, 450))
                window.blit(reload2, (180  , 470))

            else:
                num_fire = 0
                rel_time = False

        colides = sprite.groupcollide(monsters, bullets, True, True)
        for c in colides:
            score +=1
            monster = Enemy("ufo.png", randint(0, 450), -40, 50, 50, randint(1,5))
            monsters.add(monster)
        if sprite.spritecollide(ship, monsters, False) or lost > 1 :
            finish = True
            fire_sound.set_volume(0)
            window.blit(lose, (150, 200))
        if score >= 10:
            finish =True
            fire_sound.set_volume(0)
            window.blit(win , (150, 200))

    display.update()

    time.delay(50)





























































































































































































































































































































































































































































































































































































































































































































































































































































































































































print("Hello World")