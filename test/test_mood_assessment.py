# test_mood_assessment.py
"""
Unit tests for mood assessment functions
"""

import unittest
import sys
import os

# Add current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from src.mood_assessment import assess_mood, get_mood_statistics

class TestMoodAssessment(unittest.TestCase):
    """Test cases for mood assessment functions"""
    
    def test_assess_mood_valid_numbers(self):
        """Test valid number inputs"""
        test_cases = [
            ("1", 1, "Critical"),
            ("2", 2, "Low"),
            ("3", 3, "Mid"),
            ("4", 4, "High"),
            ("5", 5, "Indifferent"),
            (1, 1, "Critical"),  # Integer input
            (2, 2, "Low"),       # Integer input
        ]
        
        for input_val, expected_level, description in test_cases:
            with self.subTest(input=input_val):
                result = assess_mood(input_val)
                self.assertIsNotNone(result, f"Failed for input: {input_val}")
                self.assertEqual(result['level'], expected_level, 
                               f"Level mismatch for {input_val}")
                self.assertIn(description.lower(), result['description'].lower())
    
    def test_assess_mood_valid_keywords(self):
        """Test valid keyword inputs"""
        test_cases = [
            ("critical", 1),
            ("distress", 1),
            ("low", 2),
            ("struggling", 2),
            ("mid", 3),
            ("okay", 3),
            ("high", 4),
            ("thriving", 4),
            ("indifferent", 5),
            ("neutral", 5),
        ]
        
        for input_val, expected_level in test_cases:
            with self.subTest(input=input_val):
                result = assess_mood(input_val)
                self.assertIsNotNone(result, f"Failed for input: {input_val}")
                self.assertEqual(result['level'], expected_level)
    
    def test_assess_mood_case_insensitive(self):
        """Test case insensitive inputs"""
        test_cases = ["CRITICAL", "Low", "MID", "High", "INDIFFERENT"]
        
        for input_val in test_cases:
            with self.subTest(input=input_val):
                result = assess_mood(input_val)
                self.assertIsNotNone(result, f"Failed for input: {input_val}")
    
    def test_assess_mood_guard_clauses(self):
        """Test guard clauses reject invalid inputs"""
        # Test None input
        self.assertIsNone(assess_mood(None))
        
        # Test empty string
        self.assertIsNone(assess_mood(""))
        self.assertIsNone(assess_mood("   "))
        
        # Test invalid type
        self.assertIsNone(assess_mood([]))
        self.assertIsNone(assess_mood({}))
        self.assertIsNone(assess_mood(1.5))
        
        # Test invalid values
        self.assertIsNone(assess_mood("0"))
        self.assertIsNone(assess_mood("6"))
        self.assertIsNone(assess_mood("happy"))
        self.assertIsNone(assess_mood("sad"))
    
    def test_assess_mood_pure_function(self):
        """Test that function is pure (same output for same input)"""
        test_inputs = ["1", "high", "mid", "invalid", 3, "  High  "]
        
        for input_val in test_inputs:
            # Call function twice with same input
            result1 = assess_mood(input_val)
            result2 = assess_mood(input_val)
            
            # Should get same result both times
            self.assertEqual(result1, result2,
                           f"Function not pure for input: {input_val}")
    
    def test_get_mood_statistics(self):
        """Test mood statistics calculation"""
        # Test with valid mood history
        mood_history = [
            {"level": 1, "description": "Critical"},
            {"level": 3, "description": "Mid"},
            {"level": 4, "description": "High"},
            {"level": 2, "description": "Low"},
            {"level": 3, "description": "Mid"},
        ]
        
        stats = get_mood_statistics(mood_history)
        self.assertIsNotNone(stats)
        self.assertEqual(stats["average"], (1+3+4+2+3)/5)
        self.assertEqual(stats["count"], 5)
        self.assertEqual(stats["min"], 1)
        self.assertEqual(stats["max"], 4)
        self.assertEqual(stats["levels"], [1, 3, 4, 2, 3])
    
    def test_get_mood_statistics_empty(self):
        """Test statistics with empty or invalid history"""
        # Test empty list
        self.assertIsNone(get_mood_statistics([]))
        
        # Test list with None values
        self.assertIsNone(get_mood_statistics([None, None]))
        
        # Test list with invalid mood dicts
        self.assertIsNone(get_mood_statistics([{"not_level": 1}, {"test": 2}]))


def run_tests():
    """Run all tests"""
    print("Running Mood Assessment Unit Tests...")
    print("=" * 60)
    
    # Create test suite
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestMoodAssessment)
    
    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Print summary
    print("\n" + "=" * 60)
    print("TEST SUMMARY")
    print("=" * 60)
    
    if result.wasSuccessful():
        print("✓ All tests passed!")
        print(f"Tests run: {result.testsRun}")
        return True
    else:
        print("✗ Some tests failed")
        print(f"Tests run: {result.testsRun}")
        print(f"Failures: {len(result.failures)}")
        print(f"Errors: {len(result.errors)}")
        return False


if __name__ == "__main__":
    success = run_tests()
    sys.exit(0 if success else 1)