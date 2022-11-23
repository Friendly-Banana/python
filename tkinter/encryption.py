import string
import tkinter as tk

def key_ok(msg, key):
    if len(msg) > len(key):
        error.set("Key too short")
        return False
    for char in msg:
        if char not in abc:
            error.set("Message contains invalid character: \"" + char + "\"")
            return False
    for char in key:
        if char not in abc:
            error.set("Key contains invalid character: \"" + char + "\"")
            return False
    error.set("")
    return True

def encrypt(msg, key):
    if key_ok(msg, key):
        encrypted = ""
        for m, k in zip(msg, key):
            encrypted += abc[(abc.index(m) + abc.index(k)) % len(abc)]
        return encrypted

def decrypt(msg, key):
    if key_ok(msg, key):
        decrypted = ""
        for i, char in enumerate(msg):
            decrypted += abc[(abc.index(char) - abc.index(key[i])) % len(abc)]
        return decrypted

def caesar(msg, key):
    try:
        rot = int(key)
    except ValueError:
        return error.set("Key must be an integer")
    new_msg = "".join(abc[(abc.index(char) + rot) % len(abc)] for char in msg)
    return new_msg

def switch_in_out(old_msg, key):
    msg.set(out.get())
    return old_msg

def charset_changed():
    global abc
    abc = ""
    for charset in char_check:
        if char_check[charset].get():
            abc += charsets[charset]

def msg_or_key_changed(*args):
    msg_len.set(f"Input ({len(msg.get())} chars)")
    key_len.set(f"Key ({len(key.get())} chars)")

def helper(cmd):
    return lambda: out.set(cmd(msg.get(), key.get()))

abc = ""
charsets = {"Lowercase" : string.ascii_lowercase, "Uppercase" : string.ascii_uppercase, "Digits" : string.digits, "Punctuation" : string.punctuation, "Space" : " "}
methods = ("Switch In- and Output", switch_in_out), ("Encrypt", encrypt), ("Decrypt", decrypt), ("Caesar / Rotate", caesar)
root = tk.Tk()
root.title("Crypto")

msg = tk.StringVar()
msg_len = tk.StringVar(value="Input (0 chars)")
msg.trace_add("write", msg_or_key_changed)
key = tk.StringVar()
key_len = tk.StringVar(value="Key (0 chars)")
key.trace_add("write", msg_or_key_changed)
out = tk.StringVar()
error = tk.StringVar()

topbar = tk.Frame()
topbar.pack()
tk.Label(topbar, text="Methods").pack()
for text, cmd in methods:
    tk.Button(topbar, text=text, command=helper(cmd)).pack(side=tk.LEFT)

char_check = {k : tk.IntVar() for k in charsets}
char_selection = tk.Frame()
char_selection.pack(side=tk.RIGHT)
tk.Label(char_selection, text="Use Characters").pack()
for charset in charsets:
    tk.Checkbutton(char_selection, text=charset, command=charset_changed, variable=char_check[charset]).pack(anchor="w")

entries = tk.Frame()
entries.pack(side=tk.LEFT)
tk.Label(entries, textvariable=msg_len).grid(row=1, column=0)
tk.Entry(entries, textvariable=msg, bg="white", fg="black").grid(row=1, column=1)
tk.Label(entries, textvariable=key_len).grid(row=2, column=0)
tk.Entry(entries, textvariable=key, bg="white", fg="black").grid(row=2, column=1)
tk.Label(entries, text="Output").grid(row=3, column=0)
tk.Entry(entries, textvariable=out, bg="white", fg="black").grid(row=3, column=1)
tk.Label(entries, justify=tk.CENTER, textvariable=error, foreground="red").grid(rowspan=2)

root.mainloop()