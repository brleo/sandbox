import os

folder = "common/csv/"

files = []

for path in os.listdir(folder):
    if os.path.isfile(os.path.join(folder, path)):
        files.append(path)

print(files)