b1 >> play('V (BV)').every(4, "reverse")

b2 >> play('([LL]{eh})', dur=PDur(3, 6), amp=0.4)

t1 >> play('  : ')+(1, [4, 1])

t1.stop()

p1 >> play('s', dur=PDur(3, 5))

x1 >> creep([2, 4, 6]).every(2, "stutter", 4, dur=1/2, oct=[2, 5]).every(3, "reverse")

x1.stop()

bs >> dbass([2, 4, 6], dur=PDur(4, 4)).every(3, "reverse")

d1 >> play("b", dur=PDur(4,5), amp=0.6).every(3, "reverse")

b1 >> dub(-2 ,dur=PDur(3, 4), amp=0.6)




p4 >> pads([1, (3, 5), (3, 6)], dur=PDur(5, 6), amp=0.8).every(5, "reverse")
p4.stop()


print(SynthDefs)
