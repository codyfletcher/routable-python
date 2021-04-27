from unittest.mock import patch

from routable import Client
from routable.conftest import MockResponse


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