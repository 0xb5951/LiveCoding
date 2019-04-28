import time

flag = True

b2 >> blip(oct=[1, 3, 1, 4], dur=1/2) + [(2, 4, 6), (1, 3, 5)]

d1 >> play("--xo--*(ox, oo)x", dur=1/2)

p2 >> play('Nothingisimpossible', amp=2)

p3 >> play('tomorrow is rainy')

for x in range(3):
    if flag == True:
        b1 >> blip(oct=4, dur=1/3) + [2, 6, 8]
        flag = False
        time.sleep(1)
    else:
        b1 >> blip(oct=4, dur=1/3) + [3, 7, 9]
        flag = True
        time.sleep(1)
        
Clock.bpm = 200
