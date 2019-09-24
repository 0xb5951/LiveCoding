b1 >> play("V [VV] ")
t1 >> play('  : ')+(1, [4, 1])
p1 >> play(':', dur=PDur(3, 5))

p2 >> play('O', dur=4)

x1 >> pluck([2, 2, 3, 6]).every(3, "offadd", 4).every(2, "stutter", 4, dur=3, pan=[-1,1], oct=5).every(4, "reverse")

bs >> bass([2, 4], amp=1).every(2, "reverse")
bs.stop()

d1 >> play("b", dur=PDur(3,8), amp=0.6).every([2, 6], "reverse")

bs >> dbass(PRange(5), dur=PDur(4, 4)).every(2, "reverse")

j2 >> bell(PRand(8, 16)[:8], dur=PDur(2, 4), amp=0.6)

p4 >> pads([3, 4, 6,(3,5,7)], dur=PDur(3, 4), amp=0.8).every(2, "reverse")

p4.stop()

