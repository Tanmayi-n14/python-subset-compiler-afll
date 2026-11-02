from parser import parser

def main():
    print("Python Syntax Validator (CFG-based)")
    print("Enter Python code. Type 'exit' to quit.")
    
    while True:
        try:
            s = input('>>> ')
        except EOFError:
            break
        if not s or s.lower() == 'exit':
            break
        result = parser.parse(s, tracking=True)
        if result is not None or s.strip() == '':
            print("--------------------")
            print("Valid Syntax!")
            print("--------------------")

if __name__ == "__main__":
    main()
