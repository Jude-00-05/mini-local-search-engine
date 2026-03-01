from crawler import crawl_documents
from indexer import build_inverted_index
from ranker import rank_documents

documents=crawl_documents("documents")

index= build_inverted_index(documents)

print("Search Engine Ready! Type your query (or 'exit' to quit):")


while True:
    query=input("Enter your query").lower()

    if query=="exit":
        break

    results=rank_documents(query,documents)
    print("Search Results:")

    for doc,score in results:
        print(f"{doc} (Score: {score:.4f})")
