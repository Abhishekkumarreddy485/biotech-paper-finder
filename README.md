Here’s a professional `README.md` for your **PubMed Papers Project**:

---

```markdown
# PubMed Pharma Article Filter

This project fetches research papers from [PubMed](https://pubmed.ncbi.nlm.nih.gov/) using a user-provided query, filters for articles that have **at least one non-academic author affiliated with pharmaceutical or biotech companies**, and exports the filtered results into a CSV file.

---

## 📁 Project Structure

```

pubmed\_papers\_project/
├── pyproject.toml
├── src/
│   └── pubmed\_papers/
│       ├── **init**.py
│       ├── fetcher.py         # Fetches articles from PubMed API
│       ├── filters.py         # Filters articles with pharma/biotech authors
│       ├── writer.py          # Writes filtered articles to a CSV file
│       └── utils.py           # (Optional: Utility functions, currently empty or can be used for enhancements)
└── test\_fetch.py              # Entry point script to run the pipeline

````

---

## ⚙️ Setup Instructions

1. **Install Poetry** (if not already installed):

   ```bash
   pip install poetry
````

2. **Install dependencies**:

   ```bash
   cd pubmed_papers_project
   poetry install
   ```

3. **Run the program**:

   ```bash
   poetry run python -m pubmed_papers.test_fetch
   ```

   > 💡 If you're on Windows PowerShell, and using user-level install, you might need to run:
   >
   > ```powershell
   > & "$env:USERPROFILE\AppData\Roaming\Python\Scripts\poetry.exe" run python -m pubmed_papers.test_fetch
   > ```

---

## How It Works

1. **Query PubMed**
   The `fetch_pubmed_articles(query, max_results)` function fetches articles from PubMed based on a keyword.

2. **Filter Articles**
   Using `has_pharma_author(article)`, we check if any author in the article has an affiliation related to pharmaceutical or biotech companies.

3. **Export Results**
   The filtered list of articles is written to a CSV file (`filtered_articles.csv`) with detailed author info.

---

## Example Output

The resulting CSV contains:

| PMID | Title | Journal | Date | Author | Affiliation |
| ---- | ----- | ------- | ---- | ------ | ----------- |

---

## Testing

You can modify `test_fetch.py` to change the query or number of results:

```python
query = "cancer therapy"
articles = fetch_pubmed_articles(query, max_results=20)
```

---

## 📌 Notes

* Affiliation filtering is based on keyword matching like `pharma`, `biotech`, `ltd`, etc. Improve accuracy by expanding or fine-tuning the keyword list in `filters.py`.
* The script uses NCBI's E-utilities API (`esearch` and `efetch`) to access PubMed articles.

---

## Future Improvements

* Add more robust keyword matching using regex or NLP.
* Add unit tests and logging.
* Provide a CLI or web interface for user input.
* Support DOI and abstract export.

---

## 🧑‍💻 Author

Made by Abhishek kumar reddy. Feel free to contribute or fork the repo!

---

## License

MIT License – do anything you want, but give credit. 

```

---

Let me know if you want a `requirements.txt` alternative, license file, or want to publish it on GitHub with a proper `pyproject.toml` example.
```
