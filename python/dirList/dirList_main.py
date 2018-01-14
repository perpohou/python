#-*- coding=UTF-8 -*-
import dirList
import os
import tkinter
import time
def main():
    print("hello world")
    d = dirList.DirList(os.curdir)
    tkinter.mainloop()
if __name__ == "__main__":
    main()

