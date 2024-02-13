import requests
from pybtex.database.input import bibtex

def find_doi_for_entry(title):
    """Search CrossRef for a DOI given an article title."""
    url = "https://api.crossref.org/works"
    params = {"query.title": title, "rows": 1}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        results = response.json()
        items = results.get("message", {}).get("items", [])
        if items:
            return items[0].get("DOI")
    return None

def append_doi_to_bibtex(bib_file_path):
    """Parse a BibTeX file and append missing DOIs."""
    parser = bibtex.Parser()
    bib_data = parser.parse_file(bib_file_path)
    
    for entry in bib_data.entries.values():
        if 'doi' not in entry.fields:
            title = entry.fields.get('title')
            if title:
                doi = find_doi_for_entry(title)
                if doi:
                    entry.fields['doi'] = doi
                    print(f"Found DOI for '{title}': {doi}")
                else:
                    print(f"No DOI found for '{title}'")
            else:
                print("No title found for an entry, skipping...")
        else:
            print(f"Entry '{entry.fields.get('title')}' already has a DOI.")

    # Optionally, you can save the updated BibTeX to a new file
    bib_data.to_file('updated_lib.bib')

# Replace 'your_bibtex_file.bib' with the path to your BibTeX file
bib_file_path = 'your_bibtex_file.bib'
append_doi_to_bibtex('Lib.bib')
