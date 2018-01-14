#-*- coding=UTF-8 -*-
import os
import tkinter
import time

class DirList(object):
    def __init__(self,initdir=None):
        self.top = tkinter.Tk()
        self.label = tkinter.Label(self.top,text="sar directory list")
        self.label.pack()
        self.cwd = tkinter.StringVar(self.top)
        self.dirl = tkinter.Label(self.top,fg="blue",font="Helvetica 12 bold")
        self.dirl.pack()
        #scrollbar and listbox
        self.dirfm = tkinter.Frame(self.top)
        self.dirsb = tkinter.Scrollbar(self.dirfm)
        self.dirsb.pack(side=tkinter.RIGHT,fill=tkinter.Y)
        self.dirlb = tkinter.Listbox(self.dirfm,height=15,width=50,yscrollcommand=self.dirsb.set)
        self.dirlb.bind("<Double-1>",self.setDirAndGo)
        self.dirlb.pack(side=tkinter.LEFT,fill=tkinter.BOTH)
        self.dirsb.config(command=self.dirlb.yview)
        self.dirfm.pack()
        #entry box
        self.diren = tkinter.Entry(self.top,width=50,textvariable=self.cwd)
        self.diren.bind("<Return>",self.doLS)
        self.diren.pack()
        self.bfm = tkinter.Frame(self.top)
        #clear button
        self.bclr = tkinter.Button(self.bfm,text="clear",command=self.clearHandler,
                                  background="black",foreground="white")
        self.bclr.pack(side=tkinter.LEFT)
        #enter button
        self.bent = tkinter.Button(self.bfm,text="enter",command=self.doLS,
                                  background="black",foreground="white")
        self.bent.pack(side=tkinter.LEFT)
        #quit button
        self.bqut = tkinter.Button(self.bfm,text="quit",command=self.top.quit,
                                  background="black",foreground="white")
        self.bqut.pack(side=tkinter.LEFT)
        self.bfm.pack()
    def setDirAndGo(self,ev=None):
        print("setDirAndGo() called")
        self.last = self.cwd.get()
        self.dirlb.config(selectbackground="red")
        check = self.dirlb.get(self.dirlb.curselection())
        if not check:
            check = os.curdir
        self.cwd.set(check)
        self.doLS()
    def doLS(self,ev=None):
        print("doLS() called")
        error = ""
        tdir = self.cwd.get()
        if not tdir:
            tdir = os.curdir
        if not os.path.exists(tdir):
            error = tdir + ":no such file"
        elif not os.path.isdir(tdir):
            error = tdir + ":not a directory"
        if error:
            print(error)
            self.cwd.set(error)
            self.top.update()
            time.sleep(2)
            if not (hasattr(self,"last") and self.last):
                self.last = os.curdir
            self.cwd.set(self.last)
            self.dirlb.config(selectbackground="blue")
            self.top.update()
            return
        self.cwd.set("fetching directory contents...")
        self.top.update()
        dirlist = os.listdir(tdir)
        dirlist.sort()
        os.chdir(tdir)

        self.dirl.config(text=os.getcwd())
        self.dirlb.delete(0,tkinter.END)
        self.dirlb.insert(tkinter.END,os.curdir)
        self.dirlb.insert(tkinter.END,os.pardir)
        for eachFile in dirlist:
            self.dirlb.insert(tkinter.END,eachFile)
        self.dirlb.config(selectbackground="blue")

    def clearHandler(self):
        print("clearHandler() called")
