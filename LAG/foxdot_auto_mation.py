import numpy as np
import time
import random
import json
​
time_interval = 1
​
def RN(N):
    return np.random.randint(N)
​
def RN1(N):
    return np.random.randint(1, N)
​
def melody():
    contents = [
        "m1 >> pluck([(0,4,3,2)], oct=5, dur=1/2, echo=0.75, sus=1, room=1, amp=0.7, chop=4)",
        "m1 >> pluck(P[0, 3, 0, 4].stutter(32), dur=1/4) + (0, 2, 4)",
        "m1 >> pluck(var([0, 3, 0, 4], 8), dur=[1,1/4,1/4,1/2]) + (0, 2, 4)",
        "m1 >> quin(var([0, 3, 0, 4, 0, 2, 0, 3], 8), dur=[1,1/4,1/4,1/2]) + (0, 2, 4)",
        "m1 >> sitar(P[0,2,3,7].arp([0, -2]), dur=1/4)",
        "m1 >> pasha(P[0,2,2,7].arp([0, -2]), dur=1/4)",
        "m1 >> pasha( P[(0,2,5,7),(0,2,2,7),(0,5,5,7),(0,5,7,7)], dur=[1/4, 1/4, 1/4,rest(1), 1/4, 1/4,rest(2)])",
        "m1 >> pasha([(0,2,5,7),(0,2,5,7),(0,2,5,7),(0,2,5,7),(0,5,5,7),(0,5,5,7),(0,5,5,7),(0,5,5,7)], dur=[1/4, 1/4, 1/4, 1/4, rest(4)])"
    ]
    N = len(contents)
    return contents[RN(N)]
​
def drum():
    contents = [
        "d1 >> play('(X[--])Xo{-[--][-x]}',amp=2)",
        "d1 >> play('(X[--])Xu{-[--][-x]}',amp=2)",
        "d1 >> play('(X[--])Xa{-[--][-x]}',amp=2)",
        "d1 >> play('X-X-[xx]X -X-X-xX -',amp=2)",
        "d1 >> play('X-X-[xx]X -X-X-xX u',amp=2)",
        "d1 >> play('xX oX X-',amp=2)",
        "d1 >> play('xX aX X-',amp=2)",
        "d1 >> play('xX oX X-xX aX X=',amp=2)",
        "d1 >> play('X[--]X[--]X[--]X[--]X[--]X[--]X[--] u',amp=2)",
        "d1 >> play('X[--]X[--]X[--]X[--]X[--]X[--]X[--] =',amp=2)",
        "d1 >> play('X X X X ',amp=2)",
        "d1 >> play('X X X X X X X-X-',amp=2)",
        "d1 >> play('X X X X X X X[--]X-',amp=2)",
        "d1 >> play('X X xXxXX X X-X-',amp=2)"
    ]
    N = len(contents)
    return contents[RN(N)]
