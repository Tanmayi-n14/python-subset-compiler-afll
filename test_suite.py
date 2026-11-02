"""
Automated Test Suite for Python Subset Syntax Validator (AFLL Coursework)
Runs test cases covering all 5 core CFG features and verifies grammar rules.
"""

from parser import parser

def test_syntax(cases):
    passed = 0
    total = len(cases)
    print(f"\nRunning {total} test cases...")
    print("=" * 60)
    
    for idx, (code, should_be_valid, description) in enumerate(cases, 1):
        print(f"[{idx}/{total}] Testing: {code}")
        print(f"       Description: {description}")
        result = parser.parse(code, tracking=True)
        is_valid = result is not None or code.strip() == ''
        
        status = "PASS" if is_valid == should_be_valid else "FAIL"
        if status == "PASS":
            passed += 1
        print(f"       Result: {status} (Expected: {'Valid' if should_be_valid else 'Invalid'})\n")
        
    print("=" * 60)
    print(f"Summary: {passed}/{total} tests passed.")
    return passed == total

if __name__ == "__main__":
    test_cases = [
        # 1. List Comprehensions
        ("a = [x*x for x in nums]", True, "Basic list comprehension"),
        ("b = [x+y/2 for x in data]", True, "List comprehension with arithmetic expression"),
        ("c = [x for x in items if x > 10]", True, "Conditional list comprehension"),
        ("d = [x for x in items if x == 0]", True, "Conditional list comprehension with equality"),
        ("e = [x + (y*2) for x in y if z < 1]", True, "Complex nested expression list comprehension"),
        ("a = [x for x in range(10)]", False, "Invalid: function call inside iterator"),
        
        # 2. With Statements
        ("with open(\"file.txt\") as f:", True, "Basic with-statement"),
        ("with my_func(\"data.csv\") as data:", True, "With-statement with custom function"),
        ("with open(filename) as f:", False, "Invalid: identifier argument instead of string"),
        
        # 3. Lambda Assignments
        ("add = lambda a, b: a + b", True, "Multi-argument lambda"),
        ("gt = lambda x: x > 10", True, "Comparison lambda"),
        ("empty = lambda : 1", True, "Zero-argument lambda"),
        ("logic = lambda x: x >= 0", True, "Relational lambda"),
        
        # 4. From-Import Statements
        ("from math import sqrt", True, "Single import"),
        ("from os import path, environ", True, "Multiple imports"),
        ("from utils import *", True, "Wildcard import"),
        ("from utils import helper as h", True, "Import with alias"),
        ("from other import func, test as t, old_func", True, "Mixed imports with alias"),
        
        # 5. Set Declarations
        ("a = {1, 2, 3}", True, "Numeric set literal"),
        ("b = {1 + 2, x * 3, y / 4}", True, "Expression set literal"),
        ("c = {}", True, "Empty set literal"),
        ("d = {x > 10, y == 0, 1}", True, "Set with relational expressions"),
        ("a = {1: 2}", False, "Invalid: dictionary colon syntax"),
    ]
    
    test_syntax(test_cases)
