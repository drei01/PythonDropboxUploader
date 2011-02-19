import os

from dbupload import upload_file
from getpass import getpass

email = raw_input("Enter Dropbox email address:")
password = getpass("Enter Dropbox password:")

path = '/path/to/your/directory'
for file in os.listdir(path):
    if os.path.isfile(os.path.join(path, file)):
        print("found "+os.path.basename(file))
        upload_file(os.path.join(path, file),"/","dbupload_test.txt",email,password)
        print("Uploaded "+os.path.basename(file)+" to dropbox")
