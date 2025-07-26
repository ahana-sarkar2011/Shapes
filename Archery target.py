import pgzrun
import random
WIDTH=400
HEIGHT=400

def draw():
    r=175
    for i in range(7):
        r1=70
        g=20
        b=random.randint(0,255)
        screen.draw.filled_circle((200,200),r,(r1,g,b))
        r=r-25

pgzrun.go()