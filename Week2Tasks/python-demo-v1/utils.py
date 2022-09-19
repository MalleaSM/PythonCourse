from datetime import datetime

def get_timestamp_string():
    return datetime.now().strftime("%Y%m%d%H%M%S")

def get_dir_name():
    return datetime.now().strftime("%Y%m%d")