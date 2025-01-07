# MySQL Workbench Credential Extractor (PoC)

A proof-of-concept script to demonstrate the extraction of stored credentials from MySQL Workbench's user data file.

**DISCLAIMER:** This code is for educational and proof-of-concept purposes only. Unauthorized access to credentials is illegal and unethical. Use responsibly and ethically.

## Motivation

This project was created to explore the security of stored credentials in MySQL Workbench and to demonstrate the potential risks.

## Installation

1.  Clone the repository: `git clone https://github.com/yourusername/mysql-workbench-credentials.git`
2.  Navigate to the project directory: `cd mysql-workbench-credentials`
3.  Create a virtual environment: `python3 -m venv .venv`
4.  Activate the virtual environment:
    *   Linux/macOS: `source .venv/bin/activate`
    *   Windows: `.venv\Scripts\activate`
5.  Install dependencies: `pip install -r requirements.txt`

## Usage

Run the script: `python main.py`

## Example Output

Extracted credentials:
user1
password123
host1

## Limitations

*   This script might not work with future versions of MySQL Workbench if the storage format changes.
*   It relies on the `win32crypt` library, which is Windows-specific.
