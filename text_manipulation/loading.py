import os
from time import sleep
from math import floor, ceil

loading = [ "/—\|",
    ".oO@*",
    "←↖↑↗→↘↓↙",
    "→⬊↓⬋←⬉↑⬈",
    "▁▂▃▄▅▆▇█",
    "▏▎▍▌▋▊▉█",
    "▖▘▝▗",
    "┤┘┴└├┌┬┐",
    "◢◣◤◥",
    "◰◳◲◱",
    "◴◷◶◵",
    "◐◓◑◒", 
    "⣾⣽⣻⢿⡿⣟⣯⣷"[::-1], 
    "⠁⠂⠄⡀⢀⠠⠐⠈"]

    
def main():
    clear_cmd = "clear" if os.name == "posix" else "cls"
    gen = individual(40)
    for frame in gen:
        os.system(clear_cmd)
        print(frame)
        sleep(0.1)
    print("Finished")

def individual(frames):
     for i in range(frames):
         yield "\n".join(ld[i % len(ld)] for ld in loading)
     
# rate: frames for full cycle
def synchronized(frames, rate = 8):
    for i in range(frames):
        s = ""
        for an in loading:
            ind = int(i // (rate / len(an)))
            char = an[ind % len(an)]
            s += char + "\n" * 2
        yield s
        
def increase(frames, width=8):
    bar = " ▏▎▍▌▋▊▉█"
    for i in range(1, frames+1):
        t = i / frames * width
        yield f"{bar[-1] * floor(t)}{bar[round((t - floor(t)) *8)]}"

# ❌✔✅,  #, □■, ○●, 🧱🧨🌲, 🚧🏗️🧱
def darken(frames, chars="░▒▓", width=16):
    for i in range(1, frames+1):
        t = i / frames * width
        s = chars[-1] * floor(t)
        if round(t - floor(t)) != 0:
            s += chars[1]
        while len(s) < width:
            s += chars[0]
        yield s
    
if __name__ == "__main__":
    main()