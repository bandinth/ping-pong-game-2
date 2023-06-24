from pygame import*


class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,player_speed,widht,height):
        super().__init__()
        self.image=transform.scale(image.load(player_image),(widht,height))
        self.speed=player_speed
        self.rect=self.image.get_rect()
        self.x=player_x
        self.y=player_y
    def reset(self):
        screen.blit(self.image,(self.rect.x,self.rect.y))

class Player(GameSprite):
    def update_r(self):
        keys=get_pressed()
        if keys["UP"] and self.rect.y>5:
            self.rect.y-=self.speed
        if keys["DOWN"] and self.recy.y<width-80:
            self.rect.y+=self.speed
    def update_l(self):
        if keys["W"] and self.rect.y>5:
            self.rect.y-=self.speed
        if keys["S"] and self.recy.y<width-80:
            self.rect.y+=self.speed
        


width=500
height=700

background=(255,100,20)

screen=display.set_mode((width,height))
screen.fill(background)
display.set_caption("Пінг Понг")

clock=time.Clock()

finish=False
game=True

FPS=60

racket1=Player("raket.png",30,200,4,50,150)
racket2=Player("raket.png",520,200,4,50,150)
ball=Player("ball.png",200,200,4,50,50)

font.init()
lose1=font.render("Player 1 LOSE!",True,(255,0,0))
lose2=font.render("Player 2 LOSE!",True,(255,0,0))

speed_x=3
speed_y=3


while not finish:
    for e in event.get():
        if e.type==QUIT:
            game=False
    if finish!=True:
        racket1.update_r()
        racket2.update_l()
        ball.rect.x+=speed_x
        ball.rect.y+=speed_y

        if sprite.collide_rect(racket1,ball) or sprite.collide_rect(racket2,ball):
            speed_x*=-1
            speed_y*=1
        if ball.rect.y>width-50 or ball.rect.y<0:
            speed_x*=-1

        if ball.rect.x<0:
            finish=True
            screen.blit(lose1,(200,200))
        if ball.rect.x>width:
            finish=True
            screen.blit(lose2,(200,200))
        raket1.reset()
        raket2.reset()
        ball.reset()
            
            
    display.update()
    clock.tick(FPS)
