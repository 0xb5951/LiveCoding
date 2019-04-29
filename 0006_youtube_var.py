var.chords = var([0, 4, 5, 3], 4)

p1 >> pluck(var.chords + [0, 2, 4], dur=PDur([3, 5, 7], 8))
b1 >> bass(var.chords, dur=1/2)

Clock.bpm = 120
