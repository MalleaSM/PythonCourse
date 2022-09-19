import os
from utils import get_dir_name
from utils import get_timestamp_string

def create_dir(dir_name):
    os.mkdir(dir_name)


def get_file_name(prefix = "log",extension="txt"):
    """"
    builds filename using prefix string, suffix string (build from datetime) and extension string 
    output is prefix_suffix.extension
    """
    timestamp_string = get_timestamp_string()
    return "{}_{}.{}".format(prefix,timestamp_string,extension)

def write_data_in_file(data,filename,target_path=""):
    """"
    Writes data in filename 
    filename lives in target_path
    """
    #Make sure non_empty target path exists and works
    
    path = validate_path(target_path)
    if(os.path.exists(path)):
        #file = f"{target_path}{filename}"
        with open(os.path.join(path, filename),'w') as logs:
            logs.write(data)
    else:
        create_dir(path)
        write_data_in_file(data,filename,path)

def validate_path(target_path):
    if(target_path == "" or target_path == None):
        target_path = get_dir_name()
        create_dir(target_path)
    
    return target_path
