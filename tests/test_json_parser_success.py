def test_single_json(json_parse):
    payload = '{"id":"test","score":12,"ip":"1.2.3.4"}'
    response = json_parse(payload)

    assert len(response.json_dicts) == 1
    assert response.json_dicts["test"]["1.2.3.4"] == 1
    assert response.json_dicts["test"]["score"] == 12
    assert str(response) == "\ntest:\n\t1.2.3.4: 1\n\tscore: 12"


def test_many_json_single_id(json_parse):
    payload = """{"id":"test_2","score":5,"ip":"1.2.3.5"}
{"id":"test_2","score":17,"ip":"1.2.3.4"}
{"id":"test_2","score":9,"ip":"1.2.3.4"}"""
    response = json_parse(payload)

    assert len(response.json_dicts) == 1
    assert response.json_dicts["test_2"]["1.2.3.4"] == 2
    assert response.json_dicts["test_2"]["1.2.3.5"] == 1
    assert response.json_dicts["test_2"]["score"] == 31
    assert str(response) == "\ntest_2:\n\t1.2.3.5: 1\n\t1.2.3.4: 2\n\tscore: 31"


def test_many_json_unique_ids(json_parse):
    payload = """{"id":"test_1","score":5,"ip":"1.2.3.5"}
    {"id":"test_2","score":17,"ip":"1.2.3.4"}
    {"id":"test_3","score":9,"ip":"1.2.3.4"}"""
    response = json_parse(payload)

    assert len(response.json_dicts) == 3
    assert response.json_dicts["test_1"]["1.2.3.5"] == 1
    assert response.json_dicts["test_1"]["score"] == 5
    assert response.json_dicts["test_2"]["1.2.3.4"] == 1
    assert response.json_dicts["test_2"]["score"] == 17
    assert response.json_dicts["test_3"]["1.2.3.4"] == 1
    assert response.json_dicts["test_3"]["score"] == 9
    assert str(response) == """
test_1:\n\t1.2.3.5: 1\n\tscore: 5
test_2:\n\t1.2.3.4: 1\n\tscore: 17
test_3:\n\t1.2.3.4: 1\n\tscore: 9"""


def test_json_extra_keys(json_parse):
    payload = """{"id":"test_1","score":5,"ip":"1.2.3.5", "key_list": []}
        {"id":"test_2","score":17,"ip":"1.2.3.4", "key_int": 1234}
        {"id":"test_3","score":9,"ip":"1.2.3.4", "key_1":1, "key_2":"a", "key3":{"n":1}}"""
    response = json_parse(payload)

    assert len(response.json_dicts) == 3
    assert response.json_dicts["test_1"]["1.2.3.5"] == 1
    assert response.json_dicts["test_1"]["score"] == 5
    assert response.json_dicts["test_2"]["1.2.3.4"] == 1
    assert response.json_dicts["test_2"]["score"] == 17
    assert response.json_dicts["test_3"]["1.2.3.4"] == 1
    assert response.json_dicts["test_3"]["score"] == 9
    assert str(response) == """
test_1:\n\t1.2.3.5: 1\n\tscore: 5
test_2:\n\t1.2.3.4: 1\n\tscore: 17
test_3:\n\t1.2.3.4: 1\n\tscore: 9"""
