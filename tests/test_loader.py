"""
Unit tests to ensure the loader file correctly loads and flattens json files
"""

from pathlib import Path
import pytest
from harness.loader import flatten_file

ROOT = Path(__file__).resolve().parent.parent 
AWS_START_LOGGING = (ROOT / "logs" / "aws" / "cloudtrail_logs" / "start_logging.json")
AWS_STOP_LOGGING = (ROOT / "logs" / "aws" / "cloudtrail_logs" / "stop_logging.json")

# Test that it flattens file in logs / aws / cloudtrail_logs / StartLogging.json
def test_flatten_json_keys():
    tmp_dct = flatten_file(AWS_START_LOGGING) 
    assert tmp_dct["eventTime"] == "2026-10-20T12:44:36Z"

# Tested nested key
def test_nested_json_keys():
    my_dict = flatten_file(AWS_STOP_LOGGING) 
    assert my_dict["userIdentity_type"] == "AssumedRole"

# Test number of keys is correct
def test_correct_num_keys():
    num_keys = len(flatten_file(AWS_START_LOGGING).keys())
    assert num_keys == 34