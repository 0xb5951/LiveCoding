b1 >> bass([0, 0, 10, 14, 15], dur=1/4)

d1 >> play('oxxo')

hh >> play('----(-*)')

p2 >> pluck(dur=1/4, amp=[1, 1/2, 1/2, 1, 0, 1, 0, 1, 1/2, 1/2, 1, 0, 1, 1/2, 1/4, 1], amplify=var([1,0],[6,2]))

p1 >> pluck([0, 2, 4, 6, 7], scale=Scale.minor)
Scale.default = "dorian"

p1 >> pluck([0, 1, 2, 3], dur=1/2, sus=10)
p1 >> pluck([0, 2, 4, 6], dur=1/2, sus=10)

p1 >> pluck(oct=[4, 5, 6])
p1 >> pluck(oct=[5, 6, 7])
p1 >> pluck(oct=[6, 7, 8])
p1 >> pluck(oct=[7, 8, 9])

p2 >> pluck(dur=4, slide=0, slidedelay=0.5)
