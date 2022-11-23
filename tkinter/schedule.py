#!/usr/bin/python3
import time
import tkinter as tk


class Event:
    def __init__(self, name: str, interval: int, loop: bool, method2run: str):
        self.name = name
        self.interval = interval
        self.loop = loop
        self.method = method2run
        self.start = time.time()

    def done(self):
        self.restTime = self.interval - round(time.time() - self.start)
        if self.restTime <= 0:
            self.run()
            if self.loop:
                self.start = time.time()
            return True

    def info(self):
        return (
            self.name,
            f"{self.interval} s",
            "True" if self.loop else "False",
            self.method,
            f"{self.restTime} s",
        )

    def run(self):
        exec(self.method)


def blink():
    root.config(bg="red")
    time.sleep(1)
    root.config(bg="white")


def new(*args):
    if len(args) == 4:
        events.append(Event(*args))
        return

    def ev():
        events.append(
            Event(name.get(), int(interval.get()), loop_var.get(), method.get())
        )
        window.destroy()

    window = tk.Toplevel()
    window.title("Create New Event")
    tk.Label(window, text="Event name").grid(row=0, column=0)
    name = tk.Entry(window)
    name.grid(row=0, column=1)
    tk.Label(window, text="Interval in s").grid(row=1, column=0)
    interval = tk.Spinbox(window, from_=1, to=6000)
    interval.grid(row=1, column=1)
    loop_var = tk.IntVar()
    tk.Checkbutton(window, text="Loop event", variable=loop_var).grid(row=2, column=1)
    tk.Label(window, text="Method to run").grid(row=3, column=0)
    method = tk.Entry(window)
    method.grid(row=3, column=1)
    tk.Button(window, text="Ok", command=ev).grid(row=4, column=1)
    window.mainloop()


def show():
    for row, event in enumerate(events[:]):
        if event.done():  # event has happened
            events.remove(event)
        else:
            print(row)
            tk.Button(root, text="\t".join(event.info())).grid(row=row + 2)
    root.after(1000, show)


events = []

root = tk.Tk()
root.title("Schedule")
tk.Button(root, text="New Event", command=new).grid()
tk.Label(
    root,
    text="    ".join(
        ["Event name", "Interval", "Loop", "Method", "Time till execution"]
    ),
).grid(row=1)

new("Blink", 5, True, "blink()")
show()
root.mainloop()
