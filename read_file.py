import os
from pathlib import Path

FILE_NAME = "convert_projector.ai"

def read_file(file_path):
   path = Path(file_path)
   ai_file = path / FILE_NAME
   try:
      with open(ai_file, 'r', encoding='utf-8') as f:
         content = f.read().strip()
   except Exception as e:
         print(e)
