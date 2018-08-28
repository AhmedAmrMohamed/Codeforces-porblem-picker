import tkinter as tk
from tkinter import Entry
from inter import *
import threading
class gui:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Problem Picker')
        self.inter = inter(self)
        self.buttons={}
        self.labels ={}
        self.tags =set()
        self.tagoption = tk.IntVar()
        self.filteroption = tk.IntVar()
        self.row=1
        self.handles  = set()
        self.handle = tk.StringVar()
        self.root.geometry('600x500')
        self.root.bg='white'
        self.handleLabel = tk.Label(self.root,text = 'Enter handle',font ='console 10 bold')
        self.handleLabel.grid(row = 1, column = 1,columnspan = 2)
        self.handleEntryfunc()
        self.addHandleButtonfun()
        self.problemsbutton = tk.Button(self.root,text = "choose porblems" ,font ='console 10 bold',command = self.chooseproblems)
        self.problemsbutton.grid(row = 2,column = 2,padx=10,pady=5)
        tk.Button(self.root,text='Load last handles',command=self.loadlasthandles).grid(row=3,column=2,pady=5,padx=10)
        tk.Button(self.root,text='update the base',command=self.updatebase).grid(row=4,column=2,pady=5,padx=10)
        self.lastbasetime = tk.Label(self.root,text = f'last update on : {self.inter.basetime}')
        self.lastbasetime.grid(row=5,column=2,pady=5,padx=10)
        self.root.mainloop()

    def handleEntryfunc(self):
        self.handleEntry = tk.Entry(self.root,textvariable =  self.handle)
        self.handleEntry.delete(0,100)
        self.handleEntry.grid(row = 1,column = 5 , columnspan = 5,padx = 10)
        self.handleEntry.config(width = 20)

    def addHandleButtonfun(self):
        self.addHandleButton = tk.Button(self.root,text = 'Add Handle',font = 'console 10 bold',command = self.addhandlefun)
        button =  self.addHandleButton
        button.grid(row=1,column = 10,padx = 10)

    def addhandlefun(self):
        handle = self.handle.get()
        self.handle.set('')
        if not(handle in self.handles):
            self.handles.add(handle)
            self.row+=1
            row = self.row
            label  = tk.Label(self.root,text = handle,font = 'console 10 bold')
            button = tk.Button(self.root,text = 'remove',command = lambda row=row:self.remove(row))
            label.grid(column=10,row = row,padx =10,pady = 5)
            button.grid(column=13,row=row,padx = 10)
            self.buttons[row] = button
            self.labels[row]  = label
            # self.lables[]
        print(self.buttons)

    def remove(self,row):
        labelref = self.labels[row]
        butref = self.buttons[row]
        butref.config(bg = 'red',text = 'removed',command = lambda row=row:self.reinsert(row) )
        self.handles.remove(labelref.cget('text'))
        print(self.handles)

    def reinsert(self,row):
        labelref = self.labels[row]
        butref = self.buttons[row]
        butref.config(bg = 'white',text = 'remove',command = lambda row=row:self.remove(row) )
        self.handles.add(labelref.cget('text'))
        print(self.handles)

    def loadlasthandles(self):
        handles  = self.inter.loadlast(self.inter.handlesfile)
        for handle in handles:
            self.handle.set(handle)
            self.addhandlefun()

    def updatebase(self):
        self.inter.updatebase()
        self.lastbasetime.config(text=f'last update on : {self.inter.basetime}')

    def chooseproblems(self):
        print(self.handles)
        self.inter.picklelast(self.inter.handlesfile,self.handles)
        self.inter.connectthreading(self.handles)
        self.pr = tk.Tk()
        self.pr.title('Problem Picker')
        self.pr.geometry('600x500')
        self.rendertags()
        self.rendertagsoptions()
        self.renderfilteroptions()
        self.rendersubmit()
        # self.renderloadlasttags()
        self.pr.mainloop()

    def rendertags(self):
        row = 0
        col =0
        tags = list(self.inter.gettags())
        self.tagboxes = {}
        tags.sort()
        for tag in tags :
            check = tk.Checkbutton(self.pr,text = tag)
            check.grid(row = row//2,column = col%2)
            check.config(justify='left',width = 10,anchor = "w",command  = lambda tag=tag:self.updatetags(tag))
            row+=1
            col+=1
            self.tagboxes[tag] = check

    def rendertagsoptions(self): #for some reason this method wasn't working the way it's suppose to, so i made a hack around .
        tk.Label(self.pr,text='Problems must contain',font = 'console 10 bold').grid(row = 0,column=10,columnspan=4)
        tk.Radiobutton(self.pr,text='only These tags',value=1,variable = self.tagoption,anchor = 'w',command = lambda :self.hacktag(1)).grid(row=1,column = 10,padx = 10)
        tk.Radiobutton(self.pr,text='some of These tags',value=2,variable = self.tagoption,anchor = 'w',command= lambda :self.hacktag(2)).grid(row=2,column = 10,padx = 10)
        tk.Radiobutton(self.pr,text='All of These tags',value=3,variable = self.tagoption,anchor = 'w',command = lambda :self.hacktag(3)).grid(row=3,column =10,padx = 10)

    def renderfilteroptions(self):
        tk.Label(self.pr,text='Filter by',font = 'console 10 bold').grid(row = 5,column=10,columnspan=4)
        tk.Radiobutton(self.pr,text='not Submitted by the contestants',variable = self.filteroption,value=1,anchor = 'w',command = lambda :self.hackfilter(1)).grid(row=6,column = 10,padx = 10)
        tk.Radiobutton(self.pr,text='not Accepted by the contestants',variable = self.filteroption,value=2,anchor = 'w',command = lambda :self.hackfilter(2)).grid(row=7,column = 10,padx = 10)

    def rendersubmit(self):
        but = tk.Button(self.pr,text = 'Submit',font = 'console 10 bold')
        but.config(command = self.submit,width = 7)
        but.grid(row = 9,column=10,padx = 3)
        self.submitButton = but
        self.submitsate()

    def submitsate(self):
        def statethread():
            while self.inter.thread.isAlive():
                self.submitButton.config(state="disabled")
            self.submitButton.config(state="normal")
        threading.Thread(target = statethread).start()

    def hacktag(self,num):
        self.tagoption.set(num)

    def hackfilter(self,num):
        self.filteroption.set(num)

    def renderloadlasttags(self):
        but = tk.Button(self.pr,text = 'load last tags',command = self.loadlasttags)
        but.grid(row = 11,column = 4)

    def loadlasttags(self):
        self.tags = self.inter.loadlast(self.inter.tagsfile)
        for tag in self.tagboxes:
            if tag in self.tags:
                self.tagboxes[tag].invoke()

    def updatetags(self,tag):
        if tag in self.tags:
            self.tags.remove(tag)
        else:
            self.tags.add(tag)

    def submit(self):
        # self.inter.org=False
        print(self.tags)
        self.inter.picklelast(self.inter.tagsfile,self.tags)
        self.inter.submit()
        tk.Label(self.pr,text='problems wrote to problems.txt',font ='console 10 bold' ).grid(row = 10,column = 10,padx=10,pady=10)

gui()
