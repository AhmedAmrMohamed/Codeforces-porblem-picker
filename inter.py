import threading
import pickle
from problems import problems
from contestant import contestant
from connection import connection
import time
class inter:
    def __init__(self,info):
        self.loadedbase  = problems.loadbase()
        self.base = self.loadedbase['base']
        self.basetime = self.loadedbase['time']
        self.info = info
        self.org = "new"
        self.org = True
        self.handlesfile = 'handles'
        self.tagsfile = 'tags'

    def gettags(self):
        return problems.getalltags(self.base)

    def connectthreading(self,handles):
        self.thread = threading.Thread(target=lambda hadnles=handles:self.connect(handles))
        self.thread.start()

    def connect(self,handles):
        self.connectioninfo = connection(contestant,handles).donemembers

    def submit(self):
        print('self.org',self.org)
        if self.org == True:
            self.parse()
        elif self.org==False:
            self.connectthreading(self.info['handles'])
            while self.thread.isAlive():
                pass
        self.org=False
        contestantsinfo = self.connectioninfo
        probs = self.getprobs(self.info['tags'],self.info['tagoption'])
        # print('tags',self.info['tags'],self.info['tagoption'])
        probs = self.filterprobs(probs,contestantsinfo,self.info['filteroption'])
        # print('probs',probs)
        if len(probs)==0:
            probs =['None found']
        file = open('problems.txt','w',encoding='UTF-8')
        for i in probs:
            print(i,file = file)
        file.close()

    def getprobs(self,tags,tagoption):
        probs = set()
        if(tagoption==1):
            probs = problems.containOnlyTags(self.base,tags)
        elif(tagoption==2):
            probs = problems.containSomeTags(self.base,tags)
        elif(tagoption==3):
            probs = problems.containAllTags(self.base,tags)
        return probs

    def filterprobs(self,probs,contestants,filteroption):
        if filteroption ==1:
            probs = problems.filterSubmissions(probs,contestants)
        elif filteroption==2:
            probs = problems.filterAccepted(probs,contestants)
        return probs

    def updatebase(self):
        self.loadedbase = problems.updatebase()
        self.base = self.loadedbase['base']
        self.basetime = self.loadedbase['time']

    def parse(self):
        info=self.info
        self.info={'handles':info.handles,'tagoption':info.tagoption.get(),'filteroption':info.filteroption.get(),'tags':info.tags}




    def loadlast(self,filename):
        print(f'loading from {filename}...')
        file=open(filename,'rb')
        load = pickle.load(file)
        file.close()
        return load

    def picklelast(self,filename,tosave):
        print(f'pickleing data...')
        file = open(filename,'wb')
        pickle.dump(tosave,file)
        file.close()
