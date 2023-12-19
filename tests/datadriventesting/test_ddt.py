# Read the CSV or EXCEL file
# write data into excel file(create function create_token which can take values from the excel file)
# Verify the expected result

import requests
import pytest
from src.Constants.api_constants import APIConstants
from src.Helpers.utils import common_headers_json
# read the csv file or excel file---openpyxl
import openpyxl


# step1--read the file and put the content into a [] array or set
def read_the_credential_from_excel(file_path):
    # how to read file by using openpyxl
    credentials = []
    workbook = openpyxl.load_workbook(file_path)  # take excel file path
    sheet = workbook.active  # take active excel sheet

    for row in sheet.iter_rows(min_rows=2, values_only=True):  #row start from 2 row in and values_only not formatting just given nomal values
        username, password = row
        credentials.append({"username": username, "password": password})
        return credentials


def make_request_auth(username, password):
    payload = {
        "username": username,
        "password": password
    }
    response = requests.post(APIConstants.url_create_token(), headers=common_headers_json(),
                             json=payload)  # payload we can import here bez payload will chane dynamically
    return response


def test_post_create_token():  # this will use for#make make requests multiple time
    # make_requsts_auth--->Run this function for --Row that we have in excel
    file_path = "test_ddt.py    "
    credentials = read_the_credential_from_excel(file_path)

    for user_cred in credentials:
        username = user_cred["username"]
        password = user_cred["password"]
        print(username, password)
        response = make_request_auth(username, password)
        print(response)
        #here we can write the logic for neative and positive 