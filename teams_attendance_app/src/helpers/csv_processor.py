"""
1. Read CSV files and returns in-memory object
"""

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

