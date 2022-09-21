"""
1. Genenerates JSON from in-memory object
2. Writes in-memory object into JSON file
"""
from datetime import datetime
from datetime import timedelta
import json

def path_iterator(paths, start, end):
    for path in paths:
        read_csv_file_json(path)


def iteratedates(date,title,start,end,participants,start_time,end_time):
    data_participant = []
    dict_participant = {}
    
    data_time_meeting = []
    dict_time_meeting = {}

    
    date_aux = datetime.strptime(date,'%m/%d/%Y')
    startdate = datetime.strptime(start,'%m/%d/%Y')
    enddate = datetime.strptime(end,'%m/%d/%Y')
    delta = timedelta(days=1)
    startdate = startdate.date()
    enddate = enddate.date()

    while(startdate <= enddate):
        participant_aux = {}
        duration_aux = {}

        participant_aux['date'] = startdate.strftime('%m/%d/%Y')
        duration_aux['date'] = startdate.strftime('%m/%d/%Y')
        
        if(participant_aux['date'] == date_aux.strftime('%m/%d/%Y')):
             participant_aux['participants'] = int(participants)
             duration_aux['duration'] = calculate_time_diff(start_time,end_time)
        else:
            participant_aux['participants'] = -99999
            duration_aux['duration'] = "0h 0m"

        data_participant.append(participant_aux)
        data_time_meeting.append(duration_aux)
        startdate += delta
    
    dict_participant['meeting'] = title
    dict_participant['data'] = data_participant

    dict_time_meeting['meeting'] = title
    dict_time_meeting["data"] = data_time_meeting

    json_data_participant = json.dumps(dict_participant, indent=4)
    json_data_duration = json.dumps(dict_time_meeting, indent=4)
    
    print(json_data_participant)
    print(json_data_duration)
    write_file('participants.json',json_data_participant)
    write_file('meeting_duration.json',json_data_duration)

def read_csv_file_json(path,title,start_date,end_date):
    rows = {}
    with open(path, 'r', encoding='utf-16') as file:
        next(file)
        for line in file:
            if line != '\n':
                data = line.split("\t")
                rows[data[0]] = data[1].strip('\n')
            else:
                break
    get_data_from_file(rows,title,start_date,end_date)


def get_data_from_file(data,title,start_date,end_date):
        participants = data['Total Number of Participants']
        date = data['Meeting Start Time'].split(',')[0]
        start_time = data['Meeting Start Time'].split(',')[1]
        end_time = data['Meeting End Time'].split(',')[1]
        
        iteratedates(date,title,start_date,end_date, participants,start_time,end_time)

def create_json(paths,title,start_date,end_date):
    for path in paths:
        read_csv_file_json(path,title,start_date,end_date)

def write_file(filename,data):
    with open(filename, 'w') as file:
        file.write(data)

def calculate_time_diff(start_time,end_time):
        start_time = start_time.strip(' ')
        start_time = start_time.split(' ')[0]
        start_time = datetime.strptime(start_time, "%H:%M:%S")

        end_time = end_time.strip(' ')
        end_time = end_time.split(' ')[0]
        end_time = datetime.strptime(end_time, "%H:%M:%S")

        delta = end_time - start_time
        return str(delta)

