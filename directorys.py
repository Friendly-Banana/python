#!/usr/bin/env python3
import os

default_path = os.path.expanduser('~')

def pathwalker(depth, start_dir=default_path):
    i = 0
    for (path, dirs, files) in os.walk(start_dir):
        print("Path: " + path)
        print(str(len(dirs)) + " Directorys: " + str(dirs))
        print(str(len(files)) + " Files: " + str(files))
        i += 1
        if i >= depth:
            break
        else:
            print("\n")


def file_events():
    import pyinotify

    class MyEventHandler(pyinotify.ProcessEvent):
        def process_IN_ACCESS(self, event):
            print("ACCESS event:", event.pathname)

        def process_IN_ATTRIB(self, event):
            print("ATTRIB event:", event.pathname)

        def process_IN_CLOSE_NOWRITE(self, event):
            print("CLOSE_NOWRITE event:", event.pathname)

        def process_IN_CLOSE_WRITE(self, event):
            print("CLOSE_WRITE event:", event.pathname)

        def process_IN_CREATE(self, event):
            print("CREATE event:", event.pathname)

        def process_IN_DELETE(self, event):
            print("DELETE event:", event.pathname)

        def process_IN_MODIFY(self, event):
            print("MODIFY event:", event.pathname)

        def process_IN_OPEN(self, event):
            print("OPEN event:", event.pathname)

    # watch manager
    wm = pyinotify.WatchManager()
    wm.add_watch("/var/log", pyinotify.ALL_EVENTS, rec=True)

    # event handler
    eh = MyEventHandler()

    # notifier
    notifier = pyinotify.Notifier(wm, eh)
    notifier.loop()


# get the current working directory
def get_dir():
    print(os.getcwd())


# change the current working directory
def set_dir(new_dir):
    os.chdir(new_dir)


# list directories
def list_dirs(path=default_path):
    print(os.listdir(str(path)))


# make a new directory
def mkdir():
    os.mkdir()


# rename a directory or a file
def rename(old_name, new_name):
    os.rename(old_name, new_name)


# remove a file
def remove(file):
    os.remove(file)


# removes only empty dictionaries
def rmdir(path):
    os.rmdir()


# removes a complete dictionary
def deldir(path):
    import shutil

    shutil.rmtree(path)
