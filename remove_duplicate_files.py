import sys
import os
import shutil

kindle_dir = "/media/toannc/Kindle/documents"
local_dir = "/home/toannc/Desktop/Books"


def get_dict_dirs_and_files(top):

    dirs_files = {}
    for root, dirs, files in os.walk(top):
        dirs_files[root.replace(top, "")] = files

    return dirs_files


def mark_duplicate_files(top):
    is_duplicated = {}
    for root, dirs, files in os.walk(top):
        for file in files:
            if file in list(is_duplicated.keys()):
                is_duplicated[file].append(root)
            else:
                is_duplicated[file] = [root]

    return is_duplicated

kindle_subdirs_list = get_dict_dirs_and_files(kindle_dir)
local_subdirs_list = get_dict_dirs_and_files(local_dir)
files_occurances_counter = mark_duplicate_files(kindle_dir)


def have_corresponding_file(root, file, local_subdirs_list):
    _root = root.replace(kindle_dir, "")
    return (_root in list(local_subdirs_list.keys()) and
            file in local_subdirs_list[_root])


select_all = False
for file in files_occurances_counter:
    local_select_all = False
    if len(files_occurances_counter[file]) > 1:  # if duplicated
        for root in files_occurances_counter[file]:
            if not have_corresponding_file(root, file, local_subdirs_list):
                if local_select_all or select_all:
                    print("Remove file {}/{}".format(root, file))
                    os.remove("{}/{}".format(root, file))
                    print(files_occurances_counter[file])
                else:
                    print("Many duplicated files are here...!\n")
                    for file_name in files_occurances_counter[file]:
                        print(file_name + "/" + file)
                    print("\n")
                    print("""Do you want to remove this file {} / {} from Kindle? \n
                    1.Yes\n 2.No\n 3.Remove all local duplicated\n 4.Remove all
                    duplicated\n 0.Exit Program""".format(root, file))
                    while True:
                        select_value = input()
                        if select_value in [str(num) for num in range(0, 5)]:
                            select_value = int(select_value)
                            break
                        else:
                            print("Please input a correct value! [0,1,2,3,4]")
                    if select_value == 1:
                        print("Remove file {}/{}".format(root, file))
                        os.remove(root + '/' + file)
                    elif select_value == 2:
                        print("File {}/{} ignore!".format(root, file))
                    elif select_value == 3:
                        local_select_all = True
                    elif select_value == 4:
                        select_all = True
                    else:
                        sys.exit()

#                sys.exit()
