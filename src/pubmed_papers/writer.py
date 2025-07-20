import csv

def write_articles_to_csv(articles, filename="filtered_articles.csv"):
    with open(filename, mode="w", newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["PMID", "Title", "Journal", "Date", "Author", "Affiliation"])

        for article in articles:
            for author in article["authors"]:
                for aff in author["affiliations"]:
                    writer.writerow([
                        article["pmid"],
                        article["title"],
                        article["journal"],
                        article["pub_date"],
                        author["name"],
                        aff
                    ])
