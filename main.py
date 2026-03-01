from crawler import crawl_documents
from indexer import build_inverted_index
from ranker import rank_documents

def main():
    documents = crawl_documents("documents")
    index = build_inverted_index(documents)

    print("Mini Local Search Engine Ready!")
    print("--------------------------------")

    while True:
        query = input("Enter search query (or type 'exit'): ").lower()

        if query == "exit":
            break

        results = rank_documents(query, documents)

        print("\nSearch Results:")
        for doc, score in results:
            print(f"{doc} -> Score: {round(score, 4)}")

        print()

if __name__ == "__main__":
    main()