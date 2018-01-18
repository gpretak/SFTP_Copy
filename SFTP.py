import pysftp
# view documentation for pysftp
# http://pysftp.readthedocs.io/en/release_0.2.9/
import resources
import shutil

#Delete any files in director as script cannot overwrite
try:
    shutil.rmtree(resources.remove_folder)
except OSError:
    print("Folder already deleted")
#Connect to sftp
sftp = pysftp.Connection(host=resources.URL_Host_IP, username=resources.Username, password=resources.Password)

#Copy SFTP directory to local directory
sftp.get_r(resources.Folder,resources.replace_folder,preserve_mtime=True)
# Closes the connection
sftp.close()
print("Server files copied")
