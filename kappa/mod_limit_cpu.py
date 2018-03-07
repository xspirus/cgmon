#!/usr/bin/python

import fileinput
import subprocess

for line in fileinput.input() :
    dir = '/sys/fs/cgroup/cpu'
    line = line.rstrip()
    words = line.split(":")
    if ( words[0] == 'create' ) :
        dir += '/' + words[1]
        dir += '/' + words[3]
        subprocess.call(["mkdir", "-pv", dir])
    elif ( words[0] == 'remove' ) :
        dir += '/' + words[1]
        dir += '/' + words[3]
        subprocess.call(["rmdir", "-v", dir])
    elif ( words[0] == 'add' ) :
        dir += '/' + words[1]
        dir += '/' + words[3]
        procs = dir + '/cgroup.procs'
        file = open(procs, "a")
        file.write(words[4] + '\n')
        file.close()
        tasks = dir + '/tasks'
        file = open(tasks, "a")
        file.write(words[4] + '\n')
        file.close()
    elif ( words[0] == 'set_limit' ) :
        dir += '/' + words[1]
        dir += '/' + words[3]
        cpu = dir + '/cpu.shares'
        file = open(cpu, "w")
        file.write(words[5])
        file.close()
    else :
        print "Error motherfucker"

