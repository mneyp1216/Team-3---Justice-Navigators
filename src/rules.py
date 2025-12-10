# rules.py
"""
Validation rules for the Journal Companion program with CLI flag support
"""

import sys
import argparse
from decision_table import decision_table
from mood_assessment import assess_mood, display_mood_scale

def validate_choice(choice):
    """
    Validate user menu choice using Decision Table
    Args:
        choice (str): User's input choice
    Returns:
        str or None: Validated choice or None if invalid
    """
    if not choice:
        return None
    
    # Use decision table to evaluate the choice
    rule = decision_table.evaluate(choice)
    
    # If rule is valid, return the corresponding number
    if rule["is_valid"] and rule["rule_number"] != "Default":
        # Map back to the standard number for backward compatibility
        if rule["rule_number"] == "R1":
            return "1"
        elif rule["rule_number"] == "R2":
            return "2"
        elif rule["rule_number"] == "R3":
            return "3"
        elif rule["rule_number"] == "R4":
            return "4"
    
    # Invalid choice (Default rule)
    return None


def parse_cli_args():
    """
    Parse command line arguments with flags
    """
    parser = argparse.ArgumentParser(
        description="Journal Companion - A reflective journaling application",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python journal_app.py --help                 # Show this help message
  python journal_app.py --mood "high"          # Start with mood assessment
  python journal_app.py --version              # Show version info
  python journal_app.py --show-scale           # Display mood scale
        
For more information, see the README.md file.
        """
    )
    
    parser.add_argument(
        "--mood", "-m",
        type=str,
        help="Start with mood assessment (1-5 or keywords: critical, low, mid, high, indifferent)"
    )
    
    parser.add_argument(
        "--show-scale", "-s",
        action="store_true",
        help="Display mood assessment scale and exit"
    )
    
    parser.add_argument(
        "--version", "-v",
        action="store_true",
        help="Show version information and exit"
    )
    
    parser.add_argument(
        "--test", "-t",
        action="store_true",
        help="Run unit tests and exit"
    )
    
    return parser.parse_args()


def process_cli_args(args):
    """
    Process command line arguments
    """
    results = {}
    
    # Handle --version flag
    if args.version:
        results['action'] = 'version'
        return results
    
    # Handle --show-scale flag
    if args.show_scale:
        results['action'] = 'show_scale'
        return results
    
    # Handle --test flag
    if args.test:
        results['action'] = 'test'
        return results
    
    # Handle --mood flag
    if args.mood:
        mood_result = assess_mood(args.mood)
        if mood_result:
            results['mood'] = mood_result
            results['action'] = 'continue'
        else:
            print(f"Invalid mood value: {args.mood}")
            print("Valid values: 1-5 or keywords like 'critical', 'low', 'mid', 'high', 'indifferent'")
            results['action'] = 'exit'
    else:
        results['action'] = 'continue'
    
    return results