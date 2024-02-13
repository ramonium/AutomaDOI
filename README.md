
# BibTeX DOI Finder

This Python script automatically searches for and appends Digital Object Identifiers (DOIs) to entries in a BibTeX file that lack them. It utilizes the CrossRef API to query DOIs based on article titles, enhancing the completeness of bibliographic references.

## Features

- Parses BibTeX files to identify entries without DOIs.
- Queries the CrossRef API using titles of entries to find corresponding DOIs.
- Appends found DOIs to the BibTeX entries.
- Saves the updated BibTeX file with DOIs included.

## Prerequisites

Before running this script, ensure you have the following installed:

- Python 3.x
- `requests` library
- `pybtex` library

## Installation

1. **Clone the Repository**

   ```sh
   git clone https://github.com/yourusername/bibtex-doi-finder.git
   cd bibtex-doi-finder
   ```

2. **Install Required Python Libraries**

   Run the following command to install the necessary Python libraries:

   ```sh
   pip install requests pybtex
   ```

## Usage

1. **Prepare Your BibTeX File**

   Ensure your BibTeX file is ready and located in an accessible directory.

2. **Edit the Script**

   Open `doi_finder.py` in a text editor and replace `'your_bibtex_file.bib'` with the path to your BibTeX file.

3. **Run the Script**

   Execute the script from the command line:

   ```sh
   python doi_finder.py
   ```

   The script will process each entry in your BibTeX file, search for missing DOIs, and print the results. If a DOI is found, it will be appended to the entry. The script saves an updated version of your BibTeX file named `updated_lib.bib`.

## Contributing

Contributions to improve the script or address issues are welcome. Please feel free to fork the repository, make changes, and submit pull requests.

## License

This project is open-sourced under the [MIT License](LICENSE.md).

## Acknowledgments

- Thanks to CrossRef for providing the API used to query DOIs.
