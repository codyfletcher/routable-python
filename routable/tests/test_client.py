import json
from unittest.mock import patch

import pytest

from routable import Client


class Test__Client__instantiation:
    def test_can_instantiate_Client_with_any_string_for_authentication_token(self):
        authentication_token = "FAKE_AUTHENTICATION_TOKEN"

        client = Client(authentication_token)

        assert client is not None


    def test_can_not_instantiate_Client_without_authentication_token__raises_TypeError(self):
        with pytest.raises(TypeError):
            _ = Client()

    def test_default_headers(self):
        client = Client("FAKE_AUTHENTICATION_TOKEN")

        expected_default_headers = {
            'Authorization': 'Bearer FAKE_AUTHENTICATION_TOKEN',
            'Accept': 'application/vnd.api+json',
            'Content-Type': 'application/vnd.api+json'
        }
        assert expected_default_headers == client.headers


class MockResponse:
    def __init__(self, response_json_str, status_code):
        self.response_json_str = response_json_str
        self.status_code = status_code

    def json(self):
        return json.loads(self.response_json_str)


class Test__Client__membership:
    def test__membership_list__returns_a_list_of_dict(self):
        client = Client("FAKE_AUTHENTICATION_TOKEN")
        dummy_response_json_string = """{
          "links": {
            "first": "https://api.sandbox.routable.com/memberships/",
            "last": "https://api.sandbox.routable.com/memberships/?page%5Bnumber%5D=1",
            "next": null,
            "prev": null
          },
          "data": [
            {
              "type": "Membership",
              "id": "660640d3-82e0-43a2-ac8a-071d63c15f54",
              "attributes": {
                "avatar": null,
                "email": "michelle@fedex.com",
                "first_name": "Michelle",
                "is_approver": true,
                "is_disabled": false,
                "last_name": "Jones"
              }
            }
          ],
          "meta": {
            "pagination": {
              "page": 1,
              "pages": 1,
              "count": 1,
              "page_size": 25
            }
          }
        }"""

        with patch('routable.list_resource.requests.get') as mock_get:
            mock_get.side_effect = lambda *args, **kwargs: MockResponse(dummy_response_json_string, 200)
            sut = client.memberships.list()

            expected = [
                {
                    "type": "Membership",
                    "id": "660640d3-82e0-43a2-ac8a-071d63c15f54",
                    "attributes": {
                        "avatar": None,
                        "email": "michelle@fedex.com",
                        "first_name": "Michelle",
                        "is_approver": True,
                        "is_disabled": False,
                        "last_name": "Jones"
                    }
                }
            ]
            assert expected == sut
