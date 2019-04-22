p2 >> bass(var([0, 3], 8), dur=1/4)
p1 >> pluck(dur=1/4, amp=[1, 1/2, 1/2, 1, 0, 1,
                          0, 1, 1/2, 1/2, 1, 0, 1, 1/2, 1/4, 1])

Group(p1, p2).amplify = var([1, 0], 4)

d2 >> play("x-oo*--*", dur=1/3)

ba >> bass([0], dur=1/3, amp=1)

p1 >> pluck([0, 1, 2, 3, 4, 5, 6, 7], dur=1/4).every(4, "reverse")

p1 >> pluck([0, 1, 2, 3, 4, 5, 6, 7], dur=1 /
            2).every(PRand([2, 4, 8]), "reverse")
d1 >> play("x-o-").every(6, "stutter", cycle=8)

h1 >> play("x-o-").every(4, "trim", 3)

p1 >> pluck([0, 1, 2, 3], oct=[4, 5, 6, 7], dur=1/3).every(2, "oct.trim", 3)
