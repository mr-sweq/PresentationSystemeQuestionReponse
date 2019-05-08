from elasticsearch import Elasticsearch
import requests
import pprint

def QueryToES(query, index = "text", doc_type = "text"):

    es = Elasticsearch()
    res = es.search(index=index, doc_type=doc_type, body={"query": {"match": {"word": query}}})
    if(res['hits']['total'] < 1):
        res = es.search(index=index, doc_type=doc_type, body={"query": {"match": {"sentence": query}}})
    return res['hits']#['hits']
    #print("%d documents found" % res['hits']['total'])
    #for doc in res['hits']['hits']:

        #print("%s) %s" % (doc['_id'], doc['_source']['word']))
        #print("************************************************************************")
        #print(doc['_score'])
        #print(doc['_source']['word'])
        #print(doc['_source']['sentence'])

def QueryToES2(query, index = "text", doc_type = "text"):

    es = Elasticsearch()

    should_match = []

    for items in query :
        word_list = items.replace('[', '').replace(']', '')
        word_list = word_list.split('), (')
        for word in word_list:
            context = {"match" : {"Context": word.replace('(', '').replace(')', '')}}
            should_match.append(context)

    body = {
      "query": {
        "bool": {
          #"must": [{"match": {"Context": "'*','" + questionType + "'"}}],
          #"must": [{"match": {"Context": questionType}}],
          #"should": [{"match": {"Context": "'*','" + questionType + "'"}}],
          "should" : should_match
          #"filter": [{"term": {"category": "search"}}]
        }
      }

      #,
      #"aggs" : {
      #  "per_tag": {
      #    "terms": {"field": "tags"},
      #    "aggs": {
      #      "max_lines": {"max": {"field": "lines"}}
      #    }
      #  }
      #}
      
    }
    print(body)
    res = es.search(index = index, doc_type = doc_type, body = body)
    return res["hits"]