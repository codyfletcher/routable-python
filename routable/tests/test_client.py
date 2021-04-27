from routable import Client


def test_can_instantiate_Client_with_any_string_for_authentication_token():
    authentication_token = "FAKE_AUTHENTICATION_TOKEN"

    client = Client(authentication_token)

    assert client is not None
