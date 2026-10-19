"""
This engine using pySigma to take in Sigma rules and run them against test data

Author: Gabe Holmes
"""

from sigma.collection import SigmaCollection
from pathlib import Path
from sigma.validation import SigmaValidator
from sigma.validators.core.metadata import IdentifierExistenceIssue

# Anchor the root of the repo to the AutoRespond/ folder
ROOT = Path(__file__).resolve().parent.parent 
TEST_RULES = (ROOT / "rules" / "testing")

def load_rules(folder: Path) -> SigmaCollection:
    """ Given a Path for a load the Sigma rules in that folder. Returns a SigmaCollection"""
    if not folder.is_dir():
        raise FileNotFoundError(f"Could not find folder: {folder}")
    return SigmaCollection.load_ruleset([folder])

if __name__ == "__main__":
    tests = load_rules(TEST_RULES)
    for rule in tests.rules:
        print(rule.title)
