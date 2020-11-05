import pytest


@pytest.mark.parametrize("payload, missing_key", [
    ('{"score":12,"ip":"1.2.3.4"}', "id"),
    ('{"id":"test","ip":"1.2.3.4"}', "score"),
    ('{"id": "test", "score": 12}', "ip")
])
def test_missing_key(json_parse, payload, missing_key):
    with pytest.raises(KeyError, match=f"missing keys: {{'{missing_key}'}}"):
        json_parse(payload)


@pytest.mark.parametrize("payload", [
    12345,
    {"id": "test_id", "score": 12, "ip": "1.2.3.4"},
    [1, 2, 3, 4]
])
def test_input_type_not_string(json_parse, payload):
    with pytest.raises(TypeError, match="Please submit a string containing newline delimited JSON"):
        json_parse(payload)


def test_empty_string(json_parse):
    with pytest.raises(ValueError, match=f"Invalid json found in:"):
        json_parse("")


def test_malformed_json(json_parse):
    payload = '{"id": "test_2", "score": 17, "ip": "1.2.3.4"'  # missing close bracket
    with pytest.raises(ValueError, match=f"Invalid json found in:"):
        json_parse(payload)


@pytest.mark.parametrize("payload, error_subset", [
    ('{"id": 123, "score": 17, "ip": "1.2.3.4"}', "id must be a string"),
    ('{"id": "test_1", "score": "5", "ip": "1.2.3.4"}', "score must be an int"),
    ('{"id": "test_2", "score": 17, "ip": "127.0.0,1"}', "improper IPV4 format for ip"),
])
def test_key_validations(json_parse, payload, error_subset):
    with pytest.raises(ValueError, match=error_subset):
        json_parse(payload)
