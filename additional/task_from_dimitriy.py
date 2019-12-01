import os


def get_files_in_template(input_route):
    list_dirs_name = input_route.split('/')  # split dirs in routes
    name_last_dir = list_dirs_name[-1]  # get last dir
    list_files = os.listdir(path=input_route)  # get all files in last_dir
    new_name_dir = [name_last_dir] * len(list_files)  # get length files in last dir

    # print(list_files)
    # for i in zip(new_name_dir, list_files):
    #     print(i)

    dict_files = [{new_name_dir: af} for new_name_dir, af in zip(new_name_dir, list_files)]
    for file_in_directories in dict_files:
        print(file_in_directories)


input_route = "/home/bohdan/Documents/common/flask_advance"  # input your route


if __name__ == "__main__":
    get_files_in_template(input_route)
