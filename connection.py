import threading
import pickle
from time import sleep
class connection:
    '''this is the calss responsible for threading the http requests.'''
    def __init__(self,classref,members):
        '''
        classref :: a refrence to the contestant class
        members  :: a list of the members handles
        '''
        self.members = set(members)    #handles of the members
        self.donemembers = set()       #contestant objects of the members that have already been processed
        self.__doneHandles = set()     #a temp set to hold the members handles that have been processed so they
                                       #can be seafely removed from self.donemembers.
        self.classref = classref
        self.failed   = set()          #handles that haven't been processed correctly
        self.li=[]                     #A list of all the active threads.

        while(self.filter()):
            print(self.members)
            self.threads()
            self.buffer()

    def filter(self):
        """
        remove the handles in self.__doneHandles from self.donemembers
        return True if there still members to be processed; False otherwise.
        """
        for key in self.__doneHandles:
            self.members.discard(key)
        return len(self.members)

    def threads(self):
        for num,me in enumerate(self.members):
            #the three lines below intialize a thread with the right info and add it to self.li
            x=threading.Thread(target=lambda me=me:self.connect(me))
            x.start()
            self.li.append(x)
            #if there are 5 active threads hold on till all is finished
            if (1+num)%5==0:
                self.buffer()
                self.li=[]

    def buffer(self):
        """
        Keep this thread paused till all the other threads are done.
        """
        for i in self.li:
            while(i.isAlive()):
                pass

    def connect(self,name):
        """
        intialize the contestant object -the one handling the http requests
        and add the preocessed handles to both self.donemembers and self.__doneHandles
        """
        print('thread ',name)
        try:
            x=self.classref(name)
            self.donemembers.add(x)
            self.__doneHandles.add(x.handle)
        except Exception:
            print(name,'------------')
            self.__doneHandles.add(name)
            # self.members.discard(name)


