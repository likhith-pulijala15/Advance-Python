import json
FILE = "data.json"

# ---------- WRITE ----------
data = {
    "name": "Likhith",
    "age": 21,
    "skills": ["Python", "Django"]
}

with open(FILE, "w") as f:
    json.dump(data, f, indent=4)

print("Initial data written")

# ---------- READ ----------
with open(FILE, "r") as f:
    data = json.load(f)

print("Read data:", data)

# ---------- UPDATE ----------
data["age"] = 22
data["skills"].append("React")

with open(FILE, "w") as f:
    json.dump(data, f, indent=4)

print("Updated data written")

# ---------- READ AGAIN ----------
with open(FILE, "r") as f:
    updated_data = json.load(f)

print("Final data:", updated_data)





# --------------- os Module -----------------
import os

#Current working directory
print(os.getcwd()) #get current directory
os.chdir() #change directory

#Lists files and folders
print(os.listdir())              # current directory
os.listdir("my_folder")   # specific folder

# Create directories
os.mkdir("test")          # single folder
os.makedirs("a/b/c")      # nested folders

# Walk through directories
for root, dirs, files in os.walk("."):
    print(root, dirs, files)

# Rename files or folders
os.rename("old.txt", "new.txt")

# Remove files or folders
os.remove("file.txt")     # delete file
os.rmdir("folder")        # delete empty folder
os.removedirs("a/b/c")    # delete nested empty folders

# Environment variables
os.environ["API_KEY"] = "12345"
print(os.getenv("API_KEY"))