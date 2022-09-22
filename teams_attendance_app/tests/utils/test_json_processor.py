from src.helpers.json_processor import calculate_time_diff

def test_calculate_time_diff():
    start_time = " 8:28:10 AM"
    end_time = "  10:09:18 AM"
    result = calculate_time_diff(start_time,end_time)
    assert(result != ""),"Result shouldnt be empty"


    