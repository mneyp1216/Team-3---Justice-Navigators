# mood_assessment.py
"""
Mood Assessment Module - Pure function with guard clauses and normalization
Now includes session tracking and trend analysis
"""

import datetime

def assess_mood(mood_input):
    """
    Pure function to assess mood with guard clauses and normalization.
    
    Guard Clauses:
    1. Check if input is None
    2. Check if input is empty after stripping
    3. Check if input is a string or number
    4. Check if input can be converted to int
    
    Normalization:
    1. Convert to lowercase if string
    2. Strip whitespace
    3. Convert to int if possible
    
    Mood Scale:
    1: Critical - Distress, overwhelm, crisis indicators
    2: Low - Struggling, stressed, emotionally heavy
    3: Mid - Okay, some good/some strain
    4: High - Thriving, motivated, doing well
    5: Indifferent - Neutral
    
    Returns:
        dict: Contains mood level, description, and timestamp or None if invalid
    """
    # GUARD CLAUSE 1: Check if input is None
    if mood_input is None:
        return None
    
    # GUARD CLAUSE 2: Check if input is string or int
    if not isinstance(mood_input, (str, int)):
        return None
    
    # NORMALIZATION: Convert to string for processing
    if isinstance(mood_input, int):
        mood_str = str(mood_input)
    else:
        mood_str = mood_input
    
    # Normalize: lowercase and strip
    normalized = mood_str.lower().strip()
    
    # GUARD CLAUSE 3: Check if empty after normalization
    if not normalized:
        return None
    
    # Mood mapping with synonyms
    mood_map = {
        # Level 1: Critical
        "1": {"level": 1, "description": "Critical - Distress, overwhelm, crisis indicators"},
        "critical": {"level": 1, "description": "Critical - Distress, overwhelm, crisis indicators"},
        "distress": {"level": 1, "description": "Critical - Distress, overwhelm, crisis indicators"},
        "crisis": {"level": 1, "description": "Critical - Distress, overwhelm, crisis indicators"},
        "overwhelmed": {"level": 1, "description": "Critical - Distress, overwhelm, crisis indicators"},
        
        # Level 2: Low
        "2": {"level": 2, "description": "Low - Struggling, stressed, emotionally heavy"},
        "low": {"level": 2, "description": "Low - Struggling, stressed, emotionally heavy"},
        "struggling": {"level": 2, "description": "Low - Struggling, stressed, emotionally heavy"},
        "stressed": {"level": 2, "description": "Low - Struggling, stressed, emotionally heavy"},
        "heavy": {"level": 2, "description": "Low - Struggling, stressed, emotionally heavy"},
        "sad": {"level": 2, "description": "Low - Struggling, stressed, emotionally heavy"},
        
        # Level 3: Mid
        "3": {"level": 3, "description": "Mid - Okay, some good/some strain"},
        "mid": {"level": 3, "description": "Mid - Okay, some good/some strain"},
        "okay": {"level": 3, "description": "Mid - Okay, some good/some strain"},
        "medium": {"level": 3, "description": "Mid - Okay, some good/some strain"},
        "mixed": {"level": 3, "description": "Mid - Okay, some good/some strain"},
        "alright": {"level": 3, "description": "Mid - Okay, some good/some strain"},
        
        # Level 4: High
        "4": {"level": 4, "description": "High - Thriving, motivated, doing well"},
        "high": {"level": 4, "description": "High - Thriving, motivated, doing well"},
        "thriving": {"level": 4, "description": "High - Thriving, motivated, doing well"},
        "motivated": {"level": 4, "description": "High - Thriving, motivated, doing well"},
        "good": {"level": 4, "description": "High - Thriving, motivated, doing well"},
        "great": {"level": 4, "description": "High - Thriving, motivated, doing well"},
        "happy": {"level": 4, "description": "High - Thriving, motivated, doing well"},
        
        # Level 5: Indifferent
        "5": {"level": 5, "description": "Indifferent - Neutral"},
        "indifferent": {"level": 5, "description": "Indifferent - Neutral"},
        "neutral": {"level": 5, "description": "Indifferent - Neutral"},
        "ok": {"level": 5, "description": "Indifferent - Neutral"},
        "fine": {"level": 5, "description": "Indifferent - Neutral"},
        "meh": {"level": 5, "description": "Indifferent - Neutral"},
    }
    
    # Get the mood result
    mood_result = mood_map.get(normalized, None)
    
    if mood_result:
        # Add timestamp
        mood_result['timestamp'] = datetime.datetime.now().isoformat()
        return mood_result
    
    return None


def display_mood_scale():
    """Display the mood assessment scale"""
    scale = """
    MOOD ASSESSMENT SCALE:
    =====================
    1: Critical - Distress, overwhelm, crisis indicators
    2: Low - Struggling, stressed, emotionally heavy
    3: Mid - Okay, some good/some strain
    4: High - Thriving, motivated, doing well
    5: Indifferent - Neutral
    
    You can use numbers (1-5) or keywords like:
    "critical", "low", "mid/okay", "high/good", "indifferent/neutral"
    """
    return scale


def get_mood_statistics(mood_history):
    """
    Pure function to calculate mood statistics
    
    Args:
        mood_history: List of mood assessment results
        
    Returns:
        dict: Statistics including average, counts, etc.
    """
    if not mood_history:
        return None
    
    # Extract levels from valid mood assessments
    levels = []
    for mood in mood_history:
        if mood and isinstance(mood, dict) and 'level' in mood:
            levels.append(mood['level'])
    
    if not levels:
        return None
    
    # Calculate statistics
    return {
        "average": sum(levels) / len(levels),
        "count": len(levels),
        "min": min(levels),
        "max": max(levels),
        "levels": levels,
        "trend": "improving" if levels[-1] > levels[0] else "declining" if levels[-1] < levels[0] else "stable"
    }


def get_mood_emoji(level):
    """Return emoji representation of mood level"""
    emoji_map = {
        1: "😫",  # Critical
        2: "😔",  # Low
        3: "😐",  # Mid
        4: "😊",  # High
        5: "😶",  # Indifferent
    }
    return emoji_map.get(level, "❓")


def interpret_mood_change(initial_mood, current_mood):
    """
    Interpret mood change between initial and current mood
    
    Returns:
        str: Interpretation of mood change
    """
    if not initial_mood or not current_mood:
        return "No comparison available"
    
    change = current_mood['level'] - initial_mood['level']
    
    if change > 0:
        return f"Mood improved by {change} level(s) 🌟"
    elif change < 0:
        return f"Mood decreased by {abs(change)} level(s) 💭"
    else:
        return "Mood remained steady ↔️"