from os import listdir
from os.path import isfile, join
from pathlib import Path
import string
import ImportInElasticSearch as ES
#import json

class PreTraitement:
    def __init__(self) :
        self.dataPath = "../data/freebase-wex-2011-01-18-articles-first100k.tsv"

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
        for item in datas:
            esData = {"id": int(item[0]),
                      "index": index,
                      "doc_type": doc_type,
                      "body": {"word": item[1],
                              "date": item[2],
                              "xml": item[3],
                              "sentence": item[4]}}
            esDatas.append(esData)

        print("End PrepareDatasForElasticSearch")
        return esDatas

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


pr = PreTraitement()

datas = pr.PrepareDatas()
esDatas = pr.PrepareDatasForElasticSearch(datas)

es = ES.ES()

es.Imports(esDatas)