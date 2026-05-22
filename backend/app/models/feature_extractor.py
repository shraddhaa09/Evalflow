import ast
import re
import math
import numpy as np


def extract_features(code: str) -> np.ndarray:

    lines = code.splitlines()
    non_empty = [l for l in lines if l.strip()]

    lines_of_code = len(lines)

    avg_line_length = (
        np.mean([len(l) for l in non_empty])
        if non_empty else 0
    )

    comment_lines = sum(
        1 for l in lines
        if l.strip().startswith("#")
    )

    comment_ratio = (
        comment_lines /
        max(lines_of_code, 1)
    )

    function_count = len(
        re.findall(r"\bdef\b", code)
    )

    loop_count = len(
        re.findall(r"\b(for|while)\b", code)
    )

    vars_ = re.findall(
        r"\b[a-zA-Z_][a-zA-Z0-9_]*\b",
        code
    )

    variable_naming_score = (
        len([
            v for v in vars_
            if "_" in v or len(v) > 3
        ]) / max(len(vars_), 1)
    )

    def depth(node):
        children = list(ast.iter_child_nodes(node))

        if not children:
            return 1

        return 1 + max(
            depth(c)
            for c in children
        )

    try:
        tree = ast.parse(code)
        nesting_depth = depth(tree)
        ast_node_count = sum(
            1 for _ in ast.walk(tree)
        )

    except:
        nesting_depth = 0
        ast_node_count = 0

    tokens = code.split()

    if tokens:

        freq = {}

        for t in tokens:
            freq[t] = freq.get(t, 0) + 1

        probs = [
            v / len(tokens)
            for v in freq.values()
        ]

        token_entropy = -sum(
            p * math.log(p + 1e-9)
            for p in probs
        )

    else:
        token_entropy = 0

    import_count = len(
        re.findall(r"\bimport\b", code)
    )

    try_except_count = len(
        re.findall(r"\btry\b", code)
    )

    comprehension_count = len(
        re.findall(
            r"\[.*for.*in.*\]",
            code
        )
    )

    unique_identifier_ratio = (
        len(set(tokens))
        / max(len(tokens), 1)
    )

    return np.array([[
        lines_of_code,
        avg_line_length,
        comment_ratio,
        function_count,
        loop_count,
        variable_naming_score,
        nesting_depth,
        token_entropy,
        import_count,
        try_except_count,
        comprehension_count,
        unique_identifier_ratio,
        ast_node_count
    ]])