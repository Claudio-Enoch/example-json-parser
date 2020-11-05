import json

from json.decoder import JSONDecodeError

from json_parser.parsed_model import ParsedModel


def json_parser(json_objects: str) -> ParsedModel:
    """
    Accepts a string of JSON objects separated by new lines.
    JSON objects require an id, ip, and score keys.
    For each unique ID field, print it's respective IP and the number of times it appeared.
    Also, sum the scores for that ID.
    Example input:
    {"id":"t1","score":1,"ip":"1.2.3.4","message":"Hello"}
    {"id":"t1","score":5,"ip":"1.2.3.5"}
    {"id":"t1","score":1,"ip":"1.2.3.4"}
    {"id":"t2","score":3,"ip":"1.2.3.4"}
    Example output:
    t1:
        1.2.3.5: 1
        1.2.3.4: 2
        score: 7
    t2:
        1.2.3.4: 1
        score: 3
    """
    if not isinstance(json_objects, str):
        raise TypeError("Please submit a string containing newline delimited JSON")

    # create a parsing obj to handle logic for aggregating json values
    model = ParsedModel()

    # pass each json payload into the model
    for obj in json_objects.split("\n"):
        try:
            _json = json.loads(obj)
        except JSONDecodeError:  # handle malformed json and return a comprehensible msg
            raise ValueError(f"Invalid json found in: {obj}")
        model.add_dict(_json)  # validates json data
    print(model)
    return model

