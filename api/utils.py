import os
from api.constants import *


def create_files_zip_dir():
    if not os.path.exists(dir_files_zip):
        os.mkdir(dir_files_zip)
