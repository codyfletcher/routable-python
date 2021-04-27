import json


class MockResponse:
    def __init__(self, response_json_str, status_code):
        self.response_json_str = response_json_str
        self.status_code = status_code

    def json(self):
        return json.loads(self.response_json_str)
