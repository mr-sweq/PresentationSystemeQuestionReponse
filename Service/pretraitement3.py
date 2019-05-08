import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.tag import pos_tag
from nltk.chunk import ne_chunk
import spacy
from spacy import displacy
from collections import Counter
import en_core_web_sm
from nltk.chunk import conlltags2tree, tree2conlltags
from pprint import pprint
import sys
import string
import ImportInElasticSearch as ES

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


class PreTraitement3:
    def __init__(self) :
        self.dataPath = "../data/freebase-wex-2011-01-18-articles-first100k.tsv"
        self.nlp = en_core_web_sm.load()

    def PrepareDatas(self, origin=None):
        print("Begin PrepareDatas")
        datas = []
        datapath = origin
        if(origin==None):
            datapath = self.dataPath
        with open(datapath, 'r', encoding="utf8") as file:
            for line in file.readlines():
                data = self._PrepareLine(line)
                datas.append(data)
        print("End PrepareDatas")
        return datas

    def PrepareDatasForElasticSearch(self, datas, index="text", doc_type="text"):
        print("Begin PrepareDatasForElasticSearch")

        esDatas = []
        i = 1
        for item in datas:
            doc = self.nlp(item[4])
            with ListStream() as context:
                print([(X, X.ent_type_) for X in doc])

            document = {'sentence': item[4],
                    'Context': context.data}
            esData = {"id": int(item[0]),
                      "index": index,
                      "doc_type": doc_type,
                      "body": document}
            esDatas.append(esData)
            print('i : ' + str(i) + ', ' + str(i/100000) + '%')
            i += 1

        print("End PrepareDatasForElasticSearch")
        return esDatas

    def PrepareDatasForElasticSearchAndSendIt(self, datas, index="text", doc_type="text"):
        print("Begin PrepareDatasForElasticSearch")

        
        es = ES.ES()

        

        #esDatas = []
        i = 1
        lineprocessed = 1
        for item in datas:
            line = item[4]
            sentences = sent_tokenize(line)
            for sentence in sentences:
                doc = self.nlp(sentence)
                with ListStream() as context:
                    print([(X, X.ent_type_) for X in doc])

                document = {'sentence': sentence,
                        'Context': context.data,
                        'WikiID': item[0]}
                esData = {"id": i,
                          "index": index,
                          "doc_type": doc_type,
                          "body": document}
                #esDatas.append(esData)
                es.Import(id = i,
                          index = index,
                          doc_type = doc_type,
                          body = document)
                
                #print('i : ' + str(i))
                i += 1
            print('lineprocessed : ' + str(lineprocessed) + ', ' + str(lineprocessed/100000*100) + '%')
            lineprocessed += 1

        print("End PrepareDatasForElasticSearch")

    def _PrepareLine(self, line) :
        text = line
        text = text.replace('\\n\\r', '')
        text = text.replace('\\r', '')
        text = text.replace('\\n', '')
        text = text.replace('\n\r', '')
        text = text.replace('\r', '')
        text = text.replace('\n', '')

        data = text.split("\t")

        return data

    def _PrintData(self, data) :
        print(len(data))
        print("***********")
        print(data[0])
        print("***********")
        print(data[1])
        print("***********")
        print(data[2])
        print("***********")
        print(data[3])
        print("***********")
        print(data[4])
        print("***********")


pr = PreTraitement3()

datas = pr.PrepareDatas()
#esDatas = pr.PrepareDatasForElasticSearch(datas, 'textner', 'textner')
pr.PrepareDatasForElasticSearchAndSendIt(datas, 'sentencener', 'sentencener')