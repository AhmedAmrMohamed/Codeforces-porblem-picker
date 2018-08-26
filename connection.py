import threading
import pickle
from time import sleep
class connection:
    def __init__(self,classref,members):
        self.members = set(members)
        self.donemembers = set()
        self.__doneHandles = set()
        self.classref = classref
        self.failed   = set()
        self.li=[]

        while(self.filter()):
            print(self.members)
            self.threads()
            self.buffer()

    def filter(self):
        for key in self.__doneHandles:
            self.members.discard(key)
        return len(self.members)
    def threads(self):
        for num,me in enumerate(self.members):
            x=threading.Thread(target=lambda me=me:self.connect(me))
            x.start()
            self.li.append(x)

            if (1+num)%5==0:
                self.buffer()
                self.li=[]

    def buffer(self):
        for i in self.li:
            while(i.isAlive()):
                pass

    def connect(self,name):
        print('thread ',name)
        try:
            x=self.classref(name)
            self.donemembers.add(x)
            self.__doneHandles.add(x.handle)
        except Exception:
            print(name,'------------')
            self.__doneHandles.add(name)
            # self.members.discard(name)

# import time
# def count():
#     for i in range(10):
#         time.sleep(1)
# li=[threading.Thread(target=count),threading.Thread(target=count)]
# for i in li:
#     i.start()
# def buffer():
#     for i in li:
#         while(i.isAlive()):
#             pass
#     print('done')
# buffer()









    # def __init__(self,classref,members):
    #     self.members = set(members)
    #     self.donemembers = set()
    #     self.classref = classref
    #     self.contestants = set()
    #     self.done = False
    #     self.checkpast()
    #     self.process()
    #
    # def checkpast(self):
    #     f=open('connection','rb')
    #     x=pickle.load(f)
    #     f.close()
    #     if not x.done:
    #         if self.allert():
    #             self = x
    #             print('reloaded',self.donemembers)
    # def allert(self):
    #     print('reloode last unfinished connection')
    #     if input().lower()[0] == 'y':
    #
    #         return True
    #     return False
    #
    # def process(self):
    #     print('a')
    #     for handle in self.members:
    #         print(handle,self.donemembers,handle in self.donemembers)
    #         if handle in self.donemembers:
    #             continue
    #         try:
    #             self.contestants.add(self.classref(handle))
    #             self.donemembers.add(handle)
    #             print(handle,"OK",self.done)
    #             self.save()
    #         except Exception as exc:
    #             print('connection lost for : ',exc)
    #     self.done = True
    #     self.save()
    # def save(self):
    #     f=open('connection','wb')
    #     pickle.dump(self,f)
    #     f.close()
