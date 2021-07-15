import os


# Global Variables
titleEntries = []
titleEntriesString = " "
archivePath = "/home/bromteque/tstest"

# Get list of files
entries = os.listdir(archivePath)

# Create or open file
if os.path.exists("./archive.txt"):
    print("File found. Opening.")
    archiveFile = open("archive.txt", "wt")
else:
    print("File not found, creating file.")
    archiveFile = open("archive.txt", "xt")

# Get title
for entry in entries:
    hyphenIndex = entry.rfind("-")
    titleEntries.append("\n" + entry[:hyphenIndex])

# Remove newline from first title
titleEntries[0] = titleEntries[0].replace("\n", "")

# Merge list into string
for title in titleEntries:
    titleEntriesString += title

# Strip leading whitespace
titleEntriesString = titleEntriesString.lstrip()

# Write to file
archiveFile.write(titleEntriesString)
