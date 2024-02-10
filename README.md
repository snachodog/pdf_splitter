# PDF Splitter Script

This Python script automates the process of splitting multi-page PDF files into individual pages and moving all processed files, including original single-page PDFs and newly created split PDFs, into a designated "Processed" folder within the current directory.

## Features

- **PDF Splitting**: Splits multi-page PDFs into separate files, each containing a single page.
- **File Management**: Moves both original and split PDFs to a "Processed" folder to keep your workspace organized.
- **Ease of Use**: Designed to run in the directory containing your PDF files, eliminating the need for complex path configurations.

## Setup

To use this script, you'll need Python installed on your system. The script is compatible with Python 3.6 and above.

### Dependencies

This project relies on the `PyPDF2` library for handling PDF operations. You can install this dependency using pip:

```bash
pip install PyPDF2
```
## Usage

- Clone this repository or download the script to your local machine.
- Place the script in the directory containing your PDF files.
- Open a terminal or command prompt in the same directory.
- Run the script using Python:

 ```bash
  python pdf_splitter.py
```
The script will process all PDF files in the directory, splitting any multi-page documents and moving all files to a new "Processed" folder.

## Contributing
Contributions to improve the script or add new features are welcome. Please feel free to fork the repository and submit pull requests.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
