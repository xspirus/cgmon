#!/usr/bin/python

import fileinput

max = 2000
sum = 0
nvlist = []

for line in fileinput.input():
    line = line.rstrip()
    words = line.split(":")
    app = words[1]
    value = int(words[3])
    sum += value
    nvlist.append((app, value))

if sum > max :
    score = -1.0
else :
    score = 1.0

toprint = 'score{sep}{val}'
toprint = toprint.format(sep=':', val=score)
print toprint

for tuple in nvlist :
    toprint = 'set_limit{sep}{name}{sep}cpu.shares{sep}{val}'
    toprint = toprint.format(sep=':', name=tuple[0], val=tuple[1])
    print toprint
