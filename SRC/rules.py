# rules.py

def validate_choice(choice: str) -> str:
    """
    Decision rule to validate user menu choice.
    Safe default returns "4" and Exits if input is invalid
    """
    valid_choices = ["1", "2", "3", "4"]
    if choice in valid_choices:
        return choice
    else:
        return "4"      # safe default