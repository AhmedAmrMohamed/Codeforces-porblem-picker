import requests
import time
class problems:

    def detector(function):
        def wrapper(base,tags=None):
            print(wrapper.__name__,'in effect',tags)
            tags=set(tags)
            probs=set()
            return function(base,probs,tags)
        wrapper.__name__ = function.__name__
        wrapper.__doc__ = function.__doc__
        return wrapper
    @detector
    def containAllTags(base,probs,tags=None,):
        '''return a list of the probelms with all the tags and more tags'''
        for problem in base:
            if base[problem].issuperset(tags):
                probs.add(problem)
        return probs
    @detector
    def containSomeTags(base,probs,tags):
        '''return a list of the probelms with atleast one of the tags'''
        for problem in base:
            if len(base[problem].intersection(tags))!=0:
                probs.add(problem)
        return probs
    @detector
    def containOnlyTags(base,probs,tags):
        '''return a list of the probelms that contains only these tags'''
        for problem in base:
            ref  = base[problem]
            if len(tags)==len(ref) and ref.issuperset(tags):
                probs.add(problem)
        return probs

    def filterAccepted(probs,contestants):
        '''filter the set of problems by removing the ones that have been
            submitted and Accepted by the contestants'''
        probscpy = probs.copy()
        for name in contestants:
            probscpy.difference_update(name.Accepted)
        return probscpy

    def filterSubmissions(probs,contestants):
        '''filter the set of problems by removing the ones that have been
        submitted by the contestants'''
        probscpy = probs.copy()
        for name in contestants:
            probscpy.difference_update(name.Submissions)
        return probscpy
    def getalltags(base):
        tags = set()
        for problem in base:
            tags.update(base[problem])
        return tags

    def updatebase():
         url       = 'http://codeforces.com/api/problemset.problems'
         res       = requests.get(url).json()['result']['problems']
         base      = {'time':time.ctime(),'base':{key['name']:set(key['tags'])  for key in res}}
         import pickle
         file = open('base','wb')
         pickle.dump(base,file)
         file.close()
         return base

    def loadbase():
        import pickle
        file = open('base','rb')
        base  = pickle.load(file)
        file.close()
        return base

    #
    # def containAllTags(base,tags=None):
    #     probs = []
    #     tags  = set(tags)
    #     for problem in base:
    #         if base[problem].issuperset(tags):
    #             probs.append(problem)
    #     return probs
    #
    # def containSomeTags(base,tags):
    #     probs = []
    #     tags  = set(tags)
    #     for problem in base:
    #         if len(base[problem].intersection(tags))!=0:
    #             probs.append(problem)
    #     return probs
    # def containOnlyTags(base,tags):
    #     probs=[]
    #     tags = set(tags)
    #     for problem in base:
    #         ref  = base[problem]
    #         if len(tags)==len(ref) and ref.issuperset(tags):
    #             probs.append(problem)
    #     return probs



        # def updatebase():
        #     '''save and return a dictionary of sets of all the problems in every tag'''
        #     url       = 'http://codeforces.com/api/problemset.problems'
        #     print(url)
        #     res       =  requests.get(url).json()
        #     base      = {}
        #     print('processing localy...')
        #     for key in res['result']['problems']:
        #         for tag in key['tags']:
        #             if tag in base:
        #                 base[tag].add(key['name'])
        #             else:
        #                 base[tag]  = {key['name']}




        # def containTags(base,tags=None):
        #     if not tags:
        #         return base
        #         basecpy = base[tags[0]].copy()
        #         for tag in tags:
        #             basecpy.update(base[tag])
        #             return basecpy
        #             def containAllTags(base,tags):
        #                 if not tags:
        #                     return base
        #                     basecpy = base[tags[0]].copy()
        #                     for tag in tags:
        #                         basecpy.intersection_update(base[tag])
        #                         return basecpy
        #
        #                         def containOnlyTags(base,tags):
        #                             url = f"http://codeforces.com/api/problemset.problems?tags={';'.join(tags)}"
        #                             res = requests.get(url).json()['result']
        #                             print(res)
        #                             res = {key['name'] for key in res['problems']}
        #                             return res
