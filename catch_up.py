from pygame import *
#создай окно игры

win = display.set_mode((700, 500))
clock = time.Clock()
background = transform.scale(image.load("background.png").convert_alpha(), (700, 500))
#задай фон сцены

#создай 2 спрайта и размести их на сцене
sprite1 = transform.scale(image.load("sprite1.png").convert_alpha(), (100, 100))
sprite2 = transform.scale(image.load("sprite2.png").convert_alpha(), (100, 100))
x1 = 100
y1 = 400
#обработай событие «клик по кнопке "Закрыть окно"»
game = True
while game:
    keys_pressed = key.get_pressed()
    win.blit(background, (0,0))
    win.blit(sprite1, (x1,y1))
    for e in event.get():
        if e.type == QUIT:
            game = False
    if keys_pressed[K_UP] and y1 > 4:
        y1 -= 5
    if keys_pressed[K_DOWN] and y1 < 396:
        y1 += 5
    if keys_pressed[K_RIGHT] and x1 < 596:
        x1 += 5
    if keys_pressed[K_LEFT] and x1 > 4:
        x1 -= 5    
    display.update()
    clock.tick(60)