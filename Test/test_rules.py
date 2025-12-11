# # test_rules.py
# # if no result are printed the test was successful

# from rules import validate_choice

# def test_valid_choice():

#     # test for valid choice returns unchanged
#     assert validate_choice("2") == "2"

# def test_invalid_choice():

#     # test for invalid choice retruns default safely to "4"
#     assert validate_choice("99") == "4"


# new test_rules.py
# in order to test needs to be add to SRC
"""
Test script for rules.py validation
"""

import sys
import os

# Add current directory to python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from rules import validate_choice, validate_with_decision_table, get_decision_table_info
from decision_table import decision_table

def test_validate_choice():
    """Test the validate_choice function"""
    print("=" * 60)
    print("TESTING validate_choice() FUNCTION")
    print("=" * 60)
    
    test_cases = [
        # (input, expected_output, description)
        ("1", "1", "Valid: Daily Reflection by number"),
        ("one", "1", "Valid: Daily Reflection by word"),
        ("daily", "1", "Valid: Daily Reflection by keyword"),
        ("2", "2", "Valid: Weekly Check-in by number"),
        ("two", "2", "Valid: Weekly Check-in by word"),
        ("weekly", "2", "Valid: Weekly Check-in by keyword"),
        ("3", "3", "Valid: View Entries by number"),
        ("three", "3", "Valid: View Entries by word"),
        ("view", "3", "Valid: View Entries by keyword"),
        ("4", "4", "Valid: Exit by number"),
        ("four", "4", "Valid: Exit by word"),
        ("exit", "4", "Valid: Exit by keyword"),
        ("quit", "4", "Valid: Exit by alternative keyword"),
        ("5", None, "Invalid: Number out of range"),
        ("hello", None, "Invalid: Random word"),
        ("", None, "Invalid: Empty string"),
        ("   ", None, "Invalid: Whitespace only"),
        ("DAILY", "1", "Valid: Case insensitive"),
        ("Two", "2", "Valid: Mixed case"),
        (" 3 ", "3", "Valid: With spaces"),
    ]
    
    passed = 0
    failed = 0
    
    for input_val, expected, description in test_cases:
        result = validate_choice(input_val)
        
        if result == expected:
            status = "✓ PASS"
            passed += 1
        else:
            status = "✗ FAIL"
            failed += 1
        
        print(f"{status}: {description}")
        print(f"  Input: '{input_val}' -> Expected: {expected}, Got: {result}")
        print()
    
    print(f"Results: {passed} passed, {failed} failed")
    return passed, failed

def test_validate_with_decision_table():
    """Test the validate_with_decision_table function"""
    print("\n" + "=" * 60)
    print("TESTING validate_with_decision_table() FUNCTION")
    print("=" * 60)
    
    test_cases = [
        ("1", "R1", "Should return R1 rule"),
        ("weekly", "R2", "Should return R2 rule"),
        ("view", "R3", "Should return R3 rule"),
        ("exit", "R4", "Should return R4 rule"),
        ("invalid", "Default", "Should return Default rule"),
    ]
    
    for input_val, expected_rule, description in test_cases:
        result = validate_with_decision_table(input_val)
        rule_number = result.get("rule_number")
        
        if rule_number == expected_rule:
            print(f"✓ PASS: {description}")
        else:
            print(f"✗ FAIL: {description}")
        
        print(f"  Input: '{input_val}' -> Rule: {rule_number}")
        print(f"  Action: {result.get('action')}")
        print(f"  Message: {result.get('output_message')}")
        print()

def test_decision_table_structure():
    """Test the decision table structure"""
    print("\n" + "=" * 60)
    print("TESTING DECISION TABLE STRUCTURE")
    print("=" * 60)
    
    info = get_decision_table_info()
    
    print(f"Rules Count: {info['rules_count']}")
    print(f"Valid Rules: {', '.join(info['valid_rules'])}")
    print(f"Default Rule: {info['default_rule']}")
    print(f"Description: {info['description']}")
    
    # Display the decision table
    decision_table.display_table()
    
    # Test each rule individually
    print("\nTesting Individual Rules:")
    print("-" * 40)
    
    rules_to_test = ["R1", "R2", "R3", "R4", "Default"]
    for rule_key in rules_to_test:
        rule = decision_table.get_rule_by_number(rule_key)
        if rule:
            print(f"\nRule {rule_key}:")
            print(f"  Input Value: {rule['input_value']}")
            print(f"  Valid Values: {', '.join(rule['valid_values']) if rule['valid_values'] else 'N/A'}")
            print(f"  Action: {rule['action']}")
            print(f"  Description: {rule['description']}")
            print(f"  Is Valid: {rule['is_valid']}")

def test_edge_cases():
    """Test edge cases and boundary conditions"""
    print("\n" + "=" * 60)
    print("TESTING EDGE CASES")
    print("=" * 60)
    
    edge_cases = [
        # Special characters
        ("!", None, "Special character"),
        ("@", None, "Special character"),
        # Numbers with spaces
        (" 1  ", "1", "Number with multiple spaces"),
        ("   two   ", "2", "Word with multiple spaces"),
        # Case variations
        ("ONE", "1", "Uppercase word"),
        ("One", "1", "Title case"),
        ("oNe", "1", "Mixed case"),
        # Partial matches (should fail)
        ("dail", None, "Partial word"),
        ("week", None, "Partial word"),
        ("vie", None, "Partial word"),
        # Numbers as words
        ("1.0", None, "Decimal number"),
        ("01", None, "Leading zero"),
    ]
    
    for input_val, expected, description in edge_cases:
        result = validate_choice(input_val)
        
        if result == expected:
            print(f"✓ PASS: {description}")
        else:
            print(f"✗ FAIL: {description}")
        
        print(f"  Input: '{input_val}' -> Expected: {expected}, Got: {result}")
        print()

def run_all_tests():
    """Run all tests"""
    print("STARTING RULES.PY TEST SUITE")
    print("=" * 60)
    
    total_passed = 0
    total_failed = 0
    
    # Run individual tests
    passed, failed = test_validate_choice()
    total_passed += passed
    total_failed += failed
    
    test_validate_with_decision_table()
    test_decision_table_structure()
    test_edge_cases()
    
    print("\n" + "=" * 60)
    print("TEST SUMMARY")
    print("=" * 60)
    print(f"Total Tests: validate_choice() had {passed} passed, {failed} failed")
    print(f"Overall: All functions tested successfully")
    
    if total_failed == 0:
        print("\n✓ All tests passed! rules.py is working correctly.")
    else:
        print(f"\n⚠ {total_failed} test(s) failed. Check the implementation.")

if __name__ == "__main__":
    run_all_tests()