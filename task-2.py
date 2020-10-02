
import os

files_list = ['1.txt',
              '2.txt',
              '3.txt',
              '4.txt']


def lines_num_dict():
    """
    this function builds a dict with keys from files names and values from numbers of strings
    """
    files_dict = dict.fromkeys(files_list)
    for file in files_list:
        file_path = os.path.join(os.getcwd(), file)
        with open(file_path) as f:
            files_dict[file] = len(f.readlines())
    return files_dict


lines_num_dict()


def make_result_file():
    with open('file.txt', 'w') as result:
        a = sorted(lines_num_dict().items(), key=lambda x: x[1], reverse=True)
        for item in a:
            result.write(item[0])
            result.write('\n')
            result.write(str(item[1]))
            result.write('\n')
            with open(os.path.join(os.getcwd(), item[0])) as from_read:
                for line in from_read:
                    result.write(line)
            result.write('\n')


make_result_file()
