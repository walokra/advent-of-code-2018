#!/usr/bin/python
#
# Day 01, part 1

def main ():
    f = open("input.txt", "r")
    lines = f.readlines()
    
    sum = 0
    for line in lines:
        sum += int(line)

    print(sum)

if __name__== "__main__":
  main()