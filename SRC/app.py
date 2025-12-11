# journal_app.py
import justice_navigator_info
import pandas as pd
import numpy as np
import os
import datetime
from colorama import init, Fore, Back, Style      # type: ignore   
import colorama                                   # type: ignore
from rules import validate_choice, parse_cli_args, process_cli_args
from decision_table import decision_table
from mood_assessment import assess_mood, display_mood_scale

init(autoreset=True)

# Add version constant
__version__ = "1.1.0"

def welcome_message():
    """introduction to journal"""
    print(f"\n{'='*14} Welcome to your Journal Companion {'='*15}\n")
    print(f"This is a private space to reflect on your journey.")
    print(f"All entries will be securely saved on your device.")
    print(f"Take your time, there's no rush.\n")

def initial_mood_assessment():
    """
    Assess user's mood immediately upon opening the application
    Returns the mood assessment result
    """
    print(f"\n{Fore.CYAN}{'='*20} INITIAL MOOD CHECK-IN {'='*20}\n")
    print(f"{'='*64}{Style.RESET_ALL}")
    print(f"\nBefore we begin, let's check in with how you're feeling right now.")
    print(f"This helps us understand your starting point.\n")
    
    print(display_mood_scale())
    
    while True:
        mood_input = input(f"\n{Fore.GREEN}How are you feeling as you open the journal today? (1-5 or keyword): ").strip()
        mood_result = assess_mood(mood_input)
        
        if mood_result:
            print(f"\n{Fore.GREEN}✓ Initial mood recorded: {mood_result['description']}{Style.RESET_ALL}")
            
            # Provide appropriate response based on mood level
            if mood_result['level'] in [1, 2]:      # Critical or Low
                print(f"\n{Fore.CYAN}Thank you for sharing that. Remember, this is a safe space.")
                print(f"We'll take this at your pace.{Style.RESET_ALL}")
            elif mood_result['level'] == 3:         # Mid
                print(f"\n{Fore.CYAN}Thanks for checking in. Let's explore your day together.{Style.RESET_ALL}")
            elif mood_result['level'] in [4, 5]:    # High or Indifferent
                print(f"\n{Fore.CYAN}Great to hear! Let's capture this moment.{Style.RESET_ALL}\n")
            
            return mood_result
        else:
            print(f"{Fore.RED}Invalid mood input. Please use 1-5 or a keyword from the scale above.{Style.RESET_ALL}")

def user_info():
    """capture basic information from user"""
    print(f"As we begin this journey, let's get to know you ...")

    # capture user name with validation
    while True:
        name = input("What is your first name, or what would like to be addressed as? ").strip()
        if name:
            break
        else:
            print(f"Please enter you name to continue.")

    # date capture for time stamps/ updated to an auto timestamp
    start_date = datetime.datetime.now().strftime("%m/%d/%Y")

    return name, start_date

