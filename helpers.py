import os
import ast

def bytes_to_dict(data: bytes) -> dict:
    '''
    Converts bytes to a dictionary
    '''
    try:
        dict_str = data.decode("UTF-8")
        return ast.literal_eval(dict_str)
    except:
        return {}

def get_file_location(file_path: str) -> str:
    '''
    Get the file location
    '''
    return '/'.join(file_path.split('/')[:-1])

def get_file_name(file_path: str) -> str:
    '''
    Get the file name
    '''
    return '.'.join(file_path.split('/')[-1].split('.'))

def create_location(server_destination_path: str, file_name:str) -> str:
    '''
    Create the location for the file
    '''
    return server_destination_path + '/' + file_name

def create_path(file_path: str, ext: str):
    '''
    Create the path for the file
    '''
    return os.path.splitext(file_path)[0] + '.' + ext

def remove_file(file_path: str):
    '''
    Remove the file
    '''
    os.remove(file_path)
