def read_file(filename: str):
    return [file_read for file_read in open(filename, 'r', encoding='utf-8')]

def write_in_file(filename: str, telephones: set):

    with open(filename, 'w', encoding='utf-8') as appendInFile:
        appendInFile.writelines(telephones)
        