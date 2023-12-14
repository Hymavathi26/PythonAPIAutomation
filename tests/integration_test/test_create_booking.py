# create nmunber functions with number of testcases
# def test_creating_booking_tc1():
#     pass
# def test_creating_booking_tc2():
#     pass
# def test_creating_booking_tc3():
#     pass

# we can use class also instead of using functions

from src.Helpers.api_requests_wrapper import post_requests
# from src.Constants.api_constants import base_url
from src.Constants.api_constants import APIConstants
from src.Helpers.utils import common_headers_json
from src.Helpers.payload_manager import payload_creating_booking
from src.Helpers.common_verification import verify_response_should_not_be_none, verify_http_status_code
import pytest
import json


class TestCreateBooking(object):
    @pytest.mark.positive
    def test_creating_booking_tc1(self):
        # url, headers,payload
        response = post_requests(url=APIConstants.url_creating_boooking(), auth=None, headers=common_headers_json(),
                                 payload=payload_creating_booking(), in_json=False)
        print(response)
        bookingid = response.json()["bookingid"]  # it prints bookingid
        print(bookingid)
        verify_response_should_not_be_none(response.json()["bookingid"])  # call verify_response fun and pass bookingid key and convert response into json()
        verify_http_status_code(response, 200)
    @pytest.mark.neative
    def test_creating_booking_tc2(self):
        # url, headers,payload
        response = post_requests(url=APIConstants.url_creating_boooking(), auth=None, headers=common_headers_json(),
                                 payload={}, in_json=False)
        verify_http_status_code(response, 500)