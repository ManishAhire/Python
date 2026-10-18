import os

# Get current directory
print("\nCurrent Directory: ", os.getcwd())

# Change Directory
os.chdir("/Users/manishahire/Documents/Work/Python/Fundamentals")
print("\nAfter Chaning Directory: ", os.getcwd())

# List Directory
print("\nList Directory: ", os.listdir())

# New Directory
# os.mkdir("NewDirectory")
print("\nDirectory List with Newly Created Directory: ", os.listdir())


# Rename Directory
# os.rename("NewDirectory", "New_Directory")

# Remove File / Directory

# os.remove("test.txt")
os.rmdir("New_Directory")
