from tkinter import *
from tkinter.ttk import *

root = Tk()
root.config(bg="RoyalBlue4")
root.title("Progress")


def step(bar):
    if bar["value"] >= bar["maximum"]:
        bar["value"] = 0
    else:
        bar["value"] += 10


def auto(bar, fills=1):
    steps = bar["maximum"] + 1
    for i in range(0, steps):
        for _ in range(0, fills * 50):
            bar["value"] = i % (steps)
            root.update_idletasks()


prog_det = Progressbar(root, orient=HORIZONTAL, length=100, mode="indeterminate")
prog_det.pack()
but = Button(root, text="Start", command=prog_det.start)
but.pack()

prog_in = Progressbar(
    root, orient=HORIZONTAL, maximum=100, length=100, mode="determinate"
)
prog_in.pack()
but = Button(root, text="Go On", command=lambda: step(prog_in))
but.pack()

but = Button(root, text="Auto Progress", command=lambda: auto(prog_in))
but.pack()

root.mainloop()
