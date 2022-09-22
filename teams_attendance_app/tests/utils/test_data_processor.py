from src.helpers.data_processor import *

def test_between_dates():
    result = []
    date_to_compare = "09/05/2022"
    start_date = "09/01/2022"
    end_date = "09/10/2022"
    result = between_dates(date_to_compare,start_date,end_date)
    assert len(result), "Result should not be empty"
