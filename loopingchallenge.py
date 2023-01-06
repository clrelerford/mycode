#!/usr/bin/env python3

#"Spooky Looping Exercise"

counter = 0

with open("dracula.txt", "r") as foo:
    for line in foo:
        if "vampire" in line.lower():
            print(line)
            counter += 1
            fang.write(line)

print(counter)

