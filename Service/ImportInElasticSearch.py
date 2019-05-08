#import requests
from elasticsearch import Elasticsearch

class ES:
    def __init__(self, host='localhost', port=9200):
        self.es = Elasticsearch([{'host': host, 'port': port}])


    def Import(self, index, doc_type, body, id):
        self.es.index(index=index, doc_type=doc_type, body=body, id=id)

    def Imports(self, list):
        print("Begin Imports")
        for item in list:
            self.es.index(index=item['index'], doc_type=item['doc_type'], body=item['body'], id=item['id'])
            #ES.Import(item[1], item[2], item[3], item[0])
        print("End Imports")

    def GetData(self, index, doc_type, id):
        return es.get(index=index, doc_type=doc_type, id=id)
