from client import EarleyParser

def main():
    print("=== Testing Earley Context-Free Grammar Parser ===")
    grammar = {
        "S": [("NP", "VP")],
        "NP": [("det", "noun")],
        "VP": [("verb", "NP")]
    }
    earley = EarleyParser(grammar)
    tokens = ["det", "noun", "verb", "det", "noun"]
    valid = earley.parse(tokens)
    print("Parsing valid sentence:", valid)
    assert valid

    invalid = earley.parse(["noun", "verb"])
    print("Parsing invalid sequence:", invalid)
    assert not invalid
    print("=== All tests passed successfully! ===")

if __name__ == "__main__":
    main()