def daily_reflection(name, initial_mood=None):
    """guide user through daily reflection with mood assessment"""
    print(f"\n Hello {name}, let's reflect on today...")

    # record date and time
    current_date = datetime.datetime.now().strftime("%m/%d/%Y")
    current_time = datetime.datetime.now().strftime("%I:%M %p")

    print(f"\nToday's Date: {current_date}")
    print(f"Current Time: {current_time}")
    
    # MOOD ASSESSMENT INTEGRATION - Show initial mood from start of session
    if initial_mood:
        print(f"\n{Fore.CYAN}Initial Mood (from start of session):")
        print(f"{Fore.YELLOW}{initial_mood['description']}{Style.RESET_ALL}")
        
        # Check if mood has changed
        print(f"\n{Fore.CYAN}Has your mood changed since you started?")
        print(display_mood_scale())
    else:
        print(f"\n{Fore.CYAN}Let's check in with your current mood...")
        print(display_mood_scale())
    
    while True:
        mood_input = input(f"\n{Fore.GREEN}How are you feeling right now? (1-5 or keyword): ").strip()
        current_mood = assess_mood(mood_input)
        
        if current_mood:
            # Compare with initial mood if available
            if initial_mood:
                if current_mood['level'] < initial_mood['level']:
                    print(f"\n{Fore.GREEN}✓ Mood recorded: {current_mood['description']}")
                    print(f"{Fore.CYAN}I notice you're feeling a bit lower than when we started.")
                    print(f"That's okay - let's explore what's coming up.{Style.RESET_ALL}")
                elif current_mood['level'] > initial_mood['level']:
                    print(f"\n{Fore.GREEN}✓ Mood recorded: {current_mood['description']}")
                    print(f"{Fore.CYAN}Great to see an improvement! Let's build on this.{Style.RESET_ALL}")
                else:
                    print(f"\n{Fore.GREEN}✓ Mood recorded: {current_mood['description']}")
                    print(f"{Fore.CYAN}Your mood has remained steady.{Style.RESET_ALL}")
            else:
                print(f"\n{Fore.GREEN}✓ Mood recorded: {current_mood['description']}{Style.RESET_ALL}")
            break
        else:
            print(f"{Fore.RED}Invalid mood input. Please use 1-5 or a keyword from the scale.{Style.RESET_ALL}")

    # need to evaluate the daily questions with team, these are possible examples
    daily_questions = [
        "What's a positive thing that happened today?",
        "What made the day challenging, and how did you handle it?",
        "Did you connect with anyone today, how was that experience?",
        "What did you learn about yourself today?",
        "Is there is something that you are looking forward to tomorrow?",
        "What would you do differently tomorrow? ",
        "How are you feeling at this moment? (use 1-5 words)"
    ]

    # blank space for response
    answers = []

    for e, question in enumerate(daily_questions, 1):
        print(f"\n{e}. {question}")
        answer = input("Let me hear your thoughts: ")
        answers.append(answer)

        # user control to skip questions
        if e < len(daily_questions):
            skip = input("\nPress ENTER to continue or type 'SKIP' to finish: ")
            if skip.lower() == 'skip':
                # if SKIP, fill in the rest of the questions with "Skipped"
                for s in range(e, len(daily_questions)):
                    answers.append("Skipped")
                break

    return current_date, current_time, answers, current_mood

def weekly_check_in(name):
    """Weekly checkin with deeper questions"""
    print(f"\n{name}, let's check-in...")

    weekly_questions = [
        "What do you feel was your biggest accomplishment this week? ",
        "What do you feel was the most challenging this week? ",
        "What support do you need right now? ",
        "What is one goal you would like to set for next week? ",
        "How have you grown of changed this week? "
    ]

    answers = []
    current_date = datetime.datetime.now().strftime("%m/%d/%Y")

    for e, question in enumerate(weekly_questions, 1):
        print(f"\n{e}. {question}")
        answer = input("Your response: ")
        answers.append(answer)

         # user control to skip questions
        if e < len(weekly_questions):
            skip = input("\nPress ENTER to continue or type 'SKIP' to finish: ")
            if skip.lower() == 'skip':
                # if SKIP, fill in the rest of the questions with "Skipped"
                for s in range(e, len(weekly_questions)):
                    answers.append("Skipped")
                break

    return current_date, answers

def save_entry(entry_type, date, time, content, name, mood=None, initial_mood=None):
    """Create file for Journal Entries"""
    filename = f"{name}_journal.txt"

    with open(filename, "a") as file:
        file.write(f"\n{'='*64}\n")
        file.write(f"Entry Type: {entry_type}\n")
        file.write(f"Date: {date} | Time: {time}\n")
        if initial_mood:
            file.write(f"Initial Mood: {initial_mood['description']}\n")
        if mood:
            file.write(f"Current Mood: {mood['description']}\n")
            if initial_mood:
                mood_change = mood['level'] - initial_mood['level']
                if mood_change > 0:
                    file.write(f"Mood Change: Improved by {mood_change} level(s)\n")
                elif mood_change < 0:
                    file.write(f"Mood Change: Decreased by {abs(mood_change)} level(s)\n")
                else:
                    file.write(f"Mood Change: Remained steady\n")
        file.write(f"{'='*64}\n")

        if entry_type == "Daily Reflection":
            daily_questions = [
                "Positive moment: ",
                "Challenge handled: ",
                "Connections: ",
                "Self-discovery: ",
                "Looking forward: ",
                "Do differently: ",
                "Current feelings: "
            ]

            for e, (question, answer) in enumerate(zip(daily_questions, content)):
                file.write(f"{question}{answer}\n")

        elif entry_type == "Weekly Check-in":
            weekly_questions = [
                "Biggest accomplishment: ",
                "Most challenging: ",
                "Support needed: ",
                "Goal for next week: ",
                "Personal goal: "
            ]

            for e, (question, answer) in enumerate(zip(weekly_questions, content)):
                file.write(f"{question}{answer}\n")
    
    print(f"\n{Fore.GREEN}√ Your entry has been saved to {filename}")

