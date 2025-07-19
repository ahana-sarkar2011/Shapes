import pgzrun
import random

WIDTH=400
HEIGHT=400

def draw():
    screen.fill("pink")
    x=400
    y=100
    
    for i in range(30):
        r1=random.randint(0,255)
        g=random.randint(0,255)
        b=random.randint(0,255)
        r=Rect((200,200),(x,y))
        r.center=(200,200)
        screen.draw.rect(r,(r1,g,b))
        x=x-10
        y=y+10
    screen.draw.text("AHANA",center=(200,200),color="blue")

pgzrun.go()    