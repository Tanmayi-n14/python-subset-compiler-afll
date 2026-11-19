"""
Python Subset Syntax Validator — Demonstration Script
Runs sample valid and invalid code snippets through the Lexer and Parser.
"""

import sys
from pathlib import Path

try:
    from parser import parser
except ImportError:
    print("Error: 'ply' is required. Run 'pip install ply' or 'pip install -r requirements.txt'")
    sys.exit(1)

DEMO_SNIPPETS = [
    ("List Comprehension", "cubes = [x**3 for x in numbers if x % 2 == 0]"),
    ("Context Manager", "with open('dataset.csv', 'r') as stream:"),
    ("Lambda Expression", "square = lambda a, b: a * b + 10"),
    ("Module Import", "from collections import defaultdict, Counter"),
    ("Set Literal", "unique_ids = {101, 202, 303, 404}"),
    ("Invalid Syntax (Expected Fail)", "with open('file') without error:"),
]

def main():
    print("=" * 65)
    print("  PLY-Based Python Subset Grammar Validator — Live Demos")
    print("=" * 65)
    
    for category, code in DEMO_SNIPPETS:
        print(f"\nFeature: {category}")
        print(f"Code   : {code}")
        try:
            res = parser.parse(code, tracking=True)
            if res is not None or code.strip() == "":
                print("Result : ✅ VALID SYNTAX (Accepted by CFG)")
            else:
                print("Result : ❌ SYNTAX ERROR (Rejected by Parser)")
        except Exception as e:
            print(f"Result : ❌ PARSE ERROR: {e}")

if __name__ == '__main__':
    main()
