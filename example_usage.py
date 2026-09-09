"""Example usage for Earley CFG Parser Skill."""
from client import EarleyParser

def main():
    print("Executing Earley CFG Parser...")
    grammar = {
        "S": [["NP", "VP"]],
        "NP": [["agent"], ["the", "agent"]],
        "VP": [["learns"], ["learns", "fast"]]
    }
    parser = EarleyParser(grammar, "S")
    valid = parser.parse(["the", "agent", "learns", "fast"])
    print("Sentence valid according to CFG:", valid)
    assert valid == True

    invalid = parser.parse(["agent", "sleeps"])
    assert invalid == False
    print("Earley CFG Parser verified successfully!")

if __name__ == "__main__":
    main()
