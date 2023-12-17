#common headers
def common_headers_json():
    headers = {
        "Content-Type":"application/json",
    }
    return headers

def common_headers_for_put_delete_patch():
    headers = {
        "Content-Type":"application/json",
        "Authorization":"Basic YWRtaW46cGFzc3dvcmQxMjM=",
    }
    return headers

def common_headers_xml():
    headers = {
        "Content-Type":"application/xml",
    }
    return headers

#if Read data from Excel, csv, json, YAML---keep these common function here in future
