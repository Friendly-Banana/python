import os, shutil, glob
import tkinter as tk
import tkinter.messagebox as msg

TAGS = "Log", "Debug", "Warning", "Error"
SKIP_OPTIONS = "Skip all", "Overwrite all", "Ask for each"


def default_ask_ov():
    return input("Overwrite [y/n]? ").lower().startswith("y")


def ask_overwrite():
    return msg.askyesno(message="Overwrite existing file?")


class FileSorter:
    def __init__(self):
        self.home = "/data/user/0/Programme/"
        self.excluded = []
        self.dirs = {".py": "Python", ".cs": "C#"}
        self.path_sep = "/"

    def sort(self, skip=0, logger=print, get_input=default_ask_ov):
        """
        Sorts files
        skip: controls the handling of files which exist at the destination
        0 skip all
        1 overwrite all
        2 ask for each
        """
        logger(f"Debug: targets are {self.dirs}")
        logger(f"Debug: Skipoption is {skip}")
        logger(f"Debug: excluded: {self.excluded}")
        os.chdir("..")
        logger(f"Debug: Working in {os.getcwd()}")
        for file_path in [
            path for path in glob.glob("**", recursive=True) if os.path.isfile(path)
        ]:
            if any(path in file_path for path in self.excluded):
                continue
            logger(f"Log: {file_path}")
            _, file_ext = os.path.splitext(file_path)
            if file_ext in self.dirs.keys():
                if os.path.exists(file_path):
                    logger(f'Warning: "{file_path}" already exists.')
                    if skip == 0:
                        logger(f'Log: Skipped "{file_path}"')
                        continue
                    elif skip == 1:
                        pass
                    elif skip == 2:
                        if not get_input():
                            continue
                        logger(f'Log: Overwrote "{file_path}"')
                # creates a new folder
                if not os.path.exists(self.dirs[file_ext]):
                    os.mkdir(self.dirs[file_ext])
                shutil.move(
                    file_path,
                    self.dirs[file_ext]
                    + self.path_sep
                    + file_path.split(self.path_sep)[-1],
                )

    def gui_sort(self):
        self.root = tk.Tk()
        self.dir_frame = tk.Frame(self.root)
        self.dir_frame.pack()
        tk.Label(self.dir_frame, text="Ending").grid(row=0, column=0)
        tk.Label(self.dir_frame, text="Destination").grid(row=0, column=1)
        self.dir_label = list()
        for index, ext in enumerate(self.dirs.keys()):
            dir = tk.Entry(self.dir_frame)
            dir.insert(0, ext)
            dir.grid(row=1 + index, column=0)
            dir_ext = tk.Entry(self.dir_frame)
            dir_ext.insert(0, self.dirs[ext])
            dir_ext.grid(row=1 + index, column=1)
            self.dir_label.append((dir, dir_ext))
        tk.Button(self.root, text="×", command=self.remove_last).pack(side=tk.TOP)
        tk.Button(self.root, text="+", command=self.add_entry).pack(side=tk.TOP)

        # excluded
        self.excl = tk.StringVar(self.root, ", ".join(self.excluded))
        tk.Entry(self.root, textvariable=self.excl).pack(fill=tk.X)

        sb = tk.Scrollbar(self.root)
        text = tk.Text(self.root, background="black", yscrollcommand=sb.set)
        sb.config(command=text.yview)
        sb.pack(side=tk.RIGHT)
        text.pack()
        self.msg = list()
        self.msg_box = text
        # tags
        text.tag_config("Log", foreground="white")
        text.tag_config("Debug", foreground="lightblue")
        text.tag_config("Warning", foreground="yellow")
        text.tag_config("Error", foreground="red")
        self.visible = 0
        self.tag_vars = list()
        options = tk.Frame(self.root)
        options.pack()
        for index, tag in enumerate(TAGS):
            tag_var = tk.IntVar()
            tk.Checkbutton(
                options, text=tag, variable=tag_var, command=self.change_visible
            ).grid(row=0, column=index)
            self.tag_vars.append(tag_var)

        self.skip = tk.IntVar(self.root, 0)
        for index, skip in enumerate(SKIP_OPTIONS):
            tk.Radiobutton(options, text=skip, variable=self.skip, value=index).grid(
                row=1, column=index
            )

        tk.Button(self.root, text="Sort", command=self.call_sort).pack()
        self.root.mainloop()

    # helper methods

    def send_msg(self, msg):
        self.msg.append(msg)
        for tag in TAGS:
            if tag in msg and TAGS.index(tag) >= self.visible:
                self.msg_box.insert(tk.END, msg + "\n", tag)
                return
        self.msg_box.insert(tk.END, msg + "\n")

    def change_visible(self):
        self.msg_box.delete("1.0", tk.END)
        for msg in self.msg:
            for index, tag in enumerate(TAGS):
                if tag in msg and self.tag_vars[index].get():
                    self.msg_box.insert(tk.END, msg + "\n", tag)
        self.msg_box.yview(0)

    def remove_last(self):
        index = len(self.dir_label) - 1
        if index < 0:
            return
        # key = list(self.dirs.keys())[index]
        # self.dirs.pop(key, None)
        dir_lab, dir_ext = self.dir_label.pop(index)
        dir_lab.destroy()
        dir_ext.destroy()

    def add_entry(self):
        pos = len(self.dir_label) + 1
        dir = tk.Entry(self.dir_frame)
        dir.grid(row=pos, column=0)
        dir_ext = tk.Entry(self.dir_frame)
        dir_ext.grid(row=pos, column=1)
        self.dir_label.append((dir, dir_ext))

    def call_sort(self):
        self.excluded = self.excl.get().split(", ")
        self.dirs = {key.get(): value.get() for key, value in self.dir_label}
        self.sort(self.skip.get(), self.send_msg, ask_overwrite)


if __name__ == "__main__":
    FileSorter().gui_sort()
