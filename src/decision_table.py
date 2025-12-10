# decision_table.py
"""
Decision Table for Journal Companion Program
Implements decision table with >= 4 rows plus Default row
PR Reference: Implements feature request #42 - Mood Assessment Integration
Issue: https://github.com/mneyp1216/journal-companion/issues/42
Decision Table Documentation: See README.md "Rule Behavior" section
"""

from colorama import Fore, Style

class DecisionTable:
    """
    Decision Table implementation for menu choices
    
    DECISION TABLE STRUCTURE:
    ==================================================================
    | Rule # | Input         | Valid Values        | Action          |
    ==================================================================
    | R1     | "1"           | 1, one, daily       | Daily Reflection|
    | R2     | "2"           | 2, two, weekly      | Weekly Check-in |
    | R3     | "3"           | 3, three, view      | View Entries    |
    | R4     | "4"           | 4, four, exit, quit | Exit Program    |
    | Default| Other         | Invalid             | Show Error      |
    ==================================================================
    
    PR Reference: #42 - Mood Assessment Integration
    Links to Decision Table: See class documentation above
    """
    
    def __init__(self):
        # Define the decision table rules (4 valid rules + 1 default rule)
        self.rules = {
            "R1": {
                "rule_number": "R1",
                "input_value": "1",
                "valid_values": ["1", "one", "daily"],
                "action": "daily_reflection",
                "description": "Start daily reflection process with mood assessment",
                "output_message": "Starting Daily Reflection with mood assessment...",
                "is_valid": True
            },
            "R2": {
                "rule_number": "R2",
                "input_value": "2",
                "valid_values": ["2", "two", "weekly"],
                "action": "weekly_checkin",
                "description": "Start weekly check-in process",
                "output_message": "Starting Weekly Check-in...",
                "is_valid": True
            },
            "R3": {
                "rule_number": "R3",
                "input_value": "3",
                "valid_values": ["3", "three", "view"],
                "action": "view_entries",
                "description": "View previous journal entries",
                "output_message": "Displaying previous entries...",
                "is_valid": True
            },
            "R4": {
                "rule_number": "R4",
                "input_value": "4",
                "valid_values": ["4", "four", "exit", "quit"],
                "action": "exit_program",
                "description": "Exit the program gracefully",
                "output_message": "Exiting program...",
                "is_valid": True
            },
            "Default": {
                "rule_number": "Default",
                "input_value": "any other value",
                "valid_values": [],
                "action": "show_error",
                "description": "Invalid input - show error message and increment error count",
                "output_message": "Invalid selection! Please try again.",
                "is_valid": False
            }
        }
    
    def evaluate(self, user_input):
        """
        Evaluate user input against decision table
        Args:
            user_input (str): User's menu choice
        Returns:
            dict: Matching rule information
            
        Decision Table Logic:
        ---------------------------------------------------------------
        | Condition                          | Action                 |
        ---------------------------------------------------------------
        | user_input in R1.valid_values      | Return R1 rule         |
        | user_input in R2.valid_values      | Return R2 rule         |
        | user_input in R3.valid_values      | Return R3 rule         |
        | user_input in R4.valid_values      | Return R4 rule         |
        | Otherwise (Default)                | Return Default rule    |
        ---------------------------------------------------------------
        """
        # GUARD CLAUSE: Check if input is None or empty
        if user_input is None:
            return self.rules["Default"]
        
        # Normalize input: convert to lowercase and strip whitespace
        normalized_input = str(user_input).strip().lower()
        
        # Check if input is empty after normalization
        if not normalized_input:
            return self.rules["Default"]
        
        # Check each valid rule (R1, R2, R3, R4)
        for rule_key in ["R1", "R2", "R3", "R4"]:
            rule = self.rules[rule_key]
            if normalized_input in rule["valid_values"]:
                return rule
        
        # If no match found, return Default rule
        return self.rules["Default"]
    
    def get_rule_by_number(self, rule_number):
        """
        Get specific rule by rule number
        Args:
            rule_number (str): Rule number (R1, R2, R3, R4, Default)
        Returns:
            dict: Rule information or None if not found
        """
        return self.rules.get(rule_number)
    
    def get_all_rules(self):
        """
        Return all rules in the decision table
        
        Returns:
            dict: All rules including Default
        """
        return self.rules
    
    def display_table(self):
        """
        Display the decision table in a readable format
        
        This shows the complete decision table structure as specified in requirements.
        """
        print(f"\n{Fore.CYAN}{'='*80}")
        print(f"DECISION TABLE - Journal Companion Program")
        print(f"PR Reference: #42 - Mood Assessment Integration")
        print(f"{'='*80}")
        print(f"{'Rule':<8} | {'Input':<15} | {'Valid Values':<30} | {'Action':<20}")
        print(f"{'-'*8}-|-{'-'*15}-|-{'-'*30}-|-{'-'*20}")
        
        # Display all 5 rows (4 valid + 1 default)
        for rule_key in ["R1", "R2", "R3", "R4", "Default"]:
            rule = self.rules[rule_key]
            valid_values_str = ", ".join(rule["valid_values"]) if rule["valid_values"] else "N/A (any other)"
            print(f"{rule['rule_number']:<8} | {rule['input_value']:<15} | {valid_values_str:<30} | {rule['action']:<20}")
        
        print(f"{'='*80}{Style.RESET_ALL}\n")
    
    def get_valid_choices(self):
        """
        Return list of all valid input choices
        
        Returns:
            list: All valid input values from R1-R4
        """
        valid_choices = []
        for rule_key in ["R1", "R2", "R3", "R4"]:
            rule = self.rules[rule_key]
            valid_choices.extend(rule["valid_values"])
        return valid_choices
    
    def get_decision_table_summary(self):
        """
        Get summary of decision table for documentation
        Returns:
            dict: Summary information
        """
        return {
            "total_rules": len(self.rules),
            "valid_rules": ["R1", "R2", "R3", "R4"],
            "default_rule": "Default",
            "pr_reference": "#42 - Mood Assessment Integration",
            "issue_link": "https://github.com/your-username/journal-companion/issues/42",
            "valid_inputs_count": len(self.get_valid_choices()),
            "description": "Decision table with 4 valid rules and 1 default rule"
        }
    
    def is_valid_choice(self, user_input):
        """
        Check if user input is a valid choice
        Args:
            user_input (str): Input to check
        Returns:
            bool: True if valid, False if invalid (Default rule)
        """
        rule = self.evaluate(user_input)
        return rule["is_valid"]
    
    def get_action_for_input(self, user_input):
        """
        Get the action for a given input
        Args:
            user_input (str): User input
        Returns:
            str: Action name or "show_error" for invalid inputs
        """
        rule = self.evaluate(user_input)
        return rule["action"]


