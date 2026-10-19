"""
This engine using pySigma to take in Sigma rules and run them against test data

Author: Gabe Holmes
"""

from sigma.collection import SigmaCollection
from pathlib import Path
from sigma.validation import SigmaValidator
from sigma.validators.core.metadata import IdentifierExistenceIssue

# Load the test rule from the rules folder. This is a SigmaCollection instance so can iterate through the rule using .rules
# This loads rules in the rules\testing folder
test_collection = SigmaCollection.load_ruleset([Path(".\\rules\\testing")])

for rule in test_collection:
    print(rule.title)