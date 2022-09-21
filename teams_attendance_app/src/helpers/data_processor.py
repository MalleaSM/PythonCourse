"""
    Filters in-memory meetings data and uses meeting_name, star_date, end_date, etc...
"""

import os
from datetime import datetime
from helpers.csv_processor import read_meeting_title_in_csv_file

ROOTDIR = 'teams_attendance_app/attendace_reports'
allpaths = []

def filter_directories(data):
    name,start,end = data
    dir_between_dates = []
    for file in os.listdir(ROOTDIR):
        file = datetime.strptime(file,'%m%d%Y').strftime('%m/%d/%Y')
        aux = between_dates(file,start,end) 
        if(aux):
            dir_between_dates.append(aux)
               
    if len(dir_between_dates):
        filter_files_with_meeting_title(name,dir_between_dates)
        
    else:
        print('No meetings found between this dates')
   
    return dir_between_dates

def filter_files_with_meeting_title(meeting_title,dir_between_dates):
    for file in dir_between_dates:
        path = os.path.join(ROOTDIR,file)
        files_in_dir(path,meeting_title)

def files_in_dir(path, meeting_title):
 
    onlyfiles_csv = [files for files in os.listdir(path) if os.path.isfile(os.path.join(path, files))]
    for file_csv in onlyfiles_csv:
        complete_path = os.path.join(path,file_csv)
        current_list_with_title = read_meeting_title_in_csv_file(complete_path,meeting_title)
        if(current_list_with_title):
            add_to_complete_list(current_list_with_title)

def add_to_complete_list(list_with_title):
    for path in list_with_title:
        allpaths.append(path)


def between_dates(file_name,start_date,current_date):

    date = datetime.strptime(file_name,'%m/%d/%Y').date()
    startdate = datetime.strptime(start_date,'%m/%d/%Y').date()
    enddate = datetime.strptime(current_date,'%m/%d/%Y').date()
    
    if startdate <= date  <= enddate:
        dir_between_dates = date.strftime('%m%d%Y')
        return dir_between_dates
    else:
        return None
   
def getPaths():
    return allpaths