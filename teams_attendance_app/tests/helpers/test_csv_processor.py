
TESTPATH = 'teams_attendance_app/attendace_reports/09092022/meetingAttendanceReport(Python training) (1).csv'
TESTTITLE = "Python training"

def read_meeting_title_in_csv_file_test(complete_path, meeting_title):
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
            
    assert len(result), "expected result not empty"

def main():
    read_meeting_title_in_csv_file_test(TESTPATH,TESTTITLE)

main()
