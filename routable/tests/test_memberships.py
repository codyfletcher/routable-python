from unittest.mock import patch

import pytest_check as check

from routable import Client
from routable.conftest import MockResponse


class Test_Memberships:
    def test__memberships_list__returns_a_list_of_Membership(self):
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
              "id": "abc123",
              "attributes": {
                "avatar": "https://host/image.png",
                "email": "email@host",
                "first_name": "first",
                "is_approver": true,
                "is_disabled": false,
                "last_name": "last"
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

            first_membership = sut[0]
            check.equal("abc123", first_membership.id)
            check.equal("email@host", first_membership.email)
            check.equal("first", first_membership.first_name)
            check.equal("last", first_membership.last_name)
            check.equal("https://host/image.png", first_membership.avatar)
            check.is_true(first_membership.is_approver)
            check.is_false(first_membership.is_disabled)
