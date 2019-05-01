ch = var([2, 5], [4, 7])

p1 >> pluck(ch, dur=var([1/2, 1/4], [1, 2]), pan=-2)

bd >> play("X ", dur=var([1/2, 1/4], 2), bits=[0, 3])

tm >> play("as", dur=1/2) + [[2, 1], [3, 2]]

hh >> play("( H)  ( H)", dur=1/2)

ma >> play("Im so sick", rate=var(1/2, 1/4)) + [2, 4]

ba >> dbass(ch, dur=([1/2,  1/4]), amp=1.2, rate=var(1/2, 1/4, 1/2), pan=2)

be >> bell(ch, dur=([1/2, 1/4], [4, 1]), sus=0.5, pan=(1, -1))

print(SynthDefs)

Clock.bpm = 130

d1 >> play("x[::][xx]=", crush=8).every(4, "amen").often("stutter")
