import time
import os 


dir_files = "generated_files"
dir_images = "images"
dir_zip = "zip"
dir_files_zip = os.path.join(dir_files,dir_zip)
dir_files_images = os.path.join(dir_files, dir_images)




# variable to have date in file name
timestr = time.strftime("%Y%m%d-%H%M%S")
