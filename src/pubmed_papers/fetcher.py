import requests
import xml.etree.ElementTree as ET

def fetch_pubmed_articles(query, max_results=10):
    base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"
    
    # Step 1: Get PubMed IDs (PMIDs)
    search_url = f"{base_url}esearch.fcgi?db=pubmed&term={query}&retmode=json&retmax={max_results}"
    search_response = requests.get(search_url).json()
    pmids = search_response['esearchresult']['idlist']
    
    # Step 2: Fetch article details
    fetch_url = f"{base_url}efetch.fcgi?db=pubmed&id={','.join(pmids)}&retmode=xml"
    fetch_response = requests.get(fetch_url)
    
    root = ET.fromstring(fetch_response.content)
    articles = []

    for article in root.findall(".//PubmedArticle"):
        pmid = article.findtext(".//PMID")
        title = article.findtext(".//ArticleTitle")
        journal = article.findtext(".//Journal/Title")
        pub_date = article.findtext(".//PubDate/Year") or "Unknown"
        
        authors_data = []
        for author in article.findall(".//Author"):
            last = author.findtext("LastName") or ""
            fore = author.findtext("ForeName") or ""
            name = f"{fore} {last}".strip()
            affils = [aff.text for aff in author.findall(".//AffiliationInfo/Affiliation") if aff is not None]
            authors_data.append({"name": name, "affiliations": affils})

        articles.append({
            "pmid": pmid,
            "title": title,
            "journal": journal,
            "pub_date": pub_date,
            "authors": authors_data
        })

    return articles
