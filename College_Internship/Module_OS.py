import os

#get current working directory
print("Current working directory:", os.getcwd())
print()

#list all files and directories in the current directory in list manner
print("Files and directories in current directory:", os.listdir())
print()


#create a new directory
os.mkdir("new_directory")
print("Created new directory")
print()


#change the current working directory
os.chdir("new_directory")
print("Changed working directory to:", os.getcwd())
print()


#remove a directory
os.chdir("..")  # Change back to the parent directory
print()



#check if a file or directory exists
file_path = "new_directory"
if os.path.exists(file_path):
    print(f"{file_path} exists.")
else:
    print(f"{file_path} does not exist.")
print()


#delete a directory
os.rmdir("new_directory")
print("Deleted the directory 'new_directory' if it existed.")
print()

#list all files and directories in the current directory again
print("Files and directories in current directory after deletion:", os.listdir())