def view_previous_entries(name):
    """Review previous journal entries"""
    filename = f"{name}_journal.txt"

    if os.path.exists(filename):
        print(f"\nHere are your previous journal entries, {name}:\n")
        with open(filename, "r") as file:
            print(file.read())
    else:
        print(f"\nUnfortunately you have not saved a file yet. Your Journal is ready to listen when you are ready to say.")

def main():
    """Main program function with CLI support"""
    
    # Parse command line arguments
    args = parse_cli_args()
    cli_results = process_cli_args(args)
    
    # Handle CLI actions
    if cli_results['action'] == 'version':
        print(f"Journal Companion v{__version__}")
        print("Created with care for reflective practice")
        return
    
    if cli_results['action'] == 'show_scale':
        print(display_mood_scale())
        return
    
    if cli_results['action'] == 'test':
        print("Running unit tests...")
        # You can call test runner here
        return
    
    if cli_results['action'] == 'exit':
        return
    
    # Store command line mood if provided
    cli_mood = cli_results.get('mood', None)
    
    # 1. FIRST: Assess initial mood (unless provided via CLI)
    if cli_mood:
        initial_mood = cli_mood
        print(f"\n{Fore.CYAN}Initial mood from command line: {initial_mood['description']}{Style.RESET_ALL}\n")
    else:
        initial_mood = initial_mood_assessment()
    
    # 2. Show welcome message
    welcome_message()

    # 3. Gather user information 
    name, date = user_info()

    # 4. Personalization of welcome
    print(f"\nWelcome, {name}! I am glad you are here.")
    print(f"Keep in mind, this is your journey - we'll take it one day at a time.")

    # counter for invalid numbers when on the dashboard.
    invalid_count = 0

    while True:
        print(f"\n{Fore.CYAN}{'='*64}\n")
        print(f"Hello {name}! What would you like to do? ")
        print(f"\n{'='*64}\n")

        # integrated decision table - display valid choices
        print(f"[1, 'one', 'daily']            - Start a Daily Reflection")
        print(f"[2, 'two', 'weekly']           - Complete Weekly Check-in")
        print(f"[3, 'three', 'view']           - View Previous Entries")
        print(f"[4, 'four', 'exit', 'quit']    - Exit the Program")
        print(f"\n{'-'*64}{Style.RESET_ALL}")

        choice = input("\n Please select (1-4): ").strip()

        # use decision table to evaluate choice
        rule = decision_table.evaluate(choice)

        # check if choice is invalid (Default rule)
        if rule["rule_number"] == "Default":
            print(f"\n{Fore.RED}{'='*20} Invalid Selection {'='*21}\n")
            print(f"'{choice}' is not a valid option.")
            print(f"Please choose one of the options shown above {Style.RESET_ALL}")
            invalid_count += 1

            # check if too many invalid attempts
            if invalid_count >= 3:
                print(f"\n{Fore.RED}Too many invalid attempts ({invalid_count}/3).")
                print(f"The program will now exit to prevent misuse.")
                print(f"Please restart when you're ready.{Style.RESET_ALL}\n")
                break
            continue

        # process valid choices based on decision table rule
        print(f"\n{Fore.BLUE} {rule['output_message']}{Style.RESET_ALL}")

        if rule["rule_number"] == "R1":     # Daily Reflection
            date, time, answers, current_mood = daily_reflection(name, initial_mood)
            save_entry("Daily Reflection", date, time, answers, name, current_mood, initial_mood)
            invalid_count = 0               # Reset on successful action
            initial_mood = None             # Clear initial mood after first use

        elif rule["rule_number"] == "R2":   # Weekly Check-in
            date, answers = weekly_check_in(name)
            save_entry("Weekly Check-in", date, "Weekly", answers, name)
            invalid_count = 0               # Reset on successful action

        elif rule["rule_number"] == "R3":   # View Entries
            view_previous_entries(name)
            invalid_count = 0               # Reset on successful action

        elif rule["rule_number"] == "R4":   # Exit Program
            print(f"\nThank you for doing an entry today, {name}.")
            print(f"Remember: Progress, not perfection. You've got this!")
            print(f"Hope to see you tomorrow.\n")
            break

# Run the program
if __name__ == "__main__":
    main()