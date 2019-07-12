ch = var([-1, 1], [3, 1])

bd >> play("X", dur=var([1/2, 1/4], [2, 1]))

tm >> play("x x x ", dur=([1/2, 1/4], (1, 3)), bits=[0, 3], rate=var([1, 1/2]))

hh >> play(" -I-", bits=[0, 0, 0, 0], sus=0.1)

cp >> play("x( H )x( H )", pan=(-1, 1))

bs >> bass(ch, dur=[1/2, 1/4], sus=0.5, bits=[1, 2])

be >> bell(ch, dur=([1/2, 1/4], 2), amp=0.4)
