p1 >> bass(P[2, 5, 6].stretch([6, 2]))

p1 >> pluck(2, dur=PDur([3, 5], 5)) + [(2, 1), (7, 1)]

f4 >> zap(2, dur=1/3) + [(3, 4), 2, 2, 2]
d1 >> play('xVxx', dur=1/3)

d2 >> play('.qw.qk.', dur=1/2)

d3 >> play('-*.*', dur=1/2)

d5 >> play('I dont think so.', dur=1/3) + ([3, 3], [2, 5], 2, 4)

d9 >> play('feel ee good', dur=1/3)

d6 >> quin(oct=3, dur=PDur([1, 3], 5), amp=2)

d4 >> play('tw.ssf', dur=1/2)

d5 >> play('wqrf')

q1 >> pasha(3, dur=1/2) + [(2, 7, 4), (1, 5), (1, 6, 1)]

print(SynthDefs)

g1 >> dab(oct=5, dur=PDur([3, 4], 5), amp=1) + [3, 1]

Clock.bpm = 160
