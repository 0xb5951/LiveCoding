ch = var([0, 5, 2, 3], [8, 4, 2, 2])

p1 >> pluck(ch, dur=[1/2, 1/4, 1/4])

wo >> play("[(fuck)]", dur=1/2)

bd >> play("(x )(-[-x])")
h1 >> play("-- --- - [-- - - - ]", dur=1/2)

b2 >> bass(ch, dur=PSum(3, 2))
b1 >> bass(ch, dur=[1/4, 1/2]*4)

xx >> play("Xvs[+x]", dur=1/2)

be >> bell(ch, dur=[1/2, 1/4], amp=0.5)

Clock.bpm = 160
