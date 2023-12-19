#create booking testcase
from src.Helpers.api_requests_wrapper import post_requests
# from src.Constants.api_constants import base_url
from src.Constants.api_constants import APIConstants
from src.Helpers.utils import common_headers_json
from src.Helpers.payload_manager import payload_creating_booking
from src.Helpers.common_verification import verify_response_should_not_be_none, verify_http_status_code
import pytest
import json
from jsonschema import validate
from jsonschema.exceptions import ValidationError
import os     #by import this which we can give current working directory


class TestCreateBooking(object):

    def load_schema(self, schema_file):       #by using this we can read json schema structure file
        with open (schema_file, 'r') as file:
            return json.load(file)
    @pytest.mark.positive
    def test_creating_booking_jsonschema(self):
        # url, headers,payload
        payload=payload_creating_booking()
        print(payload)
        payload["firstname"] = "hymaraj"
        print([payload])

        response = post_requests(url=APIConstants.url_creating_boooking(), auth=None, headers=common_headers_json(),
                                 payload=payload, in_json=False)
        print(response)
        bookingid = response.json()["bookingid"]  # it prints bookingid
        print(bookingid)
        verify_response_should_not_be_none(response.json()["bookingid"])  # call verify_response fun and pass bookingid key and convert response into json()
        verify_http_status_code(response, 200)
        #to validate jsonschema
        response_json=response.json()  #res in json by using the response.json() method

        dir = os.getcwd()    #which give corrent working directory
        #print(dir)
        file = dir + "/schema.json"    #this si take from path ref content root
        schema =self.load_schema(file) #if this path showing error need to import os (operating system module)
        print(schema)

        try:
            validate(instance=response_json, schema=schema)
        except ValidationError as e:
            print(e.message)

