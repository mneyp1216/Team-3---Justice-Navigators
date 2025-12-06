# Justice-Navigator---Journal-Companion

Capstone Project - AI Edge '25

## Team Members

Name                    GitHub Handle

- Miguel Pena           - [@mneyp1216](https://github.com/mneyp1216)
- DeAnna Hoskins        - [@deannarhoskins](https://github.com/deannarhoskins)
- Michael Washington    - [@michaeljwashington1111](https://github.com/michaeljwashington1111)
- Roland Carlisle       - [@roceegithub](https://github.com/roceegithub)

## Purpose

- This application is a CLI based Journal Companion that assists the user with journal entries by determining the users mood, prompting the user based upon their mood by asking questions about the users day, and uses OpenAI's API to provide empathetic repsonses.
- The goal is to be uplift and assist with positive thinking and provide self help guidance.
- The Journal provides a personalized encounter that can help in moments of need, tracks feelings and provides words of encouragement.

## Setup

- Clone the Repository
- Install Python 3.10+
- (Optional) Create a Virtual Environment
- Install Colorama
- Install Pandas
- Install openai
- Import Numpy
- Import OS
- Import Datetime
- Import OpenAi
- Import Optional, Dict, Any
- Import Json

## How to run

- Once the system is setup the key will be SRC/ python app.py and run from the CLI in your terminal.
- System will introduce the developers and provide a header designating the name of the file.
- We would prefer your name as the system is created with the user in mind as to personalize the experience, but it is up to the user to decide which name it would like the system to refer to him as.

## Usage Instructions for  

- Run the application in the CLI using src/app.py.
- Select your mood when prompted.
- The companion will return a reflection prompt based on tone and safety rules.
- The companion will reconcile your stated mood compared to your responses.
- The companion will provide a randomn prompt to encourage journaling.
  
## Responsible AI Use

- AI is a tool, not a source of truth. Users must verify outputs.
- No sensitive or identifying data should be entered into prompts.
- This journal companion is not a crisis or therapeutic tool.
- AI responses may be incomplete or biased; safe defaults are used.
- The tool does not provide medical, legal, or mental health advice.
- AI was used to help structure initial drafts. All final content was authored, reviewed, and revised by the team.

## Prompt Library Link

- <https://docs.google.com/document/d/1NbQN0IfGE-1KPqisY_vnYpuQXiinzinBp4JX-5LuXg8/edit?usp=drive_link>

## Feature Spec

## User determined mood rating (MVP)

 As a user who wants to check in with myself,
 I want to select my mood and receive a journaling prompt,
 so I can reflect on how I’m feeling and what I need today.

 ## System generated mood rating interpreter

 The user can respond to the mood related questions and basd upon the Journal's rating, the system will notify the user if their is descrpency between the users dervied mood rating versus the system, and provide the user an opportunity jouranal about the descrpency. 

## Mood based user journal prompt 

Depending on user determined mood rating a user journal prompt is produced. 

##  AI generated feedback  
AI will be prompted using the users responses to select user journal prompts provide productive insight regarding the users journal entry. 

## Randomn user journal prompt
A usser will be randomonly assigned a prompt to encourage a journal entry related to the prompt. 

## Acceptance Criteria

When I run src/app.py, the program greets me.
I see a list of mood options (e.g., critical/ low / medium / high).
When I select a valid mood, I receive one journaling prompt.
If I enter something invalid, I receive a safe, default reflection.
The prompt must follow tone, safety, and system instructions.


## Test Plan

Highlevel Testing plan:

Test each user intent, 
Test each module, 
Test API connection, 
Test application sequence
Test Test system prompt 
Input “high” - Returns high-energy prompt.
Input “low” - Returns grounding prompt.
Input “banana” - Returns safe default prompt.


## Input 
-user inputs: name, rates the day 1-5, answers 5 questions to recieve the journals rating, selects a journal option daily or weekly, etc.), 

## Output
- moood dependent encouragement message + System generated mood rating + mood dependent user journal prompt 


