from time import sleep
from random import randint, choice
from collections import deque
from os import system

#for a in range(65, 50000, 100):
#    print("|".join(f"{i}" + chr(i) for i in range(a, a+100)))
#a = 14000
#print([chr(i) for i in range(a, a+50000)], end="\r")

chars = ["□", chr(randint(14000, 50000)), "○", " "]
def stream():
    # 0: fade in chars, 1: full, 2: fade out, 3: space
    state = 0
    while True:
        state = (state + choice([0 for _ in range(speed)] + [1])) % 4
        yield choice(chars[state])

screen = deque(maxlen=30)
fps = 30
speed = 10
space = 4
rows = 15
line = [stream() for _ in range(rows)]
# 10 sec
for _ in range(fps * 10):
    screen.appendleft((" " * space).join(next(strea) for strea in line))
    system("clear")
    for row in screen:
        print(row)
    sleep(1/fps)
