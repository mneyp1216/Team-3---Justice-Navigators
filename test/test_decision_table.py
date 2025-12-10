# test_decision_table.py

from src.decision_table import decision_table

def test_decision_table():
    """
    test the decision table with various inputs
    """
    print("Testing Decision Table...")
    print("="*50)

    test_cases = [
        "1", "one", "daily",
        "2", "two", "weekly",
        "3", "three", "view",
        "4", "four", "exit", "quit",
        "5", "hello", "", "  "
    ]

    for test in test_cases:
        rule = decision_table.evaluate(test)
        status = "✓" if rule["is_valid"] else "✗"
        print(f"{status} Input: '{test}' -> Rule: {rule['rule_number']} -> Action: {rule['action']}")

    print(f"\nDecision Table Structure:")
    decision_table.display_table()

# can be called in main() or separately
if __name__ == "__main__":
    test_decision_table()