​
def percussion():
    contents = [
        "c1 >> play('@', dur=1/4, sample=P[:8].rotate([0,1,3]), rate=4,)",
        "c1 >> play('@', dur=1/4, sample=P[:8].rotate([0,1,3]), rate=1,)",
        "c1 >> play('@', dur=1/2, sample=P[:8].rotate([0,1,3]), rate=2.5, )",
        "c1 >> play('@', dur=P[1/4,1/2,1/4], sample=P[:8].rotate([0,1,3]), rate=2.5, )",
        "c1 >> play('@', dur=P[1/4,1/2,1/4], sample=P[:8].rotate([0,1,3]), rate=3.5, )",
        "c1 >> play('x', dur=P[1/4,1/2,1/4], sample=P[:8].rotate([0,1,3]), rate=4,)",
        "c1 >> play('x', dur=P[1/4,1/2,1/4], sample=P[:8].rotate([0,1,3]), rate=8,amp=1.5)",
        "c1 >> play('@', dur=P[1/4,1/2,1/4,1/4,1/4,1/2], sample=P[:8].rotate([0,1,3]), rate=2.5, )",
        "c1 >> play('@', dur=P[1/4,1/2,1/4,1/4,1/4,1/2], sample=P[:8].rotate([0,1,3]), rate=4.5, )",
        "c1 >> play('o', dur=P[1/4,1/2,1/4,1/4,1/4,1/2], sample=P[:8].rotate([0,1,3]), rate=2.5, )",
        "c1 >> play('k', dur=P[1/4,1/2,1/4,1/4,1/4,1/2], sample=P[:8].rotate([0,1,3]), rate=1.5, )",
        "c1 >> play('x', dur=P[1/4,1/2,1/4,1/4,1/4,1/2], sample=P[:8].rotate([0,1,3]), rate=2, )",
        "c1 >> play('k', dur=P[1/2,1/4,1/4,1/4,1/2,1/4], sample=P[:8].rotate([0,1,3]), rate=1.5, )",
        "c1 >> play('q', dur=P[1/2,1/4,1/4,1/4,1/2,1/4], sample=P[:8].rotate([0,1,3]), rate=1.5, )",
        "c1 >> play('x', dur=P[1/2,1/4,1/4,1/4,1/2,1/4], sample=P[:8].rotate([0,1,3]), rate=2, )"
    ]
    N = len(contents)
    return contents[RN(N)]
​
def percussion_prev():
    contents = [
        "play('x-o{-=*}', dur=1/4)",
        "play('(x[--])xo{-[--][-x]}', dur=1/2)",
        "play('x-o-', dur=1/2).every(6, 'stutter', cycle=8)",
        "play('x-oo*--*', dur=1/4)",
        "play('--xo-*(ox, oo)x', dur=1/4)",
        "play('-*.*', dur=1/2)",
        "play('I dont think so.', dur=1/4) + ([3, 3], [2, 5], 2, 4)",
        "play('wqrf')",
        "play('(x )(-[-x])')",
        "play('Xvs[+x]', dur=1/2)",
        "play('x( H )x( H )', pan=(-1, 1))",
        "play(' -I-', bits=[0, 0, 0, 0], sus=0.1)",
        "play('x x x ', dur=([1/2, 1/4], (1, 3)), bits=[0, 3], rate=var([1, 1/2]))",
        "play('X ', dur=var([1/2, 1/4], 2), bits=[0, 3])",
        "play('x[::][xx]=', crush=8).often('stutter')",
        "play('@', dur=1/4, sample=P[:8].rotate([0,1,3]), rate=4, pan=-0.5)",
        "play('<  * ><[--]>')"
    ]
    N = len(contents)
    return contents[RN(N)]
​
def ura():
    contents = [
        "u1 >> creep(oct=9, dur=1/2,chop=2 , amp=[1, 1/2, 1/2, 1, 0, 1, 0, 1, 1/2, 1/2, 1, 0, 1, 1/2, 1/4, 1])",
        "u1 >> creep((P[1, 3, 2, 0].sort()), oct=9, dur=1/2,chop=2 , amp=[1, 1/2, 1/2, 1, 0, 1, 0, 1, 1/2, 1/2, 1, 0, 1, 1/2, 1/4, 1], pan=linvar([-1,1],2))",
        "u1 >> orient(oct=9, dur=1,chop=4 , amp=0.8)",
        "u1 >> orient(oct=9, dur=1,chop=4 , amp=0.8)"
    ]
    N = len(contents)
    return contents[RN(N)]
​
def phrase_maker01():
    out = []
    bass = []
    dur = []
    for _ in range(4):
        if RN(4) == 3:
            n1 = RN(8)
            bass.append(n1)
            out.append(n1)
            dur.append(0.5)
            out.append(RN(8))
            dur.append(0.5)
        else:
            n1 = RN(8)
            bass.append(n1)
            out.append(n1)
            dur.append(1)
    return out, dur, bass
​
def phrase_generate():
    out = []
    for _ in range(4):
        out.append(RN(8))
    return out
​
def rDur():
    types = [1, 1/2, 1/4]
    N = len(types)
    return types[RN(N)]
