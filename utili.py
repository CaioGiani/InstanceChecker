import os

def list_files(directory):
    image_name_list = []
    for file in os.listdir(directory):
        if file.endswith('.jpg') or file.endswith('.png') or file.endswith('.jpeg'):
            image_name_list.append(file)
    return image_name_list

def MapLabelToImage(directory,):
    