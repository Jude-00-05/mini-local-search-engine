# Mini Local Search Engine

A simple search engine built from scratch using Python.

This project demonstrates the core components of a search engine:
- Document Crawling
- Inverted Index Construction
- TF-IDF Ranking
- Query Processing

---

## Features

- Reads local text documents
- Builds an inverted index
- Implements TF-IDF scoring
- Ranks documents based on query relevance
- Interactive CLI-based search interface

---

## Project Structure

mini-local-search-engine/
│
├── documents/
├── crawler.py
├── indexer.py
├── ranker.py
├── main.py

---

## How It Works

1. Crawl: Reads all text files from the documents folder.
2. Index: Builds an inverted index mapping words to documents.
3. Rank: Uses TF-IDF to compute relevance scores.
4. Query: Returns ranked results.

---

## Run the Project

1. Clone the repository:

git clone <your-repo-url>

2. Navigate to the folder:

cd mini-local-search-engine

3. Run:

python main.py

---

## Concepts Used

- Inverted Index
- Term Frequency (TF)
- Inverse Document Frequency (IDF)
- Information Retrieval Basics

---

## Future Improvements

- Stopword removal
- Stemming
- Boolean query support (AND / OR)
- REST API version
- Web-based interface

---

## Author

Alwin Sunny Jude
