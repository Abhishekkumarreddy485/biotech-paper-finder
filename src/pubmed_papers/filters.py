def is_pharma_affiliation(affiliation):
    keywords = ['pharma', 'biotech', 'inc', 'ltd', 'corporation', 'company', 'technologies']
    aff = affiliation.lower()
    return any(keyword in aff for keyword in keywords)

def has_pharma_author(article):
    for author in article["authors"]:
        for aff in author["affiliations"]:
            if is_pharma_affiliation(aff):
                return True
    return False
