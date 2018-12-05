#!/usr/bin/python
#
# Day 01, part 2

def main ():
    f = open("input.txt", "r")
    lines = f.readlines()

    sum = 0
    frequencies = set([sum])
    while 1:
        for line in lines:
            sum += int(line)
            if sum in frequencies:
                print("found=", sum)
                return sum

            frequencies.add(sum)
            # print("frequencies = ", frequencies)

if __name__== "__main__":
  main()