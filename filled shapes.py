import pgzrun

WIDTH=400
HEIGHT=400

def draw():
    r=Rect((100,100),(80,40))
    r.center=(100,100)
    screen.draw.rect(r,"red")

    r1=Rect((300,300),(80,40))
    r1.center=(300,300)
    screen.draw.filled_rect(r1,"red")

    screen.draw.circle((300,100),(40),"red")
    screen.draw.filled_circle((100,300),(40),"red")

pgzrun.go()