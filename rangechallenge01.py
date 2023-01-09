#!/usr/bin/env python3

#Range Challenge Extra Credit 01

start_num = input("Enter the number of bottles to start with: ")

for num in range(int(start_num), 0, -1):
    if num > 1:
        print(f"{num} bottles of beer on the wall, {num} bottles of beer.")
        print(f"Take one down, pass it around, {num-1} bottles of beer on the wall.")
    elif num == 1:
        print("1 bottle of beer on the wall, 1 bottle of beer.")
        print("Take one down, pass it around, no more bottles of beer on the wall.")
    else:
        print("No more bottles of beer on the wall, no more bottles of beer.")
        print("Go to the store and buy some more, 99 bottles of beer on the wall.")

