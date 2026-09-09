"""
Autonomous Agent Earley CFG Chart Parser Skill
Pure Python Standard Library implementation.
"""
from typing import List, Dict, Any

class EarleyParser:
    """
    Earley parser supporting general context-free grammars (CFGs).
    """
    def __init__(self, grammar: Dict[str, List[List[str]]], start_symbol: str = "S"):
        self.grammar = grammar
        self.start = start_symbol

    def parse(self, tokens: List[str]) -> bool:
        chart = [[] for _ in range(len(tokens) + 1)]
        for prod in self.grammar.get(self.start, []):
            chart[0].append((self.start, prod, 0, 0))

        for i in range(len(tokens) + 1):
            j = 0
            while j < len(chart[i]):
                lhs, rhs, dot, origin = chart[i][j]
                j += 1

                if dot < len(rhs):
                    next_symbol = rhs[dot]
                    if next_symbol in self.grammar:
                        for prod in self.grammar[next_symbol]:
                            state = (next_symbol, prod, 0, i)
                            if state not in chart[i]:
                                chart[i].append(state)
                    elif i < len(tokens) and next_symbol == tokens[i]:
                        state = (lhs, rhs, dot + 1, origin)
                        if state not in chart[i + 1]:
                            chart[i + 1].append(state)
                else:
                    for state in chart[origin]:
                        s_lhs, s_rhs, s_dot, s_origin = state
                        if s_dot < len(s_rhs) and s_rhs[s_dot] == lhs:
                            new_state = (s_lhs, s_rhs, s_dot + 1, s_origin)
                            if new_state not in chart[i]:
                                chart[i].append(new_state)

        for lhs, rhs, dot, origin in chart[len(tokens)]:
            if lhs == self.start and dot == len(rhs) and origin == 0:
                return True
        return False
