import socket

from typing import Dict


class ParsedModel:
    """
    Model to store a dictionary of IDs and their corresponding stats:
    {
    "id_one":
        {
        "1.2.3.5" : 2, # count of ip per id
        "1.2.8.4" : 1,
        score: 12
        },
    "id_two":
        {
        "1.1.1.1" : 3,
        "1.2.8.4" : 2,
        score: 20
        }, ...
    }
    """

    def __init__(self):
        self.json_dicts: Dict[str, dict] = {}

    def add_dict(self, _json: dict):
        """Parse json and add to json_dicts"""
        required_keys = {"id", "score", "ip"}
        if keys := required_keys - set(_json):
            raise KeyError(f"in {_json}:\n\tmissing keys: {keys}")

        self._validate(_json)

        # append key values to our dictionary of json_dicts
        self.json_dicts[_json["id"]] = self.json_dicts.get(_json["id"], {})
        self.json_dicts[_json["id"]][_json["ip"]] = self.json_dicts[_json["id"]].get(_json["ip"], 0) + 1
        self.json_dicts[_json["id"]]["score"] = self.json_dicts[_json["id"]].get("score", 0) + _json["score"]

    @staticmethod
    def _validate(_json: dict):
        """
        id: string
        score: int
        ip: IPV4
        """
        if not isinstance(_json["id"], str):
            raise ValueError(f"in {_json}:\n\tid must be a string: {_json['id']}")
        if not isinstance(_json["score"], int):
            raise ValueError(f"in {_json}:\n\tscore must be an int: {_json['score']}")
        try:
            socket.inet_aton(_json["ip"])
        except socket.error:
            raise ValueError(f"in {_json}:\n\timproper IPV4 format for ip: {_json['ip']}")

    def __str__(self):
        """
        Returns easily read representation
        id_one:
            1.2.3.6: 3
            1.2.3.5: 2
            score: 12
        id_two:
            1.2.3.5: 1
            score: 1
        """
        response = ""
        for _id, values in self.json_dicts.items():
            response += f"\n{_id}:"
            for k, v in values.items():
                if k != "score":
                    response += f"\n\t{k}: {v}"  # IP_ADDRESS: IP_COUNT
            response += f"\n\tscore: {values['score']}"
        return response
