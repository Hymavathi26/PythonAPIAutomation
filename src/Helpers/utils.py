#common headers
def common_headers_json():
    headers = {
        "Content-Type":"application/json",
    }
    return headers


def common_headers_xml():
    headers = {
        "Content-Type":"application/xml",
    }
    return headers

#if Read data from Excel, csv, json, YAML---keep these common function here in future
