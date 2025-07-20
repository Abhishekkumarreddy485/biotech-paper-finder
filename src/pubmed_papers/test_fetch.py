from pubmed_papers.fetcher import fetch_pubmed_articles
from pubmed_papers.filters import has_pharma_author
from pubmed_papers.writer import write_articles_to_csv

def main():
    query = "cancer therapy"
    articles = fetch_pubmed_articles(query, max_results=20)
    pharma_articles = [a for a in articles if has_pharma_author(a)]

    print(f"Found {len(pharma_articles)} articles with pharma/biotech authors.")
    write_articles_to_csv(pharma_articles)
    print("Saved to filtered_articles.csv")

if __name__ == "__main__":
    main()
