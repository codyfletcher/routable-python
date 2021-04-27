import pytest

from routable import Client


def test_can_instantiate_Client_with_any_string_for_authentication_token():
    authentication_token = "FAKE_AUTHENTICATION_TOKEN"

    client = Client(authentication_token)

    assert client is not None


def test_can_not_instantiate_Client_without_authentication_token__raises_TypeError():
    with pytest.raises(TypeError):
        _ = Client()


def test__membership_list():
    client = Client("FAKE_AUTHENTICATION_TOKEN")
    dummy_response = """{
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

    sut = client.memberships.list()

    expected_memberships = [
        {
            "type": "Membership",
            "id": "660640d3-82e0-43a2-ac8a-071d63c15f54",
            "attributes": {
                "email": "michelle@fedex.com",
                "first_name": "Michelle",
                "last_name": "Jones",
                "is_approver": True,
                "is_disabled": False,
                "avatar": None,
            }
        }
    ]
    assert expected_memberships == sut
