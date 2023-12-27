file = open('example_input.txt', 'r')
data = file.readlines()
file.close()

# print(data)

# --- Part one ---

# Max 100,000 folder size

COMMAND = '$'
START_FOLDER = '$ ls\n'
END_FOLDER = '$'
SUB_FOLDER = 'dir'
GO_UP = '$ cd ..\n'


# Find the directories


# folders = {
#     index : int,
#     name : str,
#     child : list[]
#     size : int,
#     total_size : int
# }


# def find_folders(data):
#     i = 0
#     folders = []
#     while i < len(data):
#         path = ''
#         if data[i] == '$ ls\n':
#             folder_name = data[i-1][5:-1]
#             # The line after `$ ls`. The first item in the folder
#             folder_start_index = i + 1
#             subfolders = find_subfolders(folder_start_index, data)
#             # folder_children = find_subfolders(folder_start_index, data)
#             # print("children", folder_children)
#             folders.append([folder_start_index, folder_name, subfolders])
#         i += 1
#     return folders


# directory = {
#     'root': {
#         'subdir1': {
#             'file1.txt': '',
#             'file2.txt': '',
#             'subsubdir1': {
#                 'file3.txt': '',
#             }
#         },
#         'subdir2': {
#             'file4.txt': '',
#             'file5.txt': '',
#         }
#     }
# }


def get_file_directory(data):
    directory = {}
    working_directory = []
    tree = []
    i = 0
    size = 0
    for line in data:
        if line[0] == COMMAND:
            if line == START_FOLDER:
                folder_name = data[i-1][5:-1]
                working_directory += folder_name
                depth = len(working_directory)
                directory.update(
                    {working_directory[-1]: {'name': working_directory[-1]}})
                directory.update(
                    {working_directory[-1]: {'parent': working_directory[depth - 2]}})
                print(working_directory)
                size = 0
            elif line == GO_UP:
                if len(working_directory) >= len(tree):
                    tree.append(working_directory)
                    print('tree', tree)
                working_directory.pop()
                # print(working_directory)
                size = 0
        elif line[:3] == SUB_FOLDER:
            # size = 0
            # directory[working_directory[-1]]
            pass
        else:
            size += int(line.split(' ', 1)[0])
            directory[working_directory[-1]] = size
        i += 1
    print('final tree', tree)
    return directory


# def add_subfolders(directory, data)

    # def find_subfolders(start, data):
    #     if type(start) == list:
    #         return []

    #     sub_folders = []

    #     offset = 0
    #     index = start + offset
    #     while True:
    #         if data[index][0] == END_FOLDER:
    #             break
    #         if data[index][:3] == SUB_FOLDER:
    #             # print(data[start-2], data[index])
    #             sub_folders.append(data[index][4:-1])
    #         offset += 1
    #         index = start + offset
    #         if index >= len(data):
    #             break
    #     return sub_folders

    # def calc_folder_size(folders, data):
    #     for folder in folders:
    #         folder_size = 0
    #         start_index = folder[0]
    #         offset = 0
    #         i = start_index + offset
    #         while data[i][0] != END_FOLDER:
    #             # Main folder
    #             if data[i][0:3] != SUB_FOLDER:
    #                 split = data[i][:-1].split()
    #                 folder_size += int(split[0])
    #                 pass
    #             # Subfolder
    #             # elif data[i][0:3] == SUB_FOLDER:
    #             #     find_subfolders(folder, data)
    #             #     pass
    #             offset += 1
    #             i = start_index + offset
    #             if i >= len(data):
    #                 break
    #         folder.append(folder_size)

    # def calc_total_folder_size(folders, data):
    #     for folder in folders:
    #         total_sum = folder[3]
    #         if len(folder[2]) > 0:
    #             for child in folder[2]:
    #                 i = 0
    #                 while i < len(folders):
    #                     if child in folders[i][1]:
    #                         total_sum += folders[i][3]
    #                         break
    #                     i += 1
    #         # folder.pop()
    #         folder.append(total_sum)
    #     return

    # def filter_size(folders, max):
    #     result = 0
    #     for folder in folders:
    #         if folder[4] <= max:
    #             result += folder[4]
    #     return result
    # folders = find_folders(data)
    # calc_folder_size(folders, data)
    # calc_total_folder_size(folders, data)
    # result = filter_size(folders, 100000)
    # print(folders)
    # print(result)
print(get_file_directory(data))
