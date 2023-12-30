# read a four-part MusicXML file and check if detects  parallel perfect fifths

import sys
import music21 as m21
import os

def read_file(filename):
    # read a MusicXML file    
    # return a music21 stream object    
    s = m21.converter.parse(filename)
    return s

def get_mistakes(s):
    # check if there are parallel perfect fifths between the parts
    parts = s.parts
    mistakes = []
    for i in range(0, len(parts)):
        for j in range(i+1, len(parts)):
#            mistakes += check_parallel_fifths(parts[i], parts[j])
            mistakes += check_parallel_octaves(parts[i], parts[j])
            mistakes += check_parallel_unisons(parts[i], parts[j])

#            mistakes += check_crossing_voices(parts[i], parts[j])
#            mistakes += check_voice_overlap(parts[i], parts[j])
#            mistakes += all_four_voice_leaping_in_same_direction(parts[i], parts[j])
    return mistakes

def check_parallel_fifths(part1, part2):
    # check if there are parallel perfect fifths between two parts
    # return a list of parallel perfect fifths
    mistakes = []

    for i in range(0, len(part1.pitches)-1):
        # if part1.pitches[i].isChord:
        #     console.log("chord")
        #     n1 = part1.notes[i].pitches[0]
        # else:

        n1 = part1.pitches[i]
        # if part1.notes[i+1].isChord:
        #     n2 = part1.notes[i+1].pitches[0]
        # else:
        n2 = part1.pitches[i+1]
        for j in range(0, len(part2.pitches)-1):
            # if part2.notes[j].isChord:
            #     n3 = part2.notes[j].pitches[0]
            # else:
            n3 = part2.pitches[j]
            # if part2.notes[j+1].isChord:
            #     n4 = part2.notes[j+1].pitches[0]
            # else:
            n4 = part2.pitches[j+1]
            #print measure number of n1 pitch

            # check if there are parallel perfect fifths            
            if m21.interval.Interval(n1, n2).name == "P5" and m21.interval.Interval(n3, n4).name == "P5":
                mistakes.append([n1.name, n2.name, n3.name, n4.name])
            if m21.interval.Interval(n1, n3).name == "P5" and m21.interval.Interval(n2, n4).name == "P5":
                mistakes.append([n1.name, n3.name, n2.name, n4.name])

    return mistakes

def check_parallel_octaves(part1, part2):
    # check if there are parallel perfect octaves between two parts
    # return a list of parallel perfect octaves
    mistakes = []

    for i in range(0, len(part1.pitches)-1):
        n1 = part1.pitches[i]
        n2 = part1.pitches[i+1]
        for j in range(0, len(part2.pitches)-1):
            n3 = part2.pitches[j]
            n4 = part2.pitches[j+1]
            #print measure number of n1 pitch

            # check if there are parallel perfect octaves            
            if m21.interval.Interval(n1, n2).name == "P8" and m21.interval.Interval(n3, n4).name == "P8":
                mistakes.append([n1.name, n2.name, n3.name, n4.name])
            if m21.interval.Interval(n1, n3).name == "P8" and m21.interval.Interval(n2, n4).name == "P8":
                mistakes.append([n1.name, n3.name, n2.name, n4.name])

    return mistakes

def check_parallel_unisons(part1, part2):
    # check if there are parallel perfect unisons between two parts
    # return a list of parallel perfect unisons
    mistakes = []

    for i in range(0, len(part1.pitches)-1):
        n1 = part1.pitches[i]
        n2 = part1.pitches[i+1]
        for j in range(0, len(part2.pitches)-1):
            n3 = part2.pitches[j]
            n4 = part2.pitches[j+1]
            #print measure number of n1 pitch

            # check if there are parallel perfect unisons            
            if m21.interval.Interval(n1, n2).name == "P1" and m21.interval.Interval(n3, n4).name == "P1":
                mistakes.append([n1.name, n2.name, n3.name, n4.name])
            if m21.interval.Interval(n1, n3).name == "P1" and m21.interval.Interval(n2, n4).name == "P1":
                mistakes.append([n1.name, n3.name, n2.name, n4.name])

    return mistakes

def check_crossing_voices(part1, part2):
    # check if there are crossing voices between two parts
    # return a list of crossing voices
    mistakes = []

    for i in range(0, len(part1.pitches)-1):
        n1 = part1.pitches[i]
        n2 = part1.pitches[i+1]
        for j in range(0, len(part2.pitches)-1):
            n3 = part2.pitches[j]
            n4 = part2.pitches[j+1]
            #print measure number of n1 pitch

            # check if there are crossing voices            
            if n1 > n2 and n3 < n4:
                mistakes.append([n1.name, n2.name, n3.name, n4.name])
            if n1 < n2 and n3 > n4:
                mistakes.append([n1.name, n2.name, n3.name, n4.name])

    return mistakes

def check_voice_overlap(part1, part2):
    # check if there are voice overlap between two parts
    # return a list of voice overlap
    mistakes = []

    for i in range(0, len(part1.pitches)-1):
        n1 = part1.pitches[i]
        n2 = part1.pitches[i+1]
        for j in range(0, len(part2.pitches)-1):
            n3 = part2.pitches[j]
            n4 = part2.pitches[j+1]
            #print measure number of n1 pitch

            # check if there are voice overlap            
            if n1 > n3 and n2 < n4:
                mistakes.append([n1.name, n2.name, n3.name, n4.name])
            if n1 < n3 and n2 > n4:
                mistakes.append([n1.name, n2.name, n3.name, n4.name])

    return mistakes

def all_four_voice_leaping_in_same_direction(part1, part2):
    # check if all four voices are leaping in the same direction
    # return a list of four voice leaping in the same direction
    mistakes = []

    for i in range(0, len(part1.pitches)-1):
        n1 = part1.pitches[i]
        n2 = part1.pitches[i+1]
        for j in range(0, len(part2.pitches)-1):
            n3 = part2.pitches[j]
            n4 = part2.pitches[j+1]
            #print measure number of n1 pitch

            # check if all four voices are leaping in the same direction            
            if n1 > n2 and n2 > n3 and n3 > n4:
                mistakes.append([n1.name, n2.name, n3.name, n4.name])
            if n1 < n2 and n2 < n3 and n3 < n4:
                mistakes.append([n1.name, n2.name, n3.name, n4.name])

    return mistakes

# check hidden fifths and hidden octaves
# check parallel fifths and octaves in the outer voices
# check for voice crossing
# check for voice overlap


def main():
    # read a MusicXML file
    # check if there are parallel perfect fifths in the music
    # return a list of parallel perfect fifths
    # print the list of parallel perfect fifths
    filename = sys.argv[1]
    s = read_file(filename)
#    parallel_fifths = check_parallel_fifths(s)
#    print(parallel_fifths)

    mistakes = get_mistakes(s)
    print(mistakes)



if __name__ == "__main__":
    main()


                            
