""""

"""
from file_helper import write_data_in_file
from file_helper import get_file_name
from rest_client import get_demo_api_data
 
URL='https://python-demo.free.beeceptor.com/my/api/path'
    
def main():
    filename = get_file_name()
    raw_data = get_demo_api_data(URL)
    write_data_in_file(raw_data,filename)
    print("finished")


main()