import os

def renameFiles():
    # 1. Get file name from a folder
    file_list = os.listdir(r"/Users/Kevin/Desktop/python_projects/secret_message/prank")
    print (file_list)
    saved_path = os.getcwd()

    os.chdir(r"/Users/Kevin/Desktop/python_projects/secret_message/prank")

    # 2. For each file, rename file
    for file_name in file_list:
        os.rename(file_name, file_name.translate(None,'0123456789'))
    os.chdir(saved_path)


renameFiles()
