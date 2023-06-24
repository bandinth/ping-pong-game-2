from pygame import*
width=500
height=700

background=(255,100,20)

screen=display.set_mode((width,height))
screen.fill(background)
display.set_caption("Пінг Понг")

clock=time.Clock()

finish=False

while not finish:
    for e in event.get():
        if e.type==QUIT:
            finish=True
    
    display.update()
    clock.tick(40)
