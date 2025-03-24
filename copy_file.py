import os
import shutil

source_file = "convert_projector.ai"

# https://github.com/pixijs/pixijs/tree/dev/src/rendering/renderers/gl/context
directories = [
    os.path.join("pixijs", "src","rendering","renderers","gl","context"),
    os.path.join("pixijs", "src","rendering","renderers","gl"),
    os.path.join("pixijs", "src","rendering","renderers"),
    os.path.join("pixijs", "src","rendering"),
    os.path.join("pixijs", "src"),
    os.path.join("pixijs")
]

for dir_path in directories:
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
        print(f"Created directory: {dir_path}")
    else:
        print(f"Directory already exists: {dir_path}")
    
    dest_path = os.path.join(dir_path, source_file)
    shutil.copy2(source_file, dest_path)
    print(f"Copied {source_file} to {dest_path}")

print("All directories created and files copied successfully!")
