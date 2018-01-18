import pysftp
# view documentation for pysftp
# http://pysftp.readthedocs.io/en/release_0.2.9/
import resources
import shutil

#Delete any files in directory as script cannot overwrite
try:
    shutil.rmtree(resources.remove_folder)
except OSError:
    print("Folder already deleted")
    
#Connect to sftp
sftp = pysftp.Connection(host=resources.url_host, username=resources.username, password=resources.password)

#Copy SFTP directory to local directory
sftp.get_r(resources.folder,resources.replace_folder,preserve_mtime=True)
# Closes the connection
sftp.close()
print("Server files copied")
