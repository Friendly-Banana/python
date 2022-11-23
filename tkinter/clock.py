import tkinter as tk
import time

root = tk.Tk()
root.title("Clock")
run = True

def update_clock():     
    current_time = time.strftime("%H:%M:%S")
    time_lbl.config(text=current_time)
    if run:
        time_lbl.after(1000, update_clock) 
    
current_time = time.strftime("%H:%M:%S")
time_lbl = tk.Label(root, text=current_time)
time_lbl.pack()
update_clock()

root.mainloop()