from Data.data_files import DataFiles

def get_file_data(file_path:DataFiles):
    with open(file_path, 'r') as file:
        data = file.read()
        return data
