import QuestionToQuery as QtQ
import ESQuery


question = "Who is Albert Einstein?"
#query = "Albert Einstein"
#question = "what is trimethylbenzene"
#query = "trimethylbenzene"
#question = "When was the first world war?"
#question = "first world war"
#query = "first world war"
#question = "What is buddhism"
#query = "buddhism"
#question = "Who is Einstein?"
#query = "Einstein"
#question = "Who is the biggest liar ?"
#query = "biggest liar"
#question = "what is deafness?"
#query = "deafness"
#question = "How to mesure your lenght?"
#query = "mesure your lenght"


def ShowAnswer(reponse, indexToShow) :
    if response == None:
        print("No document found...")
    else:
        print("%d documents found" % response['total'])
        max = len(response['hits'])
        if(max > 3):
            max = 3
        
        #for doc in response['hits']:
        for i in range(0, max):
            print("************************************************************************")
            print('Score : ' + str(response['hits'][i]['_score']))
            print(response['hits'][i]['_source'][indexToShow])
            #print(doc['_score'])
            #print(doc['_source']['word'])
            #print(doc['_source']['sentence'])
            #print(doc['_source'][indexToShow])



response = ESQuery.QueryToES(question, 'text', 'text')

ShowAnswer(response, 'sentence')
print("************************************************************************")

qtq = QtQ.QuestionToQuery()

queryES = qtq.TransformQuestionToESQuery(question)

response = ESQuery.QueryToES2(queryES, 'textner', 'textner')

ShowAnswer(response, 'sentence')
print("************************************************************************")

qtq = QtQ.QuestionToQuery()

queryES = qtq.TransformQuestionToESQuery(question)

response = ESQuery.QueryToES2(queryES, 'sentencener', 'sentencener')

ShowAnswer(response, 'sentence')
print("************************************************************************")