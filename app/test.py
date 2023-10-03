import os

path = "C:\\top_folder2\\top_folder\\sub_folder\\file.txt"
parts = os.path.normpath(path).split(os.sep)
sub_folder = parts[-2] if len(parts) > 1 else None
print(sub_folder)  # Output: sub_folder
