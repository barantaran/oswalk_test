import os
from pathlib import Path
import read_file

def oswalk_lookup(project_root, converted_file_path):
   for parent, dirs, files in os.walk(project_root, topdown=False):
      if read_file.FILE_NAME in files:
         if Path(converted_file_path).is_relative_to(parent):
            read_file.read_file(converted_file_path)