"""
1. Read CSV files and returns in-memory object
"""

import os
from datetime import datetime

# ROOTDIR = 'teams_attendance_app/attendace_reports'
# allpaths = []

# def filter_directories(data):
#     name,start,end = data
#     dir_between_dates = []
#     for file in os.listdir(ROOTDIR):
#         file = datetime.strptime(file,'%m%d%Y').strftime('%m/%d/%Y')
#         aux = between_dates(file,start,end) 
#         if(aux):
#             dir_between_dates.append(aux)
               
#     if len(dir_between_dates):
#         filter_files_with_meeting_title(name,dir_between_dates)
        
#     else:
#         print('No meetings found between this dates')
   
#     return dir_between_dates

# def filter_files_with_meeting_title(meeting_title,dir_between_dates):
#     for file in dir_between_dates:
#         path = os.path.join(ROOTDIR,file)
#         files_in_dir(path,meeting_title)

# def files_in_dir(path, meeting_title):
 
#     onlyfiles_csv = [files for files in os.listdir(path) if os.path.isfile(os.path.join(path, files))]
#     for file_csv in onlyfiles_csv:
#         complete_path = os.path.join(path,file_csv)
#         current_list_with_title = read_meeting_title_in_csv_file(complete_path,meeting_title)
#         if(current_list_with_title):
#             add_to_complete_list(current_list_with_title)

# def add_to_complete_list(list_with_title):
#     for path in list_with_title:
#         allpaths.append(path)

def read_meeting_title_in_csv_file(complete_path, meeting_title):
    rows = []
    result = []
    with open(complete_path, 'r', encoding='utf-16') as file:
        next(file)
        for line in file:
            if line != '\n':
                data = line.split("\t")
                rows.append(data)
            else:
                break

    for name,value in rows:
        value = value.strip("\n")
        if value == meeting_title:
            result.append(complete_path)
    
    return result

def check_duplicate_csv_files(paths):
    
    if(len(paths) >= 2):
        for index,numberPath in enumerate(paths):
            print(index,numberPath)

# def between_dates(file_name,start_date,current_date):

#     date = datetime.strptime(file_name,'%m/%d/%Y').date()
#     startdate = datetime.strptime(start_date,'%m/%d/%Y').date()
#     enddate = datetime.strptime(current_date,'%m/%d/%Y').date()
    
#     if startdate <= date  <= enddate:
#         dir_between_dates = date.strftime('%m%d%Y')
#         return dir_between_dates
#     else:
#         return None
   
# def getPaths():
#     return allpaths

# def read_csv_file(complete_path):
#     rows = []
#     with open(complete_path, 'r', encoding='utf-16') as file:
#         next(file)
#         for line in file:
#             if line != '\n':
#                 data = line.split("\t")
#                 rows.append(data)
#             else:
#                 break
#     for name,value in rows:
#         print(value)
        

# def read_csv_file_json():
#     rows = []
#     with open("c:/Users/USER/Jala University/Python-Course/week3_day1/teams_attendance_app/attendace_reports/09162022/meetingAttendanceReport(General).csv", 'r', encoding='utf-16') as file:
#         next(file)
#         for line in file:
#             if line != '\n':
#                 data = line.split("\t")
#                 rows.append(data)
#             else:
#                 break
#     print(rows)
#     rows = json.dumps(rows)
#     print(rows, type(rows))
