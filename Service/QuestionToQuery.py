import en_core_web_sm
#import ListStream as LS
import sys
#import pprint
import string


class ListStream:
    def __init__(self):
        self.data = []
    def write(self, s):
        self.data.append(s)
    def __enter__(self):
        sys.stdout = self
        return self
    def __exit__(self, ext_type, exc_value, traceback):
        sys.stdout = sys.__stdout__  

class QuestionToQuery:
    def __init__(self):
        self.nlp = en_core_web_sm.load()

    def TransformQuestionToESQuery(self, question):
        query = self.nlp(question)
        #ls = ListStream()
        #ls = LS()
        with ListStream() as queryTransformed:
        #with LS() as queryTransformed:
            print([(X, X.ent_type_) for X in query])
        #print([(X, X.ent_type_) for X in query])
        if(queryTransformed.data[len(queryTransformed.data) - 1] == '\n'):
           del queryTransformed.data[len(queryTransformed.data) - 1]
        print(queryTransformed.data)
        return queryTransformed.data
