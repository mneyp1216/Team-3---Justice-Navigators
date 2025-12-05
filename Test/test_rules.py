# test_rules.py
# if no result are printed the test was successful

from rules import validate_choice

def test_valid_choice():

    # test for valid choice returns unchanged
    assert validate_choice("2") == "2"

def test_invalid_choice():

    # test for invalid choice retruns default safely to "4"
    assert validate_choice("99") == "4"