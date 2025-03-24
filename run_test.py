import find_stupid_implementation
import find_oswalk 
import time_logger
import os
from pathlib import Path

project_root = "."
converted_file_path = "pixijs/node_modules/yaml/dist/compose"

project_root = os.path.normpath(project_root)
converted_file_path = os.path.normpath(converted_file_path)

start = time_logger.start_time()
find_stupid_implementation.stupid_lookup(project_root, converted_file_path)
print("Stupid implementation:")
time_logger.stop_time(start)

print("\n")

start = time_logger.start_time()
find_oswalk.oswalk_lookup(project_root, converted_file_path)
print("Oswalk:")
time_logger.stop_time(start)
