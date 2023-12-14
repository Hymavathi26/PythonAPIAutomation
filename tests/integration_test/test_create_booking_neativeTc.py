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
                                 payload={}, in_json=False)
        print(response)
        verify_http_status_code(response, 500)

    def test_creating_booking_tc2(self):
        # url, headers,payload
        response = post_requests(url=APIConstants.url_creating_boooking(), auth=None, headers=common_headers_json(),
                                 payload={"firstname":"admin"}, in_json=False)
        print(response)
        verify_http_status_code(response, 500)

    def test_creating_booking_tc3(self):
        # url, headers,payload
        response = post_requests(url=APIConstants.url_creating_boooking(), auth=None, headers=common_headers_json(),
                                 payload={None}, in_json=False)
        print(response)
        verify_http_status_code(response, 400)

    def test_creating_booking_tc4(self):
        # url, headers,payload
        response = post_requests(url=APIConstants.url_creating_boooking(), auth=None, headers=common_headers_json(),
                                 payload={"This is text"}, in_json=False)
        print(response)
        verify_http_status_code(response, 500)