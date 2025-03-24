import os
import read_file

def stupid_lookup(project_root, converted_file_path):
    paths = []
    while True:
        paths.insert(0, converted_file_path)
        if project_root and converted_file_path.lower() == project_root.lower():
            break
        parent = os.path.dirname(converted_file_path)
        if parent == converted_file_path:
            break
        read_file.read_file(converted_file_path)
        converted_file_path = parent
    