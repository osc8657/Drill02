from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

while(1):
    x = 390

    while (x < 780):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, 90)
        x = x + 2
        delay(0.01)

    y = 90

    while (y < 560):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x, y)
        y=y+2
        delay(0.01)

    while (x > 20):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x = x - 2
        delay(0.01)

    while (y > 90):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        y=y-2
        delay(0.01)

    while (x < 400):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, 90)
        x = x + 2
        delay(0.01)


    r = 0

    r=270

    while (r<360):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(300 * math.cos(r/360*2*math.pi) + x, 300 * math.sin(r/360*2*math.pi) + 300 + y)
        r = r + 2
        delay(0.01)

    r=0
    while (r<270):
       clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(300 * math.cos(r/360*2*math.pi) + x, 300 * math.sin(r/360*2*math.pi) + 300 + y)
        r = r + 2
        delay(0.01)

close_canvas()
