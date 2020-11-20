import os
import pysftp

PASSWORD = os.environ["PASSWORD"]
USER = os.environ["USER"]
HOST = os.environ["HOST"]

FILE_NAME = 'sample.csv'

def log_dir(sftp):
    files = sftp.listdir()
    print(files)

with pysftp.Connection(HOST, username=USER, password=PASSWORD) as sftp:

    log_dir(sftp)

    sftp.put(FILE_NAME ,confirm=False)

    log_dir(sftp)

    sftp.remove(FILE_NAME)

    log_dir(sftp)