​
def MelodySelect():
    types = ['varsaw','dirt','quin','pluck','blip','orient','nylon','swell','sitar','star','pasha','pads']
    N = len(types)
    return types[RN(N)]
​
def BassSelect():
    types = ['dab','bass','dirt','dub','jbass','sawbass','dbass']
    N = len(types)
    return types[RN(N)]
​
def UraSelect():
    types = ['growl','bell','orient','zap','marimba','karp','arpy','sitar']
    N = len(types)
    return types[RN(N)]
​
def bpm(num_people=5):
    if num_people <= 5:
        return 120
    elif num_people > 20:
        return 140
    else:
        return 120 + int(num_people / 5) * 10
​
def create_FoxDot_2m():
    """
    基本: メロディ1, ベース1, 裏音1, パーカッション1
    +a : pads1, 裏音+1
    114 ~ 120 ~ 140
    """
    #code = 'Clock.bpm = 120\n'
    code = 'Clock.bpm = ' + str(bpm()) +'\n'
    num_melody = 1
    num_bass = 0
    num_ura = 1

    flag_sample = False

    phrase = phrase_generate()

    code += 'phrase = P' + str(phrase) + '\n'

    for i in range(num_melody):
        if flag_sample:
            code += melody() + '\n'
            continue
        if i == 0:
            r = 0
        else:
            r = 3 + RN(2)
        code += 'p'+str(i)+' >> ' + MelodySelect() + '(phrase+['+str(r)+'], dur=['+str(rDur())+'])\n'

    for i in range(num_bass):
        if flag_sample:
            continue
        if i == 0:
            r = 0
        else:
            r = 3 + RN(2)
        code += 'b'+str(i)+' >> ' + BassSelect() +'(phrase+['+str(r)+'], dur=['+str(rDur())+'])\n'

    for i in range(num_ura):
        if flag_sample:
            code += ura() + '\n'
            continue
        r = 3 + RN(2)
        code += 'u'+str(i)+' >> ' + UraSelect() + '(phrase+['+str(r)+'], dur=['+str(rDur())+'])\n'

    # drum
    code += drum() + '\n'

    # pad
    code += 'p5 >> pads([' +str(RN(8)) +'], sus=2, dur=[1, rest(' +str(8+RN(8))+ ')])\n'
​
    # パーカッション
    code += percussion() + '\n'

    return code

def read_and_change():
    path = './data/foxdot_output.txt'
    f = open(path)
    data = f.read()
    f.close()

    lines = data.split('\n')

    outstr = ''

    flag_change = False

    for line in lines:
        if line == '':
            continue

        # phraseを変化
        if 'phrase' in line and flag_change == False:
            contents = line[line.find('[')+1:line.find(']')]
            words = contents.split(',')
            notes = []
            for word in words:
                notes.append(int(word))
            notes[RN(4)] += int(2+RN(2))
            outstr += 'phrase = P'+str(notes)+'\n'
            flag_change = True
        else:
            outstr += line +'\n'

    f = open(path, 'w')
    f.write(outstr)
    f.close()
​
def output_foxdot(code):
    f = open('./data/foxdot_output.txt','w')
    f.write(code)
    f.close()
​
def random_num(min_limit = 0, max_limit = 1):
    if max_limit <= 1:
        res = random.random()
    else:
        res = random.randint(min_limit, max_limit)
    return res
​
def create_hydra_code():
    with open('hydra_source.json', 'r') as f:
        source_data = json.load(f)
    source_num = len(source_data)
    select_point = str('s' + str(random_num(1, source_num)))
    using_source = source_data[select_point]
    return using_source
​
def output_hydra(code):
    f = open('./data/hydra_output.txt', 'w')
    f.write(code)
    f.close()
​
​
def main():
    while(True):
        output_foxdot(create_FoxDot_2m())
        output_hydra(create_hydra_code())
        for j in range(12):
            time.sleep(10)
            read_and_change()
            output_hydra(create_hydra_code())

if __name__ == '__main__':
    main()
