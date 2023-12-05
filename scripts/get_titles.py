import sys
import re
import os

current_directory = os.getcwd()

parent_directory = os.path.abspath(os.path.join(current_directory, os.pardir))

# Get the list of filenames in the parent directory
files_in_parent = os.listdir(parent_directory+'/topics')

for fileIndex in range(len(files_in_parent)):
    print(f'{fileIndex} <---> {files_in_parent[fileIndex]}')

indexSelection = int(input("\nSelect an option: "))

#if len(sys.argv) <= 1:
#    print("\tFilename must be provided as argument")
#    sys.exit()

#fileName = sys.argv[1]
fileName = parent_directory + '/topics/' + files_in_parent[indexSelection]
print(f'reading {fileName}', end="\n\n")

with open(fileName,"r") as file:
    for title in file:
        if re.search("^##", title):
            plainTitle = re.sub(r'#|\n', '', title).strip()
            link =  plainTitle.replace(' ', '-').lower()
            link =  re.sub(r'\.|\(|\)', '', link)
            tabCount = title.count("#") - 2
            print(f"{'    '*tabCount}- [{plainTitle}](#{link})")