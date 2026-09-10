class EarleyParser:
    """
    Earley Context-Free Grammar Chart Parser.
    Handles recursive and ambiguous grammars with predictor, scanner, and completer states.
    """
    def __init__(self, grammar):
        self.grammar = grammar

    def parse(self, tokens):
        chart = [[] for _ in range(len(tokens) + 1)]
        for rhs in self.grammar.get("S", []):
            chart[0].append(("S", rhs, 0, 0))

        for i in range(len(tokens) + 1):
            added = True
            while added:
                added = False
                for state in list(chart[i]):
                    lhs, rhs, dot, origin = state
                    if dot < len(rhs):
                        next_sym = rhs[dot]
                        if next_sym in self.grammar:
                            for prod in self.grammar[next_sym]:
                                new_st = (next_sym, prod, 0, i)
                                if new_st not in chart[i]:
                                    chart[i].append(new_st)
                                    added = True
                        elif i < len(tokens) and next_sym == tokens[i]:
                            new_st = (lhs, rhs, dot + 1, origin)
                            if new_st not in chart[i + 1]:
                                chart[i + 1].append(new_st)
                    else:
                        for prev_st in list(chart[origin]):
                            p_lhs, p_rhs, p_dot, p_orig = prev_st
                            if p_dot < len(p_rhs) and p_rhs[p_dot] == lhs:
                                new_st = (p_lhs, p_rhs, p_dot + 1, p_orig)
                                if new_st not in chart[i]:
                                    chart[i].append(new_st)
                                    added = True

        for state in chart[len(tokens)]:
            lhs, rhs, dot, origin = state
            if lhs == "S" and dot == len(rhs) and origin == 0:
                return True
        return False
