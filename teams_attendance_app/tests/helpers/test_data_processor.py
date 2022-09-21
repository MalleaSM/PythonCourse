from datetime import datetime

def between_dates(date_to_compare,start_date,current_date):
    dir_between_dates = []
    date = datetime.strptime(date_to_compare,'%m/%d/%Y').date()
    startdate = datetime.strptime(start_date,'%m/%d/%Y').date()
    enddate = datetime.strptime(current_date,'%m/%d/%Y').date()
    
    if startdate <= date  <= enddate:
        dir_between_dates = date.strftime('%m%d%Y')
   
    assert len(dir_between_dates), "dir_between_dates should not be empty"

def main():
    between_dates("09/05/2022","09/01/2022","09/10/2022")
main()