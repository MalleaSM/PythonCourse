import requests
import logging

def get_demo_api_data(URL):
    #GET DATA FROM REST API ENDPOINT
    response = requests.get(URL)

    #checks if response was successfull
    if response.status_code !=200:
        get_error_logging_message(response.status_code)
        return

    #for this case response is text in other contexts response should be .json
    return response.text

def get_error_logging_message(code):
    logging.basicConfig(filename='log.info', level=logging.WARNING, format="%(asctime)s - %(levelname)s - %(message)s")
    logging.error(f"CODE - {code} -  CONECTING TO API CODE")