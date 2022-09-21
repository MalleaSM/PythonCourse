
# sys.path is a list of absolute path strings

## app entry point
from tabnanny import check
from helpers.csv_processor import check_duplicate_csv_files
from helpers.data_processor import getPaths
from helpers.data_processor import filter_directories
from helpers.json_processor import create_json

def process_questions():
    print("What would you like to do?\n 1.start application \n 2.Quit")
    ## display questions menu
    ## drive "question" selection while not Quit
    selected_question = input("choose with the number:\t") # define if string or number or dictionary
    return int(selected_question)

def process_question_options(question):
    ## display input to request meeting name, end and start date
    ## drive "input" aquisition while not Quit

    if question != 2:
        meeting_name = input("Please Enter the METTING TITILE or Q to quit: ")
        if(meeting_name != "Q"): 
            start_date = input("Please enter the start date in format mm/dd/yyyy or Q to quit: ")
            if(start_date != "Q"):
                end_date = input("Please enter the end date in format mm/dd/yyyy or Q to quit: ")
                if(end_date != "Q"):
                    answers = [meeting_name,start_date,end_date]
                    return answers
                else:
                    return
                    
            else:
                return
                
        else:
            return


  # TODO define if string or number or dictionary or tuple

def main():
    question  = process_questions()
    arguments =  process_question_options(question)
    ## TODO: implement bussiness logic
    if(arguments):
        dates_found = filter_directories(arguments)
        paths = getPaths()
        check_duplicate_csv_files(paths)  
        create_json(paths,arguments[0],arguments[1],arguments[2])
    else:
        print("arguments none")
    
main()