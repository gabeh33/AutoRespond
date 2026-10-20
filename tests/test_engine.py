"""
Unit tests to ensure pySigma continues to work as expected when loading new rules
"""

from pathlib import Path
import pytest
from harness.engine import load_rules

ROOT = Path(__file__).resolve().parent.parent 
TEST_RULES = (ROOT / "rules" / "testing")

# Loading rules
def test_can_load_rules():
    test_rules = load_rules(TEST_RULES)
    assert len(test_rules.rules) > 0

# Test that the titles are loaded correctly
def test_can_load_titles():
    test_rules = load_rules(TEST_RULES)
    titles = [rule.title for rule in test_rules]
    assert "Okta User Account Locked Out" in titles

# Test that a filenotfound error is raised when it should be
def test_missing_folder_raise():
    with pytest.raises(FileNotFoundError):
        load_rules(ROOT / "does_not_exist")