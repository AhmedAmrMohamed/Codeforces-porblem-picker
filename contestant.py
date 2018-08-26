import requests
import logging
class contestant:
    def __init__(self,handle,last=100000):
        print(handle)
        self.handle     = handle
        self.__gotSubs  = False
        self.badhandle = True
        # self.__ACC      = False
        if last:
            self.getTries(last)
            self.getAccepted(last)
            self.getSubmissions(last)

    def getTries(self,last):
        '''get the last 'last' Submissions by the user regardless of their verdict'''
        url = f'http://codeforces.com/api/user.status?handle={self.handle}&from=1&count={last}'
        try:
            res = requests.get(url).json()
        except Exception as exc:
            raise RuntimeError(f'bad request on {self.handle}') from exc
        print(self.handle,res['status'])
        if res['status']!='OK':
            self.badhandle = True
            raise RuntimeError('wrong handle')
        # self.Submissions = {key['problem']['name']:key['verdict'] for key in res['result'}
        self.tries = res
        return 'OK'

    def getAccepted(self,last):
        '''build up self.Submissions : a set of the last "last" problems have attempted and  Accepted'''
        self.Accepted = {key['problem']['name'] for key in self.tries['result'] if key['verdict'] =='OK'}

    def getSubmissions(self,last):
        '''build up self.Submissions : a set of the last "last" problems have been attempted'''
        self.Submissions = {key['problem']['name'] for key in self.tries['result']}
