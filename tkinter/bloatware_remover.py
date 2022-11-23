import subprocess
from tkinter import *
from tkinter.ttk import *
import tkinter.messagebox as mb


def uninstall(package):
    return print(package)
    output = subprocess.run(
        f"adb pm uninstall --user 0 {package}".split(), capture_output=True, text=True
    )
    show_packages()
    if output.returncode == 0:
        history.insert(INSERT, output.stdout)
    else:
        mb.showerror("Error", "An error ocurred:\n" + output.stderr)
        history.insert(INSERT, output.stderr, ("error"))


def show_packages():
    # clean up
    for package in packages:
        package.destroy()
    packages.clear()
    # get packages
    adb = subprocess.run(
        "adb shell pm list packages".split(), capture_output=True, text=True
    )
    if adb.returncode != 0:
        mb.showerror("Error", adb.stderr)
        history.insert(INSERT, adb.stderr, ("error"))
        return
    packs = adb.stdout.strip().split("\n")
    for pack in packs:
        pack = pack.replace("package:", "")
        package = Button(frame, text=pack, command=lambda pack=pack: uninstall(pack))
        package.pack()
        packages.append(package)
        canvas.config(scrollregion=canvas.bbox("all"))


packages = []
root = Tk()
root.title("Bloatware Remover")
Style().theme_use("default")  # clam, alt, default, classic
history = Text(height=6)
history.pack()
history.tag_config("error", foreground="red")
Button(text="Update", command=show_packages).pack()

canvas = Canvas(borderwidth=0, background="#ffffff")
frame = Frame(canvas)
scrollbar = Scrollbar(orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=scrollbar.set)
canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side=RIGHT, fill=Y)
canvas.create_window((4, 4), window=frame, anchor="nw", tags="frame")
frame.bind(
    "<Configure>",
    lambda event, canvas=canvas: canvas.configure(scrollregion=canvas.bbox("all")),
)

adb = subprocess.run("adb devices".split())
if adb.returncode != 0:
    mb.showerror("Error", "Is adb installed?")

root.mainloop()
