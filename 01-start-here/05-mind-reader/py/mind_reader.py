#!/usr/bin/env python3
import random

target_number = random.randint(1, 10)

print("🔮 Can you guess the magic number?")
answer = -1
while answer != target_number:
    answer = int(input("> "))
    if(answer == target_number):
        print("🔮 You got it!")
    elif(answer > target_number):
        print("🔮 Too high!")
    else:
        print("🔮 Too low!")
