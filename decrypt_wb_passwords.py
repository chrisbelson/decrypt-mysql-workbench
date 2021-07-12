import os
import win32crypt

## get %appdata% dir ##
appdata = os.getenv('appdata')

## get wb user data ##
try:
    with open(appdata + '/MySQL/Workbench/workbench_user_data.dat', 'rb') as d:
        data = d.read()
except FileNotFoundError:
    print("File does not exist or in use!\n")
    raise 
except:
    raise

## get creds ##
bad_chars = ['\\x02', '\\x03', '\\n', '\\x00']
creds = win32crypt.CryptUnprotectData(data)
for char in bad_chars:
    creds = str(creds).split(char)

## display creds ##
print("Your creds are:")
for cred in creds:
    print(cred.replace('\\', ''))
