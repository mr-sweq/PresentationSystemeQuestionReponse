from eve import Eve
from flask import Flask, jsonify, make_response, request
import codecs, json
import QuestionToQuery as QtQ
import ESQuery

app = Eve()


def PrepareAnswer(response, indexToShow) :
    if response == None:
        text ={'score': 0, 'sentence': "No document found..."} 
        print(text)
        return [text]
    else:
        print("%d documents found" % response['total'])
        max = len(response['hits'])
        if(max > 3):
            max = 3
        if(max == 0):
            return [{'score':0, 'sentence':'No answer found...'}]
        answer = []
        #for doc in response['hits']:
        for i in range(0, max):
            print("************************************************************************")
            print('Score : ' + str(response['hits'][i]['_score']))
            print(response['hits'][i]['_source'][indexToShow])
            #print(doc['_score'])
            #print(doc['_source']['word'])
            #print(doc['_source']['sentence'])
            #print(doc['_source'][indexToShow])
            print("************************************************************************")
            answer.append({'score':response['hits'][i]['_score'], 'sentence':response['hits'][i]['_source'][indexToShow]})
        return answer

@app.route('/Question', methods=['GET'])
def Question():
    question = request.args.get('Question')
    print('Question received : ' + question)
    qtq = QtQ.QuestionToQuery()

    queryES = qtq.TransformQuestionToESQuery(question)

    response = ESQuery.QueryToES2(queryES, 'sentencener', 'sentencener')

    return jsonify(PrepareAnswer(response, 'sentence'))

if __name__ == '__main__':
    app.run(host="localhost", port="5602")