from collections import defaultdict

def build_inverted_index(documents):
    inverted_index=defaultdict(list)

    for doc_name,content in documents.items():
        words=content.split()

        for word in words:
            if doc_name not in inverted_index[word]:
                inverted_index[word].append(doc_name)
    
    return inverted_index  