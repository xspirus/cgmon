#!/usr/bin/python

import fileinput

max = 2000
threshold = 100
sum = 0
anelastic = []
elastic = []

for line in fileinput.input():
    line = line.rstrip()
    words = line.split(":")
    app = words[1]
    value = int(words[3])
    sum += value
    if (value > threshold) :
        anelastic.append((app, value))
    else :
        elastic.append((app, value))

if sum > max :
    score = -1.0
else :
    score = 1.0

toprint = 'score{sep}{val}'
toprint = toprint.format(sep=':', val=score)
print toprint

if (sum < max) :
    rest = max - sum
else :
    rest = 0
try :
    give = rest / len(elastic)
except ZeroDivisionError :
    give = 0

for tuple in anelastic :
    toprint = 'set_limit{sep}{name}{sep}cpu.shares{sep}{val}'
    toprint = toprint.format(sep=':', name=tuple[0], val=tuple[1])
    print toprint
for tuple in elastic :
    toprint = 'set_limit{sep}{name}{sep}cpu.shares{sep}{val}'
    toprint = toprint.format(sep=':', name=tuple[0], val=(tuple[1] + give))
    print toprint