def create_test_decision_table():
    """
    Create a test instance of DecisionTable for unit testing
    Returns:
        DecisionTable: Test instance
    """
    return DecisionTable()


def test_decision_table_logic():
    """
    Test function to verify decision table logic
    This demonstrates all 4 valid rules plus default rule
    """
    table = DecisionTable()
    
    print(f"{Fore.YELLOW}Testing Decision Table Logic{Style.RESET_ALL}")
    print(f"{'-'*60}")
    
    test_cases = [
        # Valid inputs for R1
        ("1", "R1", True, "Daily Reflection"),
        ("one", "R1", True, "Daily Reflection"),
        ("daily", "R1", True, "Daily Reflection"),
        
        # Valid inputs for R2
        ("2", "R2", True, "Weekly Check-in"),
        ("two", "R2", True, "Weekly Check-in"),
        ("weekly", "R2", True, "Weekly Check-in"),
        
        # Valid inputs for R3
        ("3", "R3", True, "View Entries"),
        ("three", "R3", True, "View Entries"),
        ("view", "R3", True, "View Entries"),
        
        # Valid inputs for R4
        ("4", "R4", True, "Exit Program"),
        ("four", "R4", True, "Exit Program"),
        ("exit", "R4", True, "Exit Program"),
        ("quit", "R4", True, "Exit Program"),
        
        # Default rule cases (invalid inputs)
        ("5", "Default", False, "Show Error"),
        ("hello", "Default", False, "Show Error"),
        ("", "Default", False, "Show Error"),
        ("   ", "Default", False, "Show Error"),
        (None, "Default", False, "Show Error"),
    ]
    
    passed = 0
    failed = 0
    
    for input_val, expected_rule, expected_valid, description in test_cases:
        rule = table.evaluate(input_val)
        
        if rule["rule_number"] == expected_rule and rule["is_valid"] == expected_valid:
            print(f"✓ PASS: '{input_val}' -> {rule['rule_number']} ({description})")
            passed += 1
        else:
            print(f"✗ FAIL: '{input_val}' -> Expected: {expected_rule}, Got: {rule['rule_number']}")
            failed += 1
    
    print(f"\n{Fore.CYAN}Test Results:{Style.RESET_ALL}")
    print(f"Passed: {passed}")
    print(f"Failed: {failed}")
    print(f"Total: {passed + failed}")
    
    # Display the decision table
    table.display_table()
    
    return passed, failed


# Create a global instance for easy import
decision_table = DecisionTable()

if __name__ == "__main__":
    """
    Run decision table tests when executed directly
    This demonstrates the 4+1 rule structure
    """
    print(f"{Fore.GREEN}Decision Table Module Test{Style.RESET_ALL}")
    print(f"{'='*60}")
    
    # Test the decision table logic
    passed, failed = test_decision_table_logic()
    
    # Display decision table summary
    summary = decision_table.get_decision_table_summary()
    print(f"\n{Fore.CYAN}Decision Table Summary:{Style.RESET_ALL}")
    print(f"Total Rules: {summary['total_rules']} (4 valid + 1 default)")
    print(f"Valid Rules: {', '.join(summary['valid_rules'])}")
    print(f"Default Rule: {summary['default_rule']}")
    print(f"PR Reference: {summary['pr_reference']}")
    print(f"Issue Link: {summary['issue_link']}")
    print(f"Valid Inputs: {summary['valid_inputs_count']} unique values")
    
    if failed == 0:
        print(f"\n{Fore.GREEN}✓ All decision table tests passed!{Style.RESET_ALL}")
    else:
        print(f"\n{Fore.RED}✗ {failed} test(s) failed{Style.RESET_ALL}")