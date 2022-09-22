from src.helpers.csv_processor import read_meeting_title_in_csv_file

def test_read_meeting_title_in_csv_file():
    complete_path = 'teams_attendance_app/attendace_reports/09162022/meetingAttendanceReport(Python training) (1).csv'
    meeting_title = "Python training"
    result = read_meeting_title_in_csv_file(complete_path,meeting_title)
    assert len(result), "expected result not empty list"

