# 短音のド
p1 >> pluck()
# stopメソッドで止められる
p1 >> pluck().stop()

print(SynthDefs)

p1 >> pluck([0, 2, 4], dur=[1, 1/2, 1/2], amp=0.75)

p1 >> pluck([0, 1, 2, 3], dur=2) + [0, 0, 4]

p1 >> pluck([0, 1, 2, 3], dur=2) + (0, 2, 4)

d1 >> play("x---")

d1 >> play("(x-)(-x)o-")

d1 >> play("x-o[---]", dur=1)

d1 >> play("x-o{-=*}", dur=1/4)

d1 >> play("(x[--])xo{-[--][-x]}", amp=2)

p1 >> pluck(dur=1/4, pan=linvar([-1, 1], 2))
p2 >> pluck(var([0, 3, 0, 4], 8), dur=[1, 1/4, 1/4, 1/2]) + (0, 2, 4)
