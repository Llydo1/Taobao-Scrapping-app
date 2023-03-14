import json

def get_cookie_list_from_cookie_json(path_to_cookie_json: str):
    cookie_list: list = []
    with open(path_to_cookie_json, 'r') as f:
        cookie_json = json.load(f)
    for cookie in cookie_json:
        cookie_list.append({"name": cookie["name"], "value":cookie["value"]})
    return cookie_list
    

with open('/home/llydo1/projects/samsidu/Taobao-Scrapping-app/Backend/Data/decrypted_cookie.json', 'w') as f:
    json.dump(get_cookie_list_from_cookie_json("/home/llydo1/projects/samsidu/Taobao-Scrapping-app/Backend/Data/encrypted_cookie.json")
, f)