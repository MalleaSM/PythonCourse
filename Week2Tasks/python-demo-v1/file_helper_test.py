from file_helper import validate_path
from utils import get_dir_name

def if_path_None_returns_dir_name():
    result = validate_path(None)
    print(result)
    assert result == get_dir_name(), "Expected dir name to be datetime format yyyymmdd"

def if_path_empty_returns_dir_name():
    result = validate_path("")
    print(result)
    assert result == get_dir_name(), "Expected dir name to be datetime format yyyymmdd"

def main():
    if_path_None_returns_dir_name()
    if_path_empty_returns_dir_name()

main()