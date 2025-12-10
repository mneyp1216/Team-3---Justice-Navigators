# quick_test.py
"""
Quick interactive test for rules.py
"""

from src.rules import validate_choice

def quick_test():
    print("Quick Test for validate_choice()")
    print("Type 'quit' to exit")
    print("-" * 40)
    
    while True:
        user_input = input("\nEnter a test value: ").strip()
        
        if user_input.lower() == 'quit':
            break
        
        result = validate_choice(user_input)
        
        if result:
            print(f"✓ VALID: '{user_input}' -> returns '{result}'")
            
            # Map result to action
            actions = {
                "1": "Daily Reflection",
                "2": "Weekly Check-in",
                "3": "View Entries",
                "4": "Exit Program"
            }
            print(f"  Action: {actions.get(result, 'Unknown')}")
        else:
            print(f"✗ INVALID: '{user_input}' -> returns {result}")

if __name__ == "__main__":
    quick_test()