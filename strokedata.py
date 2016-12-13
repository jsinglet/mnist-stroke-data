#!/usr/bin/env python
import numpy as np
import json
"""strokedata.py: Create strokedata from infered MNIST strokes"""

"""
Date       : Sat Nov  5 22:05:58 EDT 2016
Author     : John L. Singleton
Email      : jls@cs.ucf.edu
"""

symbols_to_convert = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

# read the file
index = open("sequences/trainlabels.txt")
data  = index.read()
index.close()

lines = data.splitlines()

counter = {}

for s in symbols_to_convert:
    counter[s] = 0

def convert_sample(idx, sample):
    num = counter[sample]
    counter[sample] = num + 1

    outfile = "strokes/sample-{0}-{1}.json".format(sample, num)

    # load data
    f = open("sequences/trainimg-{0}-inputdata.txt".format(idx))
    data = f.read()
    lines = data.splitlines()

    # each stroke is an array of tuples.
    strokes = []

    current_stroke = []

    cx = 0
    cy = 0
    init = True
    for line in lines:
        s = line.split(" ")
        dx = int(s[0])
        dy = int(s[1])
        eos = s[2] == "1"
        eod = s[3] == "1"


        # starting
        if init == True:
            cx = dx
            cy = dy
            init = False
        else:
          # figure out newpoints
          cx = cx + dx
          cy = cy + dy

        # create the point
        point = {"x": cx, "y": cy}

        current_stroke.append(point)

        if eos:
           strokes.append(current_stroke)
           current_stroke = []
    print "Exporting {0} strokes for symbol {1} to {2}".format(len(strokes), sample,  outfile)
    # write it as json
    with open(outfile, 'w') as out:
        json.dump(strokes, out)



for idx in range(0, len(lines)):
    sample = lines[idx]

    if sample in symbols_to_convert:
       convert_sample(idx, sample)

