import jsonfixer
import unittest
import json
class TestFixJson(unittest.TestCase):

    def test_fix_json_by_rule_based(self):
        error_cases = [
            ("missing_bracket", "[1, 2, 3", list),
            ("missing_quote", '{"school": "台灣大}', dict),
            ("trailing_comma", "[1, 2, ]", list),
            ("extra_comma", '{"school":"台灣大學",}', dict),
            ("extra_comma", '{"school":"台灣大學","department":"資訊工程",}', dict),
            # fail
            # ("invalid_value", '{"age": 101a2}', dict),
            # ("invalid_key", '{test1: "value"}', dict),
        ]
        for error_type, json_str, expected_type in error_cases:
            repaired_str = jsonfixer.JsonRepair(json_str).repair()
            repaired_json_dict = json.loads(repaired_str)
            self.assertTrue(
                isinstance(repaired_json_dict, expected_type), "rule-based 修復 json 功能"
            )
