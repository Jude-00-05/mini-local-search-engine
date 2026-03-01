import math
from collections import Counter

def compute_tf(word,documents):
    words=documents.split()
    word_count=Counter(words)

    return word_count[word]/len(words)


def compute_idf(word,documents):
    total_docs=len(documents)
    docs_with_word=sum(1 for doc in documents.values() if word in doc.split())

    return math.log(total_docs/(1+docs_with_word))

def rank_documents(query,documents):
    scores={}

    query_words=query.split()

    for doc_name,content in documents.items():

        score=0
        
        for word in query_words:
            tf=compute_tf(word,content)
            idf=compute_idf(word,documents)
            score+=tf+idf

        scores[doc_name]=score
    return sorted(scores.items(),key=lambda x:x[1],reverse=True)


