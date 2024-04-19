import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        return response.content
        
    def load_json(self):
        get_list = []
        gets = json.loads(self.get_response_body())
        for get in gets:
            name = get['name']
            occupation = get['occupation']
            get_list.append({'name': name, 'occupation': occupation})
        return get_list
    
    