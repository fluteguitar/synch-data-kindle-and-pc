import os
import shutil

kindle_dir = "/media/toannc/Kindle/documents"
local_dir = "/home/toannc/Desktop/Books"

def get_dict_dirs_and_files(top):

    dirs_files = {}
    for root, dirs, files in os.walk(top):
        dirs_files[root.replace(top, "")] = files
        
    return dirs_files
        
kindle_subdirs_list = get_dict_dirs_and_files(kindle_dir)
local_subdirs_list = get_dict_dirs_and_files(local_dir)

for subdir in local_subdirs_list.keys():
#    print "begin>"+subdir+"<end", type(subdir), subdir not in kindle_subdirs_list.keys()
    if subdir not in kindle_subdirs_list.keys():
        print("Create new directory {}{}".format(kindle_dir , subdir))
        shutil.copytree(local_dir + subdir, kindle_dir + subdir)
    else:
        for book_name in local_subdirs_list[subdir]:
            if book_name not in kindle_subdirs_list[subdir]:
                print("Copy {} from {}{} to {}{}".format(book_name, local_dir, subdir, kindle_dir, subdir))
                shutil.copy2("{}{}/{}".format(local_dir, subdir, book_name), "{}{}".format(kindle_dir, subdir))
