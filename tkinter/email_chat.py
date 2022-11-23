import re
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox as mb
from dataclasses import dataclass
from emails import send_email, new_emails


@dataclass
class Address:
    """Class for storing an email address"""

    address: str = ""
    password: str = ""
    name: str = ""

    def nice(self):
        if not self.name:
            self.name = self.address.split("@")[0].replace(".", " ").title()
        return f"<{self.name}>\n{self.address}"

    def valid(self):
        return re.fullmatch(r"[^@]+@[^@]+\.[^@]+", self.address)

    def creds(self):
        return self.address, self.password


def send():
    msg = msg_entry.get().strip()
    result = send_email(*emails[0].creds(), msg, "Tkinter Chat", recipient.get())
    if result == "OK":
        history["state"] = "normal"
        history.insert(END, msg + "\n", ("right"))
        history["state"] = "disabled"
        msg_entry.delete(0, "end")
        msg_entry.focus_set()
    else:
        mb.showerror("Error sending email", "Could not send email\n" + result)


def check_emails():
    msgs = new_emails(*emails[0].creds(), "Tkinter Chat")
    history["state"] = "normal"
    for msg in msgs:
        history.insert(END, msg["From"], ("user"))
        history.insert(
            END, ": " + msg.get_payload(decode=True).decode("utf-8")[:-2] + "\n"
        )
    history["state"] = "disabled"


def edit_email(old_email=Address()):
    top = Toplevel(root)
    top.title("Edit Email" if old_email.address else "Add Email")
    Label(top, text="Email").pack()
    address = Entry(top)
    address.insert(0, old_email.address)
    address.pack()
    address.focus_set()
    Label(top, text="Password").pack()
    password = Entry(top)
    password.insert(0, old_email.password)
    password.pack()
    Label(top, text="Name (optional)").pack()
    name = Entry(top)
    name.insert(0, old_email.name)
    name.pack()

    def ok():
        email = Address(address.get(), password.get(), name.get())
        if not email.valid():
            mb.showerror("Error", "Invalid email address")
            return
        emails.append(email)
        top.destroy()
        mb.showinfo("Added Email", f"Successfully added \n{email.nice()}")

    Button(top, text="Ok", command=ok).pack()
    top.mainloop()


def manage_emails():
    def wrapper(email):
        return lambda: edit_email(email)

    def ok():
        top.destroy()

    top = Toplevel(root)
    top.title("Manage Emails")
    for email in emails:
        Button(top, text=f"Edit <{email.name}>", command=wrapper(email)).pack()
    Button(top, text="Add Email", command=edit_email).pack()
    Button(top, text="Ok", command=ok).pack()
    top.mainloop()


emails = []
root = Tk()
root.title("Tkinter Chat")

Label(text="History").pack()
history = Text(height=8, width=40)
history.tag_config("right", justify=RIGHT)
history.tag_config("user", underline=True)
history["state"] = "disabled"
history.pack(padx=10)
Label(text="Recipient").pack()
recipient = Entry()
recipient.pack()
Label(text="Message").pack()
msg_entry = Entry()
msg_entry.pack()
Button(text="Send", command=send).pack()
Button(text="Refresh", command=check_emails).pack()
Button(text="Manage Emails", command=manage_emails).pack()

root.after(10000, check_emails)
root.mainloop